#!/usr/bin/env python3
from os import name, system
from art import logo, vs
from game_data import data
from random import choice

def clear():
    if name == 'nt':
        system('cls')
    else:
        system('clear')

def format_data(account):
    return f'{account["name"]}, a {account["description"]}, from {account["country"]}.'

def check_answer(guess, aFollowers, bFollowers):
    if aFollowers > bFollowers:
        winner = 'a'
    else:
        winner = 'b'
    return winner == guess
# Clear the screen and show the art.

def playGame():
    clear()
    print(logo)
    score = 0

    gameOver = False
    while not gameOver:
# Grab the first random data set.
        dataA = choice(data)
        print(f'Compare A: {format_data(dataA)}')

# Display the vs. art.
        print(vs)

# Grab the second set, making sure it's different from the first.
        dataB = choice(data)
        while dataA['name'] == dataB['name']:
            dataB = choice(data)
        print(f'Against B: {format_data(dataB)}')

# Who has more followers? A or B?
        moreFollowersGuess = input('Who has more followers? Type \'A\' or \'B\': ').lower()

# If correct, show current score and repeat game.
        if check_answer(moreFollowersGuess, dataA["follower_count"], dataB["follower_count"]):
            score += 1
            clear()
            print(logo)
            print(f'You\'re right! Current score: {score}')
        else:
            clear()
            print(logo)
            print(f'Sorry, that\'s wrong. Final score: {score}')
            gameOver = True

    keepPlaying = input('Type \'y\' to play again. ')
    if keepPlaying == 'y' or keepPlaying == 'Y':
        playGame()

playGame()
