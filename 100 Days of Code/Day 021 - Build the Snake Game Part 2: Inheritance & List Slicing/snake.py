#!/usr/bin/env python3
from os import name, system
from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270


def clear():
    if name == 'nt':
        system('cls')
    else:
        system('clear')


class Snake:

    def __init__(self):
        self.body = []
        self.create_snake()
        self.head = self.body[0]
        self.head.shape('arrow')
        self.create_walls()

    def create_walls(self):
        wall = Turtle()
        wall.penup()
        wall.hideturtle()
        wall.speed('fastest')
        wall.color('white')
        wall.goto(290, 290)
        wall.pendown()
        wall.goto(290, -290)
        wall.goto(-290, -290)
        wall.goto(-290, 290)
        wall.goto(290, 290)

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        body_part = Turtle()
        body_part.shape('square')
        body_part.color('white')
        body_part.penup()
        body_part.setposition(position)
        self.body.append(body_part)

    def extend(self):
        self.add_segment(self.body[-1].position())

    def move(self):
        for chunk_num in range(len(self.body) - 1, 0, -1):
            new_x = self.body[chunk_num - 1].xcor()
            new_y = self.body[chunk_num - 1].ycor()
            self.body[chunk_num].goto(new_x, new_y)
        self.head.forward(20)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def reset(self):
        for chunk in self.body:
            chunk.goto(1000, 1000)
        self.body.clear()
        self.create_snake()
        self.head = self.body[0]
        self.head.shape('arrow')
