# import pygame
# pygame.init()
# WIDTH = 600 # ширина екрану
# HEIGHT = 400 # довжина екрану 
# screen = pygame.display.set_mode((WIDTH,HEIGHT)) # поисвоюємо розміри екрану 
# pygame.display.set_caption("Моя перша гра на пайтоні ") # назва гри
# # кольори в форматі (RGB)
# WHITE = (255, 255, 255)
# BLACK = (0, 0, 0)
# RED = (255, 0, 0)
# GREEN = (0, 255, 0)
# BLUE = (0, 0, 255)
# PURPLE = (128,0,128)

# # Налаштування FPS ( кадри за секунду)
# FPS = 60 
# clock = pygame.time.Clock()

# running = True
# while running:
#     #Обробка подій
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running=False

#     screen.fill(WHITE) # очищувати екран 

#     # Тут ми малюємо 

#     # Оновлення екрану
#     pygame.display.update()

#     clock.tick(FPS) # Контроль фпс 
# pygame.quit()
# sys.exit()

# import pygame
# pygame.init()
# WIDTH = 800 # ширина екрану
# HEIGHT = 600 # довжина екрану 
# screen = pygame.display.set_mode((WIDTH,HEIGHT)) # поисвоюємо розміри екрану 
# pygame.display.set_caption("Моя перша гра на пайтоні ") # назва гри
# # кольори в форматі (RGB)
# WHITE = (255, 255, 255)
# BLACK = (0, 0, 0)
# RED = (255, 0, 0)
# GREEN = (0, 255, 0)
# BLUE = (0, 0, 255)
# PURPLE = (128,0,128)
# YELLOW = (255,255,0)

# # Налаштування FPS ( кадри за секунду)
# FPS = 60 
# clock = pygame.time.Clock()

# running = True
# while running:
#     #Обробка подій
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running=False

#     screen.fill(WHITE) # очищувати екран 

#     # Тут ми малюємо 
#     # 1. Зафарбований прямокутник
#     pygame.draw.rect(screen, RED, (50, 50, 100, 80))
    
#     # 2. Незафарбований прямокутник (з рамкою)
#     pygame.draw.rect(screen, BLUE, (200, 50, 100, 80), 3)
    
#     # 3. Коло
#     pygame.draw.circle(screen, GREEN, (400, 90), 40)
    
#     # 4. Лінія
#     pygame.draw.line(screen, BLACK, (50, 200), (350, 200), 2)
    
#     # 5. Згладжена лінія
#     pygame.draw.aaline(screen, PURPLE, (50, 230), (350, 230), 2)
    
#     # 6. Ламана лінія
#     points = [(50, 300), (100, 250), (150, 300), (200, 280)]
#     pygame.draw.lines(screen, RED, False, points, 3)
    
#     # 7. Полігон (багатокутник)
#     polygon_points = [(500, 200), (580, 250), (520, 320), (420, 280)]
#     pygame.draw.polygon(screen, YELLOW, polygon_points)
    
#     # 8. Еліпс
#     pygame.draw.ellipse(screen, BLUE, (450, 350, 150, 80), 2)
    
#     # 9. Дуга
#     import math
#     pygame.draw.arc(screen, GREEN, (600, 50, 150, 100), 0, math.pi, 4)
#     # Оновлення екрану
#     pygame.display.update()

#     clock.tick(FPS) # Контроль фпс 
# pygame.quit()
# sys.exit()

import pygame
import sys
import random
pygame.init()
WIDTH = 800 # ширина екрану
HEIGHT = 600 # довжина екрану 
screen = pygame.display.set_mode((WIDTH,HEIGHT)) # поисвоюємо розміри екрану 
pygame.display.set_caption("Моя перша гра на пайтоні ") # назва гри
# кольори в форматі (RGB)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PURPLE = (128,0,128)

#Початкові позиції 
x = WIDTH//2
y = HEIGHT//2
speed = 5  # 5 пікселів за кадр 5 П/к 
# Налаштування FPS ( кадри за секунду)
FPS = 60
clock = pygame.time.Clock()
xwall = random.randint(0,800)
ywall = random.randint(0,600)
xwall2 = random.randint(0,800)
ywall2 = random.randint(0,600)
xwall3 = random.randint(0,800)
ywall3 = random.randint(0,600)
running = True
while running:
    #Обробка подій
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
    #Керування клавіатурою 
    # Для керування клавіатурою ми підтягуємо функцію яка називається get_pressed()

    keys = pygame.key.get_pressed()
#Організація руху
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        x -= speed
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        x += speed
    if keys[pygame.K_UP] or keys[pygame.K_w]:
        y -= speed
    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        y += speed

    if x <0:
        x = 0
    if x > WIDTH-50:
        x = WIDTH - 50
    if y <0:
        y = 0
    if y > HEIGHT - 50:
        y = HEIGHT - 50
    screen.fill(WHITE) # очищувати екран 

# Логика поражения

    if x < xwall + 20 and x + 50 > xwall and y < ywall + 100 and y + 50 > ywall:
        running = False

    if x < xwall2 + 20 and x + 50 > xwall2 and y < ywall2 + 100 and y + 50 > ywall2:
        running = False

    if x < xwall3 + 20 and x + 50 > xwall3 and y < ywall3 + 100 and y + 50 > ywall3:
        running = False

    pygame.draw.rect(screen,BLUE,(x,y,50,50))
# 3 стіни 
    pygame.draw.rect(screen,RED,(xwall,ywall,20,100))
    pygame.draw.rect(screen,RED,(xwall2,ywall2,20,100))
    pygame.draw.rect(screen,RED,(xwall3,ywall3,20,100))

    # Оновлення екрану
    pygame.display.update()

    clock.tick(FPS) # Контроль фпс 
pygame.quit()
sys.exit()
