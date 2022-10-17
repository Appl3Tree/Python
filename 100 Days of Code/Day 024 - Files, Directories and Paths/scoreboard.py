#!/usr/bin/env python3
import turtle
from os import name, system
from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Courier', 24, 'normal')


def clear():
    if name == 'nt':
        system('cls')
    else:
        system('clear')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open(file='data.txt', mode='r') as data:
            self.high_score = int(data.read())
        self.hideturtle()
        self.penup()
        self.goto(0, 300)
        self.color('white')
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f'Score: {self.score} High Score: {self.high_score}', align=ALIGNMENT, font=FONT)

    def add_point(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open('data.txt', 'w') as data:
                data.write(f'{self.score}')
        self.score = 0
        self.update_scoreboard()
