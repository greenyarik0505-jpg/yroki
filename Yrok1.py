import turtle
turtle.bgcolor("black")
t = turtle.Turtle()
t.speed(0) 
t.width(8)

colors = ["red", "orange", "yellow", "white", "cyan", "green"]

for i in range(500):
    t.pencolor(colors[i % len(colors)])  
    t.forward(i * 3)
    t.right(121)  
turtle.done()