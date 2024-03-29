from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape('turtle')
        self.left(90)
        self.goto(STARTING_POSITION)

    def go_up(self):
        self.forward(MOVE_DISTANCE)

    def go_to_next_level(self):
        if self.ycor() >= FINISH_LINE_Y:
            return True
        else:
            return False

    def next_level(self):
        self.goto(STARTING_POSITION)
