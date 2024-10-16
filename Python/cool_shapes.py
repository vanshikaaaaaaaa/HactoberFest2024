import imp
from turtle import*

bgcolor('black')
speed(0)
hideturtle()

circle(5*5.2)
color('red')
done()

# -----------------ALTERNATIVE CODE--------

import turtle

# Setup screen
screen = turtle.Screen()
screen.bgcolor("white")

# Setup turtle
my_turtle = turtle.Turtle()
my_turtle.shape("turtle")
my_turtle.speed(5)

# Draw a cool spiral pattern
colors = ["red", "yellow", "blue", "green", "purple", "orange"]
for i in range(50):
    my_turtle.pencolor(colors[i % 6])
    my_turtle.forward(i * 10)
    my_turtle.right(144)  # This angle creates a star-like spiral

turtle.done()

# for i in range(1):
#     color('red')
#     circle(i)
#     color('orange')
#     circle(i*0.0)
#     right(3)
#     forward(3)
# done()
