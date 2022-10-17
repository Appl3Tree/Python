#!/usr/bin/env python3
#!/usr/bin/env python3
from os import name, system
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time


def clear():
    if name == 'nt':
        system('cls')
    else:
        system('clear')


# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
# with open('Input/Letters/starting_letter.txt') as template:
#     base_letter = template.read()
#
# with open('Input/Names/invited_names.txt') as name_list:
#     invitees = name_list.readlines()
#
# for name in invitees:
#     stripped_name = name.strip('\n')
#     with open(f'Output/ReadyToSend/letter_for_{stripped_name}', 'w') as new_letter:
#         temp_letter = base_letter.replace('[name]', stripped_name)
#         new_letter.write(temp_letter)


clear()
screen = Screen()
screen.setup(width=650, height=650)
screen.screensize(canvwidth=600, canvheight=600)
screen.bgcolor('black')
screen.title('My Snake Game')
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()
screen.listen()

screen.onkeypress(snake.right, 'Right')
screen.onkeypress(snake.right, 'd')
screen.onkeypress(snake.up, 'Up')
screen.onkeypress(snake.up, 'w')
screen.onkeypress(snake.left, 'Left')
screen.onkeypress(snake.left, 'a')
screen.onkeypress(snake.down, 'Down')
screen.onkeypress(snake.down, 's')

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food.
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.add_point()

    # Detect collision with wall.
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        scoreboard.reset()
        snake.reset()

    # Detect collision with tail.
    for chunk in snake.body[1:]:
        if snake.head.distance(chunk) < 10:
            scoreboard.reset()
            snake.reset()


screen.exitonclick()
