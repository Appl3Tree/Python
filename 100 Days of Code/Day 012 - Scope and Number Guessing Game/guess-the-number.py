#!/usr/bin/env python3
from random import randint
from os import name, system
from art import logo

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def clear():
    if name == 'nt':
        system('cls')
    else:
        system('clear')

def check_answer(guess, answer, turns):
    '''Checks answer against guess. Returns the number of attempts remaining.'''
    if guess > answer:
        print('Too high.')
        return turns - 1
    elif guess < answer:
        print('Too low.')
        return turns - 1
    else:
        print(f'You got it! The answer was {answer}.')

def set_difficulty():
    level = input('Choose a difficulty. Type \'easy\' or \'hard\': ')
    if level == 'hard':
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS


def game():
    clear()
    print(logo)
    print('Welcome to the Number Guessing Game!')
    print('I\'m thinking of a number between 1 and 100.')
    answer = randint(1,100)

    attempts = set_difficulty()

    guess = 0
    while guess != answer:
        print(f'You have {attempts} attempts remaining to guess the number.')
        guess = int(input('Make a guess: '))
        attempts = check_answer(guess, answer, attempts)
        if attempts == 0:
            print('You\'ve run out of guesses, you lose. The number was {num}.')
            break
    keepPlaying = input('\nWould you like to play again? Type \'y\' or \'n\': ')
    if keepPlaying == 'y':
        game()

game()
