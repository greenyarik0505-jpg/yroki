import math
import os
import random
import sys
import pygame

# ----------------------------
# Настройки игры
# ----------------------------
WIDTH, HEIGHT = 288, 512
GROUND_H = 112
FPS = 60

PIPE_SPEED = 120
PIPE_GAP = 100
PIPE_SPAWN_INTERVAL = 1.25

GRAVITY = 900
FLAP_IMPULSE = -280
MAX_FALL_SPEED = 400

BIRD_X = 56

# Цвета
SKY_TOP = (89, 201, 255)
SKY_BOTTOM = (144, 220, 255)
PIPE_GREEN = (83, 189, 57)
PIPE_DARK = (68, 156, 46)
GROUND_BROWN = (222, 216, 149)
GROUND_DARK = (204, 198, 135)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

pygame.init()
pygame.display.set_caption("Flappy Bird (pygame)")
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
font_big = pygame.font.SysFont("Arial", 40, bold=True)
font_mid = pygame.font.SysFont("Arial", 24, bold=True)
font_small = pygame.font.SysFont("Arial", 18)

# ----------------------------
# Утилиты
# ----------------------------
def draw_gradient(surface, top_color, bottom_color):
    for y in range(HEIGHT - GROUND_H):
        t = y / float(HEIGHT - GROUND_H)
        r = int(top_color[0] * (1 - t) + bottom_color[0] * t)
        g = int(top_color[1] * (1 - t) + bottom_color[1] * t)
        b = int(top_color[2] * (1 - t) + bottom_color[2] * t)
        pygame.draw.line(surface, (r, g, b), (0, y), (WIDTH, y))

def load_highscore(path="flappy_highscore.txt"):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return int(f.read().strip())
    except Exception:
        return 0

def save_highscore(score, path="flappy_highscore.txt"):
    try:
        old = load_highscore(path)
        if score > old:
            with open(path, "w", encoding="utf-8") as f:
                f.write(str(score))
    except Exception:
        pass

# ----------------------------
# Классы
# ----------------------------
class Bird:
    def __init__(self):
        self.reset()

    def reset(self):
        self.x = BIRD_X
        self.y = HEIGHT // 2
        self.vy = 0.0
        self.radius = 12
        self.alive = True
        self.angle = 0.0
        self.anim_t = 0.0
        # configurable colors (can be changed in settings)
        self.body_color = (255, 235, 130)
        self.wing_color = (250, 210, 90)
        # ensure radius/visual scale matches current window size
        self.update_scale()

    def flap(self):
        self.vy = FLAP_IMPULSE

    def update(self, dt):
        self.vy = min(self.vy + GRAVITY * dt, MAX_FALL_SPEED)
        self.y += self.vy * dt

        target_angle = -25 if self.vy < -50 else min(70, 70 * (self.vy / MAX_FALL_SPEED))
        self.angle += (target_angle - self.angle) * min(1, 8 * dt)
        self.anim_t += dt

    def draw(self, surface):
        # draw scaled bird according to current scale
        scale = min(WIDTH / 288.0, HEIGHT / 512.0)
        w = max(8, int(50 * scale))
        h = max(8, int(40 * scale))
        surf = pygame.Surface((w, h), pygame.SRCALPHA)
        cx, cy = w // 2, h // 2

        body_color = self.body_color
        wing_color = self.wing_color
        eye_white = (255, 255, 255)
        eye_black = (0, 0, 0)
        beak = (255, 140, 0)

        wing_offset = int(math.sin(self.anim_t * 12.0) * max(1, int(3 * scale)))

        pygame.draw.ellipse(surf, body_color, (cx - int(14 * scale), cy - int(12 * scale), int(28 * scale), int(24 * scale)))
        pygame.draw.ellipse(surf, wing_color, (cx - int(6 * scale), cy - int(6 * scale) + wing_offset, int(14 * scale), int(12 * scale)))
        pygame.draw.polygon(surf, beak, [(cx + int(12 * scale), cy), (cx + int(24 * scale), cy - int(4 * scale)), (cx + int(24 * scale), cy + int(4 * scale))])
        pygame.draw.circle(surf, eye_white, (cx + int(4 * scale), cy - int(6 * scale)), max(1, int(5 * scale)))
        pygame.draw.circle(surf, eye_black, (cx + int(6 * scale), cy - int(6 * scale)), max(1, int(2 * scale)))

        rotated = pygame.transform.rotate(surf, self.angle)
        rect = rotated.get_rect(center=(self.x, self.y))
        surface.blit(rotated, rect)

    def update_scale(self):
        # update radius to scale with window size
        scale = min(WIDTH / 288.0, HEIGHT / 512.0)
        self.radius = max(4, int(12 * scale))

    @property
    def rect(self):
        return pygame.Rect(self.x - self.radius, self.y - self.radius, self.radius * 2, self.radius * 2)

