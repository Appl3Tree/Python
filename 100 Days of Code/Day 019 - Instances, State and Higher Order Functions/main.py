#!/usr/bin/env python3
from os import name, system
from turtle import Turtle, Screen  # resetscreen
import random


def clear():
    if name == 'nt':
        system('cls')
    else:
        system('clear')


# Task #1
# tim = Turtle()
# screen = Screen()
# def move_forwards():
#     tim.forward(10)
#
#
# def move_backwards():
#     tim.backward(10)
#
#
# def turn_left():
#     new_heading = tim.heading() + 10
#     tim.seth(new_heading)
#
#
# def turn_right():
#     new_heading = tim.heading() - 10
#     tim.seth(new_heading)
#
#
# screen.listen()
# screen.onkey(key='w', fun=move_forwards)
# screen.onkey(key='s', fun=move_backwards)
# screen.onkey(key='a', fun=turn_left)
# screen.onkey(key='d', fun=turn_right)
# screen.onkey(key='c', fun=resetscreen)


# Task #2
is_race_on = False
screen = Screen()
screen.screensize(canvwidth=500, canvheight=400)
screen.setup(width=550, height=450)
screen.canvwidth
tim = Turtle()
tim.hideturtle()
tim.penup()
tim.speed('fastest')
tim.setposition(x=230, y=-100)
tim.pendown()
tim.goto(x=230, y=100)
color = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape='turtle')
    new_turtle.color(color[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)


user_bet = ''
while user_bet.lower() not in color:
    user_bet = screen.textinput(title='Make your bet.', prompt='Which turtle will win the race? Enter a color: ')

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)
        if turtle.xcor() >= 213:
            is_race_on = False
            winning_color = turtle.fillcolor()
            if winning_color == user_bet.lower():
                print(f'You\'ve won! The {winning_color} turtle is the winner!')
            else:
                print(f'You\'ve lost! The {winning_color} turtle is the winner!')


screen.exitonclick()
