from turtle import Turtle, Screen
import random

tim = Turtle()

colours = ["deep sky blue", "navy", "chocolate",
           "dark olive green", "crimson", "dark magenta", "deep pink"]

directions = [0, 90, 180, 270]
tim.pensize(15)
tim.speed("fastest")

for _ in range(200):
    tim.color(random.choice(colours))
    tim.forward(30)
    tim.setheading(random.choice(directions))

screen = Screen()
screen.exitonclick()