class PipePair:
    WIDTH = 52

    def __init__(self, x):
        self.x = x
        self.passed = False
        sky_h = HEIGHT - GROUND_H
        gap_center = random.randint(80, sky_h - 80)
        self.top_bottom = gap_center - PIPE_GAP // 2
        self.bottom_top = gap_center + PIPE_GAP // 2

    def update(self, dt):
        self.x -= PIPE_SPEED * dt

    def offscreen(self):
        return self.x + self.WIDTH < 0

    def draw(self, surface):
        top_rect = pygame.Rect(int(self.x), 0, self.WIDTH, max(0, int(self.top_bottom)))
        bottom_rect = pygame.Rect(int(self.x), int(self.bottom_top), self.WIDTH, (HEIGHT - GROUND_H) - int(self.bottom_top))

        for r in (top_rect, bottom_rect):
            pygame.draw.rect(surface, PIPE_DARK, r)
            inner = r.inflate(-6, 0)
            pygame.draw.rect(surface, PIPE_GREEN, inner)

        pygame.draw.rect(surface, PIPE_DARK, (int(self.x) - 2, top_rect.bottom - 10, self.WIDTH + 4, 10))
        pygame.draw.rect(surface, PIPE_DARK, (int(self.x) - 2, bottom_rect.top, self.WIDTH + 4, 10))

    def collides(self, bird_rect: pygame.Rect):
        top_rect = pygame.Rect(int(self.x), 0, self.WIDTH, max(0, int(self.top_bottom)))
        bottom_rect = pygame.Rect(int(self.x), int(self.bottom_top), self.WIDTH, (HEIGHT - GROUND_H) - int(self.bottom_top))
        return bird_rect.colliderect(top_rect) or bird_rect.colliderect(bottom_rect)

class Ground:
    def __init__(self):
        self.scroll_x = 0.0

    def update(self, dt):
        self.scroll_x = (self.scroll_x + PIPE_SPEED * dt) % WIDTH

    def draw(self, surface):
        ground_y = HEIGHT - GROUND_H
        pygame.draw.rect(surface, GROUND_BROWN, (0, ground_y, WIDTH, GROUND_H))
        pygame.draw.rect(surface, GROUND_DARK, (0, ground_y, WIDTH, 10))

        tile_w = 24
        x = -self.scroll_x
        while x < WIDTH:
            pygame.draw.rect(surface, (210, 200, 130), (int(x), ground_y + 28, tile_w, 6))
            pygame.draw.rect(surface, (196, 188, 122), (int(x), ground_y + 46, tile_w, 6))
            x += tile_w + 12

