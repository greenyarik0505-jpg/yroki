import turtle

t = turtle.Turtle()
t.speed(5)

t.pensize(5)
t.pencolor("blue")

for _ in range(4):
    t.forward(100)
    t.right(90)

t.penup()
t.goto(-150, 0)
t.pendown()

t.pensize(3)
t.pencolor("green")
for _ in range(3):
    t.forward(120)
    t.right(120)

t.penup()
t.goto(150, 0)
t.pendown()

t.pensize(2)
t.pencolor("red")

t.circle(60)

t.penup()
t.goto(0, -150)
t.pendown()

t.pensize(1)
t.pencolor("purple")

for а in range(50):
    t.forward(а * 2)
    t.right(90)

turtle.done()
