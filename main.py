from turtle import Turtle, Screen

Tom = Turtle()
screen = Screen()


def move_forward():
    Tom.forward(10)


def move_backward():
    Tom.backward(10)


def move_left():
    new_heading = Tom.heading() + 10
    Tom.setheading(new_heading)


def move_right():
    new_heading = Tom.heading() - 10
    Tom.setheading(new_heading)


def clear():
    Tom.clear()
    Tom.penup
    Tom.home()
    Tom.pendown()


screen.listen()
screen.onkey(move_forward, "w")
screen.onkey(move_backward, "s")
screen.onkey(move_left, "a")
screen.onkey(move_right, "d")
screen.onkey(clear, "c")
screen.exitonclick()
