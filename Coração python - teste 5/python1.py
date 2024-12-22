import turtle
import math

g = turtle.Turtle()
g.speed(0)
g.color("red")
turtle.bgcolor("black")

def corazon(n):
    x = 16 * math.sin(n) ** 3
    y = 13 * math.cos(n) - 5 * \
        math.cos(2*n) - 2*math.cos(3*n) - \
        math.cos(4*n)
    return x, y

g.penup()
for i in range(15):
    g.goto(0, 0)
    g.pendown()
    for n in range(0, 100, 2):
        x, y = corazon(n/10)
        g.goto(x*i, y*i)
    g.penup()

g.hideturtle()
turtle.done()