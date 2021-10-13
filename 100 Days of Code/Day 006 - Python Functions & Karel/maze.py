#!/usr/bin/env python3

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def turn_around():
    turn_left()
    turn_left()

def left_is_clear():
    turn_left()
    if front_is_clear():
        turn_right()
        return True
    else:
        turn_right()
        return False

def escape():
    if right_is_clear():
    turn_right()
    move()
    elif front_is_clear():
    move()
    elif left_is_clear():
    turn_left()
    move()
    else:
    turn_around()
    move()

while front_is_clear():
    move()
while not at_goal():
    escape()
