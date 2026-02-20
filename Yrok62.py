import pygame  # Підключаємо бібліотеку Pygame для створення ігор
import random  # Підключаємо генератор випадкових чисел
import sys  # Підключаємо системні функції для виходу з програми

WIDTH, HEIGHT = 900, 500  # Встановлюємо ширину та висоту вікна гри
FPS = 60  # Встановлюємо кількість кадрів на секунду (швидкість оновлення)

GROUND_Y = 380  # Координата Y для землі (рівень підлоги)
GRAVITY = 0.9  # Сила тяжіння, яка тягне гравця вниз 
JUMP_VELOCITY = -16  # Сила стрибка (швидкість вгору)

SCROLL_SPEED = 7  # Швидкість руху перешкод вліво
SPAWN_MIN = 60  # Мінімальний час до появи нової перешкоди
SPAWN_MAX = 120  # Максимальний час до появи нової перешкоди
SCROLL_SPEED = 7  # Базова швидкість

# === Чіт-меню стани ===
cheats = {
    "god_mode": False,
    "high_jump": False,
    "speed_hack": False
}
menu_open = False

pygame.init()  # Запускаємо (ініціалізуємо) Pygame

screen = pygame.display.set_mode((WIDTH, HEIGHT))  # Створюємо вікно гри заданого розміру
pygame.display.set_caption("GEOMETRY DASH V0.1")  # Встановлюємо заголовок вікна
clock = pygame.time.Clock()  # Створюємо годинник для контролю швидкості гри
font = pygame.font.SysFont("arial", 28)  # Налаштовуємо маленький шрифт для тексту
big_font = pygame.font.SysFont("arial", 56)  # Налаштовуємо великий шрифт для тексту


# Визначаємо кольори (червоний, зелений, синій)
WHITE = (240, 240, 240)  # Білий колір
BLACK = (15, 15, 15)  # Чорний колір
BLUE = (80, 160, 255)  # Блакитний колір
GREEN = (80, 220, 140)  # Зелений колір
RED = (255, 90, 90)  # Червоний колір
GRAY = (60, 60, 60)  # Сірий колір
YELLOW = (255, 220, 120)  # Жовтий колір


class Player:  # Створюємо клас Гравця (шаблон для нашого кубика)
    def __init__(self):  # Функція налаштування гравця при створенні
        self.size = 44  # Розмір кубика гравця
        self.rect = pygame.Rect(140, GROUND_Y - self.size, self.size, self.size)  # Створюємо квадрат гравця

        self.vel_y = 0  # Вертикальна швидкість (спочатку 0)
        self.on_ground = True  # Чи стоїть гравець на землі? (Так)
        self.rotation = 0  # Кут повороту кубика (для анімації)

    def jump(self):  # Функція стрибка
        if self.on_ground:  # Якщо гравець стоїть на землі
            if cheats["high_jump"]: 
                self.vel_y = JUMP_VELOCITY * 2
            else:
                self.vel_y = JUMP_VELOCITY
            self.on_ground = False  # Гравець більше не на землі
            
    def update(self):  # Функція оновлення стану гравця (рух, фізика)

        self.vel_y += GRAVITY  # Додаємо гравітацію до швидкості (тягне вниз)

        self.rect.y += int(self.vel_y)  # Змінюємо позицію гравця по вертикалі

        ground_top = GROUND_Y - self.size  # Вираховуємо верхню межу землі
        if self.rect.y >= ground_top:  # Якщо гравець впав нижче землі
            self.rect.y = ground_top  # Ставимо гравця на землю
            self.vel_y = 0  # Зупиняємо падіння
            self.on_ground = True  # Позначаємо, що гравець на землі

        if not self.on_ground:  # Якщо гравець у повітрі
            self.rotation = (self.rotation + 10) % 360  # Крутимо кубик
        else:  # Якщо гравець на землі
            self.rotation = 0  # Скидаємо поворот (рівно стоїть)

    def draw(self, surface):  # Функція малювання гравця на екрані

        cube_surf = pygame.Surface((self.size, self.size), pygame.SRCALPHA)  # Створюємо пусту поверхню для кубика
        cube_surf.fill(BLUE)  # Заливаємо її синім кольором

        pygame.draw.rect(cube_surf, (140, 210, 255), (6, 6, self.size - 12, self.size - 12), 3)  # Малюємо рамку

        rotated = pygame.transform.rotate(cube_surf, self.rotation)  # Повертаємо поверхню на кут обертання
        r_rect = rotated.get_rect(center=self.rect.center)  # Отримуємо новий квадрат після повороту

        surface.blit(rotated, r_rect.topleft)  # Малюємо повернутий кубик на екрані


