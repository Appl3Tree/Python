#!/usr/bin/env python3
from os import name, system
from turtle import Screen  # , Turtle
from snake import Snake
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
screen.listen()

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()
    screen.onkeypress(snake.right, 'Right')
    screen.onkeypress(snake.right, 'd')
    screen.onkeypress(snake.up, 'Up')
    screen.onkeypress(snake.up, 'w')
    screen.onkeypress(snake.left, 'Left')
    screen.onkeypress(snake.left, 'a')
    screen.onkeypress(snake.down, 'Down')
    screen.onkeypress(snake.down, 's')


screen.exitonclick()
