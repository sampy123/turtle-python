from turtle import Turtle, Screen
import random

tim = Turtle()

num_sides = 5

colours = ["deep sky blue", "navy", "chocolate",
           "dark olive green", "crimson", "dark magenta", "deep pink"]


def draw_shape(num_sides):
    for _ in range(num_sides):
        angle = 360 / num_sides
        tim.forward(100)
        tim.right(angle)


for shape_side_n in range(3, 11):
    tim.color(random.choice(colours))
    draw_shape(shape_side_n)

screen = Screen()
screen.exitonclick()
