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

# Task #1
# screen = Screen()
# screen.setup(width=650, height=650)
# screen.screensize(canvwidth=600, canvheight=600)
# screen.bgcolor('black')
# screen.title('My Snake Game')
# screen.tracer(0)
#
# snake = []
# # Initial snake body
# for i in range(3):
#     body_chunk = Turtle()
#     body_chunk.shape('square')
#     body_chunk.color('white')
#     body_chunk.penup()
#     body_chunk.setposition(x=(i * -20), y=0)
#     snake.append(body_chunk)
# screen.update()
# screen.listen()
#
# game_is_on = True
# while game_is_on:
#     screen.update()
#     time.sleep(0.1)
#     for chunk_num in range(len(snake) - 1, 0, -1):
#         new_x = snake[chunk_num - 1].xcor()
#         new_y = snake[chunk_num - 1].ycor()
#         snake[chunk_num].goto(new_x, new_y)
#     snake[0].forward(20)
#     screen.onkeypress(fun=go_east, key='d')
#     screen.onkeypress(fun=go_north, key='w')
#     screen.onkeypress(fun=go_west, key='a')
#     screen.onkeypress(fun=go_south, key='s')


# Task #2
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
