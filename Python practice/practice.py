from turtle import *
speed(200)
bgcolor('black')
hideturtle()
for i in range(200):
    color('red')
    circle(i)
    right(3)
    forward(0)
    color('orange')
    circle(i)
    right(3)
    forward(0)
    color('green')
    circle(i)
    right(3)
    forward(0)
done()
