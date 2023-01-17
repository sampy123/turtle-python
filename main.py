# import colorgram

# rgb_colors = []
# colors = colorgram.extract('colours.jpg', 30)

# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)


# print(rgb_colors)

import turtle as turtle_module
import random
turtle_module.colormode(255)
tim = turtle_module.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()
colors_list = [(220, 218, 211), (194, 176, 154), (224, 233, 225), (20, 43, 73), (205, 193, 161), (26, 115, 160), (141, 70, 58), (29, 127, 78), (16, 43, 29), (135, 159, 179), (206, 215, 223), (210, 136, 15), (219, 129, 161), (64, 39, 26), (204, 85, 125),
               (231, 216, 221), (19, 60, 117), (158, 77, 109), (118, 27, 21), (61, 41, 52), (145, 158, 150), (106, 122, 162), (131, 18, 22), (204, 186, 182), (204, 65, 60), (225, 169, 186), (56, 159, 101), (84, 61, 40), (34, 84, 46), (171, 206, 179)]


tim.setheading(225)
tim.forward(300)
tim.setheading(0)

number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(colors_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)


screen = turtle_module.Screen()
screen.exitonclick()