class Obstacle:  # Створюємо клас Перешкоди (шип або блок)
    def __init__(self, kind):  # Налаштування перешкоди
        self.kind = kind  # Тип перешкоди: 'block' або 'spike'

        if self.kind == "block":  # Якщо це блок
            w, h = 50, 50  # Розміри блоку
        else:  # Якщо це шип
            w, h = 52, 42  # Розміри шипа

        x = WIDTH + 40  # Початкова позиція X (за межами екрану праворуч)
        y = GROUND_Y - h  # Позиція Y (на землі)
        self.rect = pygame.Rect(x, y, w, h)  # Створюємо квадрат перешкоди
        self.passed = False  # Чи пройшов гравець цю перешкоду?

    def update(self):  # Оновлення перешкоди
        if cheats["speed_hack"]: 
            current_speed = SCROLL_SPEED * 1.8
        else:
            current_speed = SCROLL_SPEED
        self.rect.x -= current_speed  # Рухаємо перешкоду вліво

    def offscreen(self):  # Перевірка, чи вийшла перешкода за екран
        return self.rect.right < 0  # Якщо правий край менше 0

    def draw(self, surface):  # Малювання перешкоди
        if self.kind == "block":  # Якщо це блок
            pygame.draw.rect(surface, GREEN, self.rect)  # Малюємо зелений квадрат
            pygame.draw.rect(surface, (30, 120, 70), self.rect, 4)  # Малюємо темну рамку
        else:  # Якщо це шип
            x, y, w, h = self.rect  # Беремо координати
            p1 = (x, y + h)  # Лівий нижній кут
            p2 = (x + w // 2, y)  # Верхній кут (вістря)
            p3 = (x + w, y + h)  # Правий нижній кут
            pygame.draw.polygon(surface, RED, [p1, p2, p3])  # Малюємо червоний трикутник
            pygame.draw.polygon(surface, (160, 40, 40), [p1, p2, p3], 4)  # Малюємо рамку трикутника

    def hitbox(self):  # Отримання зони зіткнення
        if self.kind == "spike":  # Якщо це шип
            shrink = 8  # Зменшуємо зону удару, щоб було чесно
            return self.rect.inflate(-shrink, -shrink)  # Повертаємо зменшений квадрат
        else:  # Якщо блок
            return self.rect  # Повертаємо звичайний квадрат

def reset_Game():  # Функція перезапуску гри
    player = Player()  # Створюємо нового гравця
    obstacles = []  # Очищуємо список перешкод
    score = 0  # Скидаємо рахунок
    alive = True  # Гравець живий
    frame_until_spawn = random.randint(SPAWN_MIN, SPAWN_MAX)  # Час до першої перешкоди
    return player, obstacles, score, alive, frame_until_spawn  # Повертаємо всі дані

# Початкове налаштування гри
player, obstacles, score, alive, frame_until_spawn = reset_Game()


while True:  # Головний цикл гри (працює постійно)
    clock.tick(FPS)  # Обмежуємо швидкість гри до 60 кадрів/сек

    if menu_open == True:
        SCROLL_SPEED = 0
    else:
        SCROLL_SPEED = 7

    for event in pygame.event.get():  # Перевіряємо події (натискання)
        if event.type == pygame.QUIT:  # Якщо натиснули хрестик вікна
            pygame.quit()  # Закриваємо Pygame
            sys.exit()  # Виходимо з програми
        if event.type == pygame.KEYDOWN:  # Якщо натиснули кнопку на клавіатурі
            if event.key in (pygame.K_SPACE, pygame.K_UP):  # Якщо це Пробіл або Стрілка Вгору
                if alive:  # Якщо гравець живий
                    player.jump()  # Стрибаємо
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_TAB:  # Клавіша для відкриття меню
                menu_open = not menu_open
            
            if menu_open:
                if event.key == pygame.K_1:
                    cheats["god_mode"] = not cheats["god_mode"]
                if event.key == pygame.K_2:
                    cheats["high_jump"] = not cheats["high_jump"]
                if event.key == pygame.K_3:
                    cheats["speed_hack"] = not cheats["speed_hack"]
        

    if alive:  # Якщо гравець живий, оновлюємо гру
        player.update()  # Оновлюємо гравця

        frame_until_spawn -= 1  # Зменшуємо лічильник до появи перешкоди
        if frame_until_spawn <= 0:  # Якщо час прийшов
            kind = random.choice(["block", "spike", "spike"])  # Вибираємо випадкову перешкоду
            obstacles.append(Obstacle(kind))  # Додаємо нову перешкоду в гру
            frame_until_spawn = random.randint(SPAWN_MIN, SPAWN_MAX)  # Задаємо час до наступної

        for obs in obstacles:  # Перебираємо всі активні перешкоди
            obs.update()  # Рухаємо перешкоду

            if not obs.passed and obs.rect.right < player.rect.left:  # Якщо перешкода позаду гравця
                obs.passed = True  # Позначаємо як пройдену
                score += 1  # Додаємо очко

            if player.rect.colliderect(obs.hitbox()):  # Якщо гравець врізався
                if cheats["god_mode"]:
                    pass
                else:
                    alive = False  # Гравець "помер"


        obstacles = [o for o in obstacles if not o.offscreen()]  # Видаляємо перешкоди, що вийшли за екран

        screen.fill(BLACK)  # Зафарбовуємо екран чорним (очищуємо)

        for x in range(0, WIDTH, 40):  # Малюємо вертикальні лінії сітки
            pygame.draw.line(screen, GRAY, (x, 0), (x, HEIGHT), 1)
        for y in range(0, HEIGHT, 40):  # Малюємо горизонтальні лінії сітки
            pygame.draw.line(screen, GRAY, (0, y), (WIDTH, y), 1)

        pygame.draw.rect(screen, GRAY, (0, GROUND_Y, WIDTH, HEIGHT - GROUND_Y))  # Малюємо підлогу
        pygame.draw.line(screen, (110, 110, 110), (0, GROUND_Y), (WIDTH, GROUND_Y), 4)  # Малюємо лінію підлоги


        for obs in obstacles:  # Малюємо всі перешкоди
            obs.draw(screen)
        player.draw(screen)  # Малюємо гравця

        score_text = font.render(f"Score: {score}", True, WHITE)  # Створюємо текст рахунку
        screen.blit(score_text, (20, 20))  # Малюємо рахунок на екрані

        if not alive:  # Якщо гравець програв
            overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)  # Створюємо прозорий шар
            overlay.fill((0, 0, 0, 180))  # Заливка напівпрозорим чорним
            screen.blit(overlay, (0, 0))  # Накладаємо на екран

            game_over_text = big_font.render("SUUUIIII", True, RED)  # Текст програшу
            retry_text = font.render("Press SPACE to retry", True, WHITE)  # Текст перезапуску

            # Центруємо текст на екрані
            screen.blit(game_over_text, (WIDTH // 2 - game_over_text.get_width() // 2, HEIGHT // 2 - 50))
            screen.blit(retry_text, (WIDTH // 2 - retry_text.get_width() // 2, HEIGHT // 2 + 20))

        # --- Малюємо Чіт-Меню ---
        if menu_open:
            menu_w, menu_h = 320, 200
            menu_x, menu_y = (WIDTH - menu_w) // 2, (HEIGHT - menu_h) // 2
            
            # Фонова плашка меню
            pygame.draw.rect(screen, (30, 30, 30), (menu_x, menu_y, menu_w, menu_h), 0, 15)
            pygame.draw.rect(screen, YELLOW, (menu_x, menu_y, menu_w, menu_h), 3, 15)
            
            title = font.render("--- CHEAT MENU ---", True, YELLOW)
            screen.blit(title, (menu_x + 50, menu_y + 10))
            
            # Відображення опцій
            c1_col = GREEN if cheats["god_mode"] else WHITE
            c2_col = GREEN if cheats["high_jump"] else WHITE
            c3_col = GREEN if cheats["speed_hack"] else WHITE
            
            txt1 = font.render(f"1. God Mode: {'[ON]' if cheats['god_mode'] else '[OFF]'}", True, c1_col)
            txt2 = font.render(f"2. High Jump: {'[ON]' if cheats['high_jump'] else '[OFF]'}", True, c2_col)
            txt3 = font.render(f"3. Speed Hack: {'[ON]' if cheats['speed_hack'] else '[OFF]'}", True, c3_col)
            
            screen.blit(txt1, (menu_x + 20, menu_y + 50))
            screen.blit(txt2, (menu_x + 20, menu_y + 90))
            screen.blit(txt3, (menu_x + 20, menu_y + 130))
            
            hint = font.render("Press TAB to close", True, GRAY)
            screen.blit(hint, (menu_x + 60, menu_y + 170))

        pygame.display.flip()  # Оновлюємо картинку на моніторі

        # Перевірка на перезапуск
        if not alive and pygame.key.get_pressed()[pygame.K_SPACE]:  # Якщо програв і натиснув Пробіл
            player, obstacles, score, alive, frame_until_spawn = reset_Game()  # Перезапускаємо гру

        pygame.display.flip()  # Ще раз оновлюємо екран
sys.exit() # Виходимо, якщо цикл зупинився
