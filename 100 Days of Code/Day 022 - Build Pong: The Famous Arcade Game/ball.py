#!/usr/bin/env python3
from os import name, system
from turtle import Turtle
from random import randrange


def clear():
    if name == 'nt':
        system('cls')
    else:
        system('clear')


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()
        self.x_move = 10
        self.y_move = randrange(5, 25, 5)
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce(self):
        self.y_move *= -1

    def reflect(self, paddle=None):
        if paddle:
            y_diff = self.ycor() - paddle.ycor()
            if -45 <= y_diff < -30:
                self.y_move = -20
            elif -30 < y_diff < -10:
                self.y_move = -15
            elif -10 < y_diff < 10:
                if self.y_move < 0:
                    self.y_move = -10
                else:
                    self.y_move = 10
            elif 10 < y_diff < 30:
                self.y_move = 15
            elif 30 < y_diff <= 45:
                self.y_move = 20
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = 0.1
