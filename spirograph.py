from turtle import Turtle, Screen
import random

timmy = Turtle()
timmy.shape("turtle")

timmy.pensize(2)
timmy.speed(10)

screen = timmy.getscreen()
screen.bgcolor("black")

colors = ["cornflower blue", "red", "yellow", "green", "magenta", "blue", "deep pink", "lime", "orange", "blue violet"]

for i in range(80):
    timmy.color(random.choice(colors))
    timmy.circle(100)
    timmy.left(5)

my_screen = Screen()
my_screen.exitonclick()