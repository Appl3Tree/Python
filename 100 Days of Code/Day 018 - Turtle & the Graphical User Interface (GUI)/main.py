#!/usr/bin/env python3
from os import name, system
from turtle import Turtle, Screen, colormode
import random
# import colorgram


def clear():
    if name == 'nt':
        system('cls')
    else:
        system('clear')


clear()
tim = Turtle()
# Task #1
# timmy_the_turtle.hideturtle()
# timmy_the_turtle.color('black', 'dark green')

# Task #2
# for _ in range(15):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()

# Task #3
# def draw_shape(num_sides):
#     angle = 360 / sides
#     for _ in range(sides):
#         tim.right(angle)
#         tim.forward(100)
#
# colormode(255)
# for sides in range(3,11):
#     tim.color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
#     draw_shape(sides)


# Task #4
# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     randomized_color = (r, g, b)
#     return randomized_color
#
#
# def random_step():
#     tim.color(random_color())
#     # tim.width(random.randint(1,10))
#     tim.seth(random.randrange(0, 271, 90))
#     tim.forward(30)
#
#
# colormode(255)
# tim.width(10)
# tim.speed(10)
# for _ in range(200):
#     random_step()


# Task #5
# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     randomized_color = (r, g, b)
#     return randomized_color
#
#
# colormode(255)
# tim.speed('fastest')
#
#
# def draw_spirograph(size_of_gap):
#     for _ in range(int(360 / size_of_gap)):
#         tim.color(random_color())
#         tim.circle(100)
#         tim.setheading(tim.heading() + size_of_gap)
#
#
# draw_spirograph(2)


# Task #6
# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
tim.hideturtle()
tim.speed('fastest')
colormode(255)
tim.penup()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
color_list = [(22, 27, 46), (59, 93, 148), (116, 162, 206), (190, 225, 243), (74, 121, 199), (40, 24, 35),
              (36, 56, 112), (187, 143, 164), (215, 243, 239), (120, 78, 94), (237, 221, 199), (164, 184, 232),
              (135, 215, 232), (237, 206, 219), (191, 155, 138), (39, 24, 19), (190, 87, 109), (123, 87, 78),
              (230, 167, 185), (21, 31, 27), (106, 41, 55), (144, 174, 167), (86, 101, 95), (72, 147, 174),
              (147, 216, 209), (206, 86, 75), (232, 173, 163), (117, 40, 35), (215, 200, 152), (99, 144, 134)]
for _ in range(10):
    for _ in range(10):
        # Drop dot, move forward
        tim.dot(20, random.choice(color_list))
        tim.forward(50)
    # Move up and start over
    tim.seth(90)
    tim.forward(50)
    tim.seth(180)
    tim.forward(500)
    tim.seth(0)

screen = Screen()
screen.exitonclick()