# ----------------------------
# Игровое состояние
# ----------------------------
class Game:
    def __init__(self):
        # Gameplay objects
        self.bird = Bird()
        self.pipes = []
        self.ground = Ground()
        self.time_since_pipe = 0.0
        self.score = 0
        self.best = load_highscore()
        self.state = "ready"

        # Settings/UI
        self.settings_open = False

        # sky presets: list of (top, bottom)
        self.sky_presets = [
            ((89,201,255),(144,220,255)),
            ((30,30,60),(120,90,180)),
            ((255,180,120),(255,220,180)),
            ((20,40,80),(80,110,160)),          # deep blue dusk
            ((255,120,50),(255,200,140)),       # fiery sunset
            ((120,30,150),(200,150,240)),      # purple dream
            ((30,120,90),(140,220,180)),       # greenish meadow
        ]
        self.sky_index = 0

        # pipe color presets: (inner, outer)
        self.pipe_color_presets = [
            ((83,189,57),(68,156,46)),   # original green
            ((180,50,50),(140,40,40)),   # red
            ((60,140,200),(40,110,170)), # blue
            ((200,160,60),(170,140,50)), # sandy
            ((120,120,120),(90,90,90)),  # gray
        ]
        self.pipe_color_index = 0

        # ground color presets: (top, dark)
        self.ground_color_presets = [
            ((222,216,149),(204,198,135)),   # default sandy
            ((200,180,150),(170,150,130)),   # muted sand
            ((180,140,100),(150,120,90)),    # brown earth
            ((100,160,120),(80,130,100)),    # greenish turf
            ((160,160,200),(130,130,170)),   # twilight ground
        ]
        self.ground_color_index = 0

        # bird color presets
        self.bird_color_presets = [
            ((255,235,130),(250,210,90)),
            ((200,100,100),(180,80,80)),
            ((130,200,255),(100,170,230)),
            ((180,255,150),(150,230,120)),
            ((255,200,200),(220,150,150)),
            ((200,255,220),(150,230,190)),
            ((240,200,255),(210,160,230)),
            ((255,240,180),(240,210,140)),
        ]
        self.bird_color_index = 0

        # apply initial colors and cached assets
        self.apply_bird_color()
        self.sky_surface = None
        self.recreate_sky()
        self.apply_pipe_color()
        self.apply_ground_color()

        # gameover timing: auto-reset after this many seconds
        self.gameover_time = None
        self.auto_reset_delay = 1.5

    def apply_bird_color(self):
        body, wing = self.bird_color_presets[self.bird_color_index]
        self.bird.body_color = body
        self.bird.wing_color = wing

    def recreate_sky(self):
        """Create a cached gradient surface sized to the current window.
        This avoids redrawing the gradient line-by-line every frame (expensive at large sizes).
        """
        try:
            sky_h = max(1, HEIGHT - GROUND_H)
            surf = pygame.Surface((WIDTH, sky_h))
            top_c, bottom_c = self.sky_presets[self.sky_index]
            for y in range(sky_h):
                t = y / float(sky_h)
                r = int(top_c[0] * (1 - t) + bottom_c[0] * t)
                g = int(top_c[1] * (1 - t) + bottom_c[1] * t)
                b = int(top_c[2] * (1 - t) + bottom_c[2] * t)
                pygame.draw.line(surf, (r, g, b), (0, y), (WIDTH, y))
            self.sky_surface = surf
        except Exception:
            self.sky_surface = None

    def cycle_bird_color(self):
        self.bird_color_index = (self.bird_color_index + 1) % len(self.bird_color_presets)
        self.apply_bird_color()

    def apply_pipe_color(self):
        """Apply current pipe color preset into module-level globals used for drawing."""
        global PIPE_GREEN, PIPE_DARK
        inner, outer = self.pipe_color_presets[self.pipe_color_index]
        PIPE_GREEN = inner
        PIPE_DARK = outer

    def cycle_pipe_color(self):
        self.pipe_color_index = (self.pipe_color_index + 1) % len(self.pipe_color_presets)
        self.apply_pipe_color()

    def apply_ground_color(self):
        """Apply current ground color preset into module-level globals used for drawing."""
        global GROUND_BROWN, GROUND_DARK
        top, dark = self.ground_color_presets[self.ground_color_index]
        GROUND_BROWN = top
        GROUND_DARK = dark

    def cycle_ground_color(self):
        self.ground_color_index = (self.ground_color_index + 1) % len(self.ground_color_presets)
        self.apply_ground_color()

    def reset_settings(self):
        """Reset user-visible settings back to defaults (keeps gameplay state untouched)."""
        self.sky_index = 0
        self.bird_color_index = 0
        self.apply_bird_color()
        self.recreate_sky()
        self.pipe_color_index = 0
        self.apply_pipe_color()
        self.ground_color_index = 0
        self.apply_ground_color()

    def reset_game_state(self):
        """Reset gameplay state but preserve user settings (sky, bird color, pipe color)."""
        # recreate gameplay objects
        self.bird = Bird()
        # ensure bird uses current color preset
        self.apply_bird_color()
        self.bird.update_scale()
        self.pipes = []
        self.time_since_pipe = 0.0
        self.score = 0
        self.state = "ready"
        self.ground = Ground()
        self.gameover_time = None

    def reset(self):
        # preserve settings, just reset gameplay
        self.reset_game_state()

    def start(self):
        if self.state == "ready":
            self.state = "playing"
            self.bird.flap()

    def update(self, dt):
        if self.state == "ready":
            self.bird.anim_t += dt
            return

        if self.state == "playing":
            self.bird.update(dt)
            self.ground.update(dt)

            self.time_since_pipe += dt
            if self.time_since_pipe >= PIPE_SPAWN_INTERVAL:
                self.time_since_pipe = 0.0
                spawn_x = WIDTH + 10
                self.pipes.append(PipePair(spawn_x))

            for p in list(self.pipes):
                p.update(dt)
                if p.offscreen():
                    self.pipes.remove(p)

            for p in self.pipes:
                if not p.passed and p.x + p.WIDTH < self.bird.x:
                    p.passed = True
                    self.score += 1

            for p in self.pipes:
                if p.collides(self.bird.rect):
                    self.game_over()
                    break

            # ground collision => game over; ceiling collision => just collide (stop upward motion)
            if self.bird.y + self.bird.radius >= HEIGHT - GROUND_H:
                self.game_over()
            elif self.bird.y - self.bird.radius <= 0:
                # clamp to top and cancel any upward velocity so bird 'bumps' into sky
                self.bird.y = self.bird.radius
                if self.bird.vy < 0:
                    self.bird.vy = 0

        elif self.state == "gameover":
            if self.bird.y + self.bird.radius < HEIGHT - GROUND_H:
                self.bird.update(dt)
            self.ground.update(dt)

    def game_over(self):
        if self.state != "gameover":
            self.state = "gameover"
            save_highscore(self.score)
            self.best = max(self.best, self.score)

    def flap(self):
        if self.state == "ready":
            self.start()
        elif self.state == "playing":
            self.bird.flap()
        elif self.state == "gameover":
            self.reset()

    def draw(self, surface):
        # draw background using cached sky surface (faster on large/fullscreen windows)
        if self.sky_surface is None:
            # fallback: generate directly if cache missing
            top_c, bottom_c = self.sky_presets[self.sky_index]
            draw_gradient(surface, top_c, bottom_c)
        else:
            surface.blit(self.sky_surface, (0, 0))

        for p in self.pipes:
            p.draw(surface)

        self.ground.draw(surface)
        self.bird.draw(surface)

        if self.state == "ready":
            title = font_big.render("FLAPPY BIRD", True, WHITE)
            tip1 = font_mid.render("Пробел / Клик — взмах", True, WHITE)
            tip2 = font_small.render("Нажмите, чтобы начать", True, WHITE)
            surface.blit(title, title.get_rect(center=(WIDTH//2, 120)))
            surface.blit(tip1, tip1.get_rect(center=(WIDTH//2, 180)))
            surface.blit(tip2, tip2.get_rect(center=(WIDTH//2, 210)))

        if self.state in ("playing", "gameover"):
            score_surf = font_big.render(str(self.score), True, WHITE)
            outline = font_big.render(str(self.score), True, BLACK)
            for dx, dy in ((-2,0),(2,0),(0,-2),(0,2)):
                surface.blit(outline, (WIDTH//2 - outline.get_width()//2 + dx, 30 + dy))
            surface.blit(score_surf, (WIDTH//2 - score_surf.get_width()//2, 30))

        if self.state == "gameover":
            box_w, box_h = 220, 140
            box = pygame.Surface((box_w, box_h), pygame.SRCALPHA)
            pygame.draw.rect(box, (0,0,0,180), (0,0,box_w,box_h), border_radius=12)
            text1 = font_mid.render("ИГРА ОКОНЧЕНА", True, WHITE)
            text2 = font_small.render(f"Счёт: {self.score}   Рекорд: {self.best}", True, WHITE)
            text3 = font_small.render("Пробел / Клик — заново", True, WHITE)
            box.blit(text1, text1.get_rect(center=(box_w//2, 36)))
            box.blit(text2, text2.get_rect(center=(box_w//2, 70)))
            box.blit(text3, text3.get_rect(center=(box_w//2, 102)))
            screen.blit(box, box.get_rect(center=(WIDTH//2, HEIGHT//2 - 20)))

        if self.settings_open:
            self.draw_settings(surface)

        # draw FPS in top-right corner as simple white text
        try:
            fps = int(clock.get_fps())
        except Exception:
            fps = 0
        fps_surf = font_small.render(f"FPS: {fps}", True, WHITE)
        fx = WIDTH - fps_surf.get_width() - 8
        fy = 8
        surface.blit(fps_surf, (fx, fy))

    def draw_settings(self, surface):
        w, h = 420, 260
        box = pygame.Surface((w,h), pygame.SRCALPHA)
        pygame.draw.rect(box, (0,0,0,200), (0,0,w,h), border_radius=10)
        title = font_mid.render("Настройки (Esc для выхода)", True, WHITE)
        box.blit(title, title.get_rect(center=(w//2, 24)))
        infos = [
            f"1-{len(self.sky_presets)}: фон (preset)",
            "B: сменить цвет птички (cycle)",
            "P: сменить цвет труб (cycle)",
            "G: сменить цвет земли (cycle)",
            "R: сброс настроек",
            "Q: закрыть настройки"
        ]
        # draw each info line with a semi-transparent backing rectangle to improve contrast
        for i, t in enumerate(infos):
            y = 56 + i*28
            txt = font_small.render(t, True, WHITE)
            tr = txt.get_rect(topleft=(16, y))
            # background for better readability
            pygame.draw.rect(box, (0,0,0,160), (tr.x-6, tr.y-4, tr.width+12, tr.height+8), border_radius=6)
            box.blit(txt, tr)
        # draw small swatches for current sky and bird colors
        # sky swatch (top/bottom)
        sky_top, sky_bottom = self.sky_presets[self.sky_index]
        pygame.draw.rect(box, sky_top, (260, 56, 48, 48))
        pygame.draw.rect(box, sky_bottom, (260, 110, 48, 48))
        # bird swatch
        body, wing = self.bird_color_presets[self.bird_color_index]
        pygame.draw.rect(box, body, (260, 168, 48, 28))
        pygame.draw.rect(box, wing, (260, 204, 48, 28))
        # pipe swatch (inner / outer)
        p_inner, p_outer = self.pipe_color_presets[self.pipe_color_index]
        pygame.draw.rect(box, p_inner, (174, 168, 56, 28))
        pygame.draw.rect(box, p_outer, (174, 204, 56, 28))
        # ground swatch
        g_top, g_dark = self.ground_color_presets[self.ground_color_index]
        pygame.draw.rect(box, g_top, (320, 168, 48, 28))
        pygame.draw.rect(box, g_dark, (320, 204, 48, 28))
        # draw FPS at bottom of settings
        try:
            fps = int(clock.get_fps())
        except Exception:
            fps = 0
        fps_txt = font_small.render(f"FPS: {fps}", True, WHITE)
        fr = fps_txt.get_rect(topleft=(16, h - 36))
        box.blit(fps_txt, fr)

        surface.blit(box, box.get_rect(center=(WIDTH//2, HEIGHT//2)))

# ----------------------------
# Main
# ----------------------------
def main():
    # open a resizable window so user can change size with mouse
    global screen, WIDTH, HEIGHT, GROUND_H, PIPE_GAP, PIPE_SPEED, BIRD_X, FLAP_IMPULSE, MAX_FALL_SPEED
    screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
    game = Game()
    running = True
    click_held = False

    while running:
        dt = clock.tick(FPS) / 1000.0

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = False
            elif e.type == pygame.VIDEORESIZE:
                # user resized window with mouse — update sizes and rescale some layout constants
                WIDTH, HEIGHT = e.w, e.h
                screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
                scale_w = WIDTH / 288.0
                scale_h = HEIGHT / 512.0
                # clamp scale to avoid extreme physics when window is tiny or huge
                scale_h = max(0.5, min(2.5, scale_h))
                scale_w = max(0.5, min(2.5, scale_w))
                GROUND_H = int(112 * scale_h)
                PIPE_GAP = int(100 * scale_h)
                PIPE_SPEED = int(120 * scale_h)
                BIRD_X = int(56 * scale_w)
                # scale physics so jumps feel consistent on taller/shorter windows
                # scale vertical impulses with vertical scale but clamp to reasonable bounds
                FLAP_IMPULSE = int(max(-700, min(-120, -280 * scale_h)))
                MAX_FALL_SPEED = int(max(160, min(1000, 400 * scale_h)))
                # apply new X to bird so it stays in the expected horizontal position
                game.bird.x = BIRD_X
                # update bird radius/visual scale
                game.bird.update_scale()
                # regenerate cached sky surface for new size
                game.recreate_sky()
            elif e.type == pygame.KEYDOWN:
                if e.key in (pygame.K_SPACE, pygame.K_UP, pygame.K_w):
                    game.flap()
                elif e.key == pygame.K_ESCAPE:
                    # toggle settings
                    game.settings_open = not game.settings_open
                else:
                    # settings key handling when open
                    if game.settings_open:
                        if e.key == pygame.K_1:
                            game.sky_index = 0
                            game.recreate_sky()
                        elif e.key == pygame.K_2:
                            game.sky_index = 1
                            game.recreate_sky()
                        elif e.key == pygame.K_3:
                            game.sky_index = 2
                            game.recreate_sky()
                        elif e.key == pygame.K_4:
                            # if user has more presets, allow 4
                            game.sky_index = 3
                            game.recreate_sky()
                        elif e.key == pygame.K_5:
                            game.sky_index = 4
                            game.recreate_sky()
                        elif e.key == pygame.K_6:
                            game.sky_index = 5
                            game.recreate_sky()
                        elif e.key == pygame.K_7:
                            game.sky_index = 6
                            game.recreate_sky()
                        elif e.key == pygame.K_p:
                            game.cycle_pipe_color()
                        elif e.key == pygame.K_b:
                            game.cycle_bird_color()
                        elif e.key == pygame.K_g:
                            game.cycle_ground_color()
                        elif e.key == pygame.K_r:
                            game.reset_settings()
                        elif e.key == pygame.K_q:
                            game.settings_open = False
            elif e.type == pygame.MOUSEBUTTONDOWN:
                if e.button == 1:
                    click_held = True
                    if not game.settings_open:
                        game.flap()
            elif e.type == pygame.MOUSEBUTTONUP:
                if e.button == 1:
                    click_held = False

        # pause updates when in settings
        if not game.settings_open:
            game.update(dt)
        game.draw(screen)
        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
