#!/usr/bin/env python3
from os import name, system
from turtle import Screen
from paddle import Paddle
from scoreboard import Scoreboard
from ball import Ball
from random import randrange
import time


def clear():
    if name == 'nt':
        system('cls')
    else:
        system('clear')


screen = Screen()
screen.title('Pong')
screen.bgcolor('black')
screen.setup(width=850, height=650)
screen.screensize(canvwidth=800, canvheight=600)
screen.listen()
screen.tracer(0)

r_paddle = Paddle(start_position=(350, 0))
r_score = Scoreboard(score_pos=(200, 300))

l_paddle = Paddle(start_position=(-350, 0))
l_score = Scoreboard(score_pos=(-200, 300))

ball = Ball()

screen.onkey(r_paddle.go_up, 'Up')
screen.onkey(r_paddle.go_down, 'Down')
screen.onkey(l_paddle.go_up, 'w')
screen.onkey(l_paddle.go_down, 's')

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # If ball gets past the paddle, then add score to player's side.
    if ball.xcor() > r_paddle.xcor():
        l_score.add_point()
        ball.reset_position()
        ball.y_move = randrange(5, 25, 5)
        ball.reflect()
    else:
        # If ball hits paddle, then bounce away.
        if r_paddle.paddle_hit(ball):
            ball.reflect(r_paddle)

    if ball.xcor() < l_paddle.xcor():
        r_score.add_point()
        ball.goto(0, 0)
        ball.y_move = randrange(5, 25, 5)
        ball.reflect()
    else:
        if l_paddle.paddle_hit(ball):
            ball.reflect(l_paddle)

    # If ball collides with walls, then allow it to bounce.
    if ball.ycor() >= 270 or ball.ycor() <= -270:
        ball.bounce()


screen.exitonclick()
