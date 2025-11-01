# Turtle 
# Turtle Graphics - бібліотека для малювання різної графіки за допомогою черепашок

#import turtle 

# # Створення екрану
# s = turtle.getscreen()
# #Створення черепашки
# t = turtle.Turtle()
# # Скриття черепашки
# t.hideturtle()
# # Завершення програми
# turtle.done()
# # рух черепахи
# t.forward(100) #рух вперед на 100 пікселів
# t.backward(100) #рух назад на 100 пікселів
# t.left(90) #поворот на 90 градусів
# t.right(90) #поворот на 90 градусів

# # Переміщення до точки
# t.goto(100, 100) # переміщення до точки (100, 100)
# t.home() # повернення до початкової точки
# Малювання квадрату
# import turtle

#t = turtle.Turtle()
# t.forward(100)
# t.right(90)
# t.forward(100)
# t.right(90)
# t.forward(100)
# t.right(90)
# t.forward(100)
# t.right(90)

# turtle.done()

# Керування пером (пензликом)

#t.penup() # підняти перо
# t.pendown() # опустити перо

# t.pensize(10) # змінити товщину пера
# t.pencolor("red") # змінити колір пера
# t.speed(5) # змінити швидкість черепахи 0 - найвища швидкість

# # готові фігури
# t.circle(50) # малює коло радіусом 50 пікселів
# t.dot(20) # точку з діаметром 20 пікселів
# t.speed(1)
# t.fillcolor("blue") # змінити колір заповнення
# t.begin_fill() # початок заповнення
# t.circle(50) # малює коло радіусом 50 пікселів
# t.end_fill() # кінець заповнення
# turtle.done()

# задача намалювати трикутник з заливкою зеленою

# import turtle

# t=turtle.Turtle()
# t.fillcolor("green")
# t.begin_fill()
# # малювання папємаше
# # for i in range(5):
# #     t.forward(100)
# #     t.left(90)
# # t.goto(100,100)
# # for i in range(5):
# #     t.forward(100)
# #     t.left(90)
# # t.goto(200,100)
# # for i in range(5):
# #     t.forward(100)
# #     t.left(90)
# # t.goto(300,200)
# # for i in range(5):
# #     t.forward(100)
# #     t.left(90)
# # t.end_fill()
# # малювання папємаше
# n=10
# while n<=50:
#     t.circle(n)
#     n+=10
# turtle.done()

# налаштування екрану 
# turtle.bgcolor("black") # колір фону
# turtle.title("Моя програма") # назва екрану

# t=turtle.Turtle()
# t.shape("turtle") # форма черепашки
# t.color ("red","green") # колір черепашки, колір заповнення
# t.shapesize(2,2,2) # розмір черепашки

# додаткові команди
# t.clear() # очищує екран
# t.reset() # скидує налаштування
# t.undo() # скасовує останню дію
# t.stamp() # залишає відбиток черепахи

# # отримання інформації
# t.position() # повертає поточну позицію
# t.heading() # повертає поточний напрямок
# t.isdown() # повертає чи піднятий перо # True or False

# Різнокольорві кола
# Намалюйте 5 кіл різних кольорів розташованих по колу

# import turtle 
# colors = ["red", "green", "blue", "yellow", "purple"]
# t=turtle.Turtle()
# t.shape("turtle")
# t.color("black", "white")
# t.shapesize(2,2,2)
# t.pensize(10)
# t.speed(3)
# for i in range(5):
#     t.pencolor(colors[i])
#     t.circle(30)
#     t.penup()
#     t.forward(70)
#     t.pendown()
#     t.right(72)
# turtle.done()
# import turtle

# t = turtle.Turtle()
# t.color ("gold")
# t.pensize(10)
# t.speed(1)
# for f in range(6):
#     t.forward(200)
#     t.right(144)
# turtle.done()

# import turtle

# t = turtle.Turtle()
# t.speed(8)
# screen = turtle.Screen()
# screen.bgcolor("white")
# screen.title("Смайлик")

# def move_to(x, y):
#     t.penup()
#     t.goto(x, y)
#     t.pendown()

# def draw_filled_circle(radius, color, fill_color):
#     t.color(color)
#     t.fillcolor(fill_color)
#     t.begin_fill()
#     t.circle(radius)
#     t.end_fill()

# move_to(0, -100)
# draw_filled_circle(100, "orange", "yellow")

# move_to(-40, 20)
# draw_filled_circle(15, "black", "black")

# move_to(40, 20)
# draw_filled_circle(15, "black", "black")

# move_to(0 , 0)

# move_to(0, 0)
# t.color("black")
# t.fillcolor("pink")
# t.begin_fill()
# t.setheading(270)  
# for i in range(3):
#     t.forward(20)
#     t.left(120)
# t.end_fill()

# # 5. Усмішка (дуга)
# move_to(-50, -20)
# t.color("red")
# t.pensize(5)
# t.setheading(-60)  # Початковий кут
# t.circle(60, 120)  # Дуга усмішки

# # 6. Рум'янець на щічках
# # Лівий рум'янець
# move_to(-70, 10)
# t.pensize(1)
# draw_filled_circle(12, "pink", "lightpink")

# # Правий рум'янець
# move_to(70, 10)
# draw_filled_circle(12, "pink", "lightpink")

# # 7. Брови 
# move_to(-50, 50)
# t.color("brown")
# t.pensize(4)
# t.setheading(30)
# t.forward(25)

# move_to(50, 50)
# t.setheading(150)
# t.forward(25)

# # Підпис
# move_to(-50, -150)
# t.color("black")
# t.pensize(1)
# t.write("Щасливий смайлик! ", font=("Arial", 14, "bold"))

# t.hideturtle()

# turtle.done()

# import turtle

# t = turtle.Turtle()
# t.forward(100)
# t.right(90)
# t.forward(100)
# t.right(90)
# t.forward(100)
# t.right(90)
# t.forward(100)
# t.right(90)

# for i in range(3):
#     t.forward(20)
#     t.left(120)

# t.circle(50)

# for i in range(8):
#     t.forward(20)
#     t.left(60)

# t.speed(1)
# for f in range(6):
#     t.forward(200)
#     t.right(144)
# turtle.done()

#         Домашка

import turtle

t = turtle.Turtle()
for i in range(6):
    t.forward(40)
    t.left(90)
    t.forward(30)
    t.right(90)
turtle.done()