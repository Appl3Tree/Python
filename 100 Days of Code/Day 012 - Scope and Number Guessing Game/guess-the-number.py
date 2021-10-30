#!/usr/bin/env python3
import random
import os

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

gameOver = False
while not gameOver:
    clear()
    print('Welcome to the Number Guessing Game!')
    print('I\'m thinking of a number between 1 and 100.')
    num = random.randint(1,100)
    difficulty = input('Choose a difficulty. Type \'easy\' or \'hard\': ')
    if difficulty == 'hard':
        attempts = 5
    else:
        attempts = 10
    while attempts > 0:
        print(f'You have {attempts} attempts remaining to guess the number.')
        guess = int(input('Make a guess: '))
        if guess != num:
            attempts -= 1
            if guess > num:
                print('Too high.')
            else:
                print('Too low.')
            print('Guess again.')
        else:
            print(f'You got it! The answer was {num}')
            break
    if attempts == 0:
        print('You\'ve run out of guesses, you lose. The number was {num}.')
    keepPlaying = input('\nWould you like to play again? Type \'y\' or \'n\': ')
    if keepPlaying == 'n':
        gameOver = True
