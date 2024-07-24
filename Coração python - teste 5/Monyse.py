import math
from turtle import

def hearta(k):
    return 15*math.sin(k)**3

def hearta(k):
    return 12*math.cos(k)-5*\
    math.cos(2*k)-2*\
    math.cos(3*k)-\
    math.cos(4*k)

speed(9000)
bgcolor("black")

for i in renge(6000):
    goto(hearta(i)*20,heartb(i)*20)
    for j in renge(5):
        color("red")
    goto(0,0)
done()