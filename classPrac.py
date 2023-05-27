import turtle
from turtle import Turtle, Screen
import random

timmy = Turtle()
timmy.shape("turtle")
# timmy.forward(100)
# timmy.right(90)

# for x in range(15):
#     timmy.forward(10)
#     timmy.penup()
#     timmy.forward(10)
#     timmy.pendown()

colors = ["cornflower blue", "red", "yellow", "green", "magenta", "blue", "deep pink", "lime", "orange", "blue violet"]

def draw_polygon():
    sides = 3
    color_index = 0
    while sides <= 10:
        timmy.color(colors[color_index])
        for x in range(sides):
            timmy.forward(100)
            timmy.right(360/sides)
        sides += 1
        color_index += 1


draw_polygon()

# def square():
#     for x in range(4):
#         timmy.forward(100)
#         timmy.right(90)

# def pentagon():
#     timmy.color("red")
#     for x in range(5):
#         timmy.forward(100)
#         timmy.right(72)

# def hexagon():
#     timmy.color("blue")
#     for x in range(6):
#         timmy.forward(100)
#         timmy.right(60)

# def heptagon():
#     timmy.color("green")
#     for x in range(7):
#         timmy.forward(100)
#         timmy.right(60)



my_screen = Screen()
my_screen.exitonclick()

# from prettytable import PrettyTable
# table = PrettyTable()

# table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
# table.add_column("Type", ["Electric", "Water", "Fire"])
# table.align = "l"

# print(table)