#!/usr/bin/env python3
from os import name, system
from turtle import Turtle
STARTING_POSITIONS = [(350, 0), (-350, 0)]


def clear():
    if name == 'nt':
        system('cls')
    else:
        system('clear')


class Paddle(Turtle):

    def __init__(self, start_position):
        super().__init__()
        self.color('white')
        self.shape('square')
        self.penup()
        self.turtlesize(stretch_wid=5, stretch_len=1)
        self.goto(start_position)

    def go_up(self):
        if self.ycor() < 240:
            new_y = self.ycor() + 20
            self.goto(self.xcor(), new_y)

    def go_down(self):
        if self.ycor() > -240:
            new_y = self.ycor() - 20
            self.goto(self.xcor(), new_y)

    def paddle_hit(self, ball):
        paddle_x = range(int(self.xcor() - 10), int(self.xcor() + 11))
        paddle_y = range(int(self.ycor() - 50), int(self.ycor() + 51))
        if self.xcor() < 0:
            if ball.xcor() - 10 in paddle_x and ball.ycor() in paddle_y:
                return True
            else:
                return False
        else:
            if ball.xcor() + 10 in paddle_x and ball.ycor() in paddle_y:
                return True
            else:
                return False
