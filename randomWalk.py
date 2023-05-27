from turtle import Turtle, Screen
import random

timmy = Turtle()
timmy.shape("turtle")
timmy.pensize(10)

colors = ["cornflower blue", "red", "yellow", "green", "magenta", "blue", "deep pink", "lime", "orange", "blue violet"]
directions = [0, 90, 180, 270]


for i in range(50):
    timmy.color(random.choice(colors))
    timmy.setheading(random.choice(directions))
    timmy.forward(50)

my_screen = Screen()
my_screen.exitonclick()