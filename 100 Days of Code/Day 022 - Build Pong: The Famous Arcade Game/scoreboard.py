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

    def __init__(self, score_pos):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.goto(score_pos)
        self.color('white')
        self.update_scoreboard()
        self.create_center()
        self.create_walls()

    def add_point(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f'Score: {self.score}', align=ALIGNMENT, font=FONT)

    def create_center(self):
        center_line = Turtle()
        center_line.penup()
        center_line.hideturtle()
        center_line.speed('fastest')
        center_line.color('white')
        center_line.goto(0, -300)
        center_line.setheading(90)
        for _ in range(30):
            center_line.pendown()
            center_line.forward(10)
            center_line.penup()
            center_line.forward(10)

    def create_walls(self):
        wall = Turtle()
        wall.penup()
        wall.hideturtle()
        wall.speed('fastest')
        wall.color('white')
        wall.goto(375, 300)
        wall.pendown()
        wall.goto(375, -300)
        wall.goto(-375, -300)
        wall.goto(-375, 300)
        wall.goto(375, 300)