#!/usr/bin/env python3
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
        self.hideturtle()
        self.penup()
        self.goto(0, 300)
        self.color('white')
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f'Score: {self.score}', align=ALIGNMENT, font=FONT)

    def add_point(self):
        self.score += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write('GAME OVER', align='center', font=FONT)
