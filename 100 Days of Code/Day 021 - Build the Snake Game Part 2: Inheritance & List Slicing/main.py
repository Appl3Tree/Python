#!/usr/bin/env python3
from os import name, system
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time


def clear():
    if name == 'nt':
        system('cls')
    else:
        system('clear')


clear()
screen = Screen()
screen.setup(width=650, height=650)
screen.screensize(canvwidth=600, canvheight=600)
screen.bgcolor('black')
screen.title('My Snake Game')
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()
screen.listen()

screen.onkeypress(snake.right, 'Right')
screen.onkeypress(snake.right, 'd')
screen.onkeypress(snake.up, 'Up')
screen.onkeypress(snake.up, 'w')
screen.onkeypress(snake.left, 'Left')
screen.onkeypress(snake.left, 'a')
screen.onkeypress(snake.down, 'Down')
screen.onkeypress(snake.down, 's')

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food.
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.add_point()

    # Detect collision with wall.
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game_is_on = False
        scoreboard.game_over()

    # Detect collision with tail.
    for chunk in snake.body[1:]:
        if snake.head.distance(chunk) < 10:
            game_is_on = False
            scoreboard.game_over()


screen.exitonclick()
