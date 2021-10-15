#!/usr/bin/env python3
import random
import os
import sys
word_list = []
with open('100 Days of Code/Day 007 - Hangman/word_list', 'r') as f:
    word_list = f.read().splitlines()

stages = ['''
 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========
''', '''
 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========
''', '''
 +---+
 |   |
 O   |
/|\  |
     |
     |
=========
''', '''
 +---+
 |   |
 O   |
/|   |
     |
     |
=========
''', '''
 +---+
 |   |
 O   |
 |   |
     |
     |
=========
''', '''
 +---+
 |   |
 O   |
     |
     |
     |
=========
''', '''
 +---+
 |   |
     |
     |
     |
     |
=========
''']
#word_list = ['ardvark', 'baboon', 'camel']
chosen_word = random.choice(word_list)
if os.name == 'nt':
    os.system('cls')
else:
    os.system('clear')
logo = '''
  _
 | |
 | |__   __ _ _ __   __ _ _ __ ___   __ _ _ __
 | '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \\
 | | | | (_| | | | | (_| | | | | | | (_| | | | |
 |_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                     __/ |
                    |___/
'''
print(logo)
display = []
word_length = len(chosen_word)

# Set display to all _'s
for letter in chosen_word:
    display.append('_')

endOfGame = False
lives = 6
guessedLetters = []
while not endOfGame:
    # Get guess and replace _ with guess if it exists.
    guess = input('Guess a letter: ').lower()
    if guess in guessedLetters:
        print('You\'ve already guessed that letter.')
    else:
        for position in range(word_length):
            letter = chosen_word[position]
            if letter == guess:
                display[position] = letter
        if guess not in chosen_word:
            lives -= 1
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')
        print(logo)
        print(stages[lives])
        guessedLetters += guess
        print(f"Currently guessed characters: {' '.join(guessedLetters)}")
        print(f'Incorrect guesses left: {lives}')
        print(f"{' '.join(display)}")
        if '_' not in display:
            endOfGame = True
            print('\nYou win!')
        if lives == 0:
            endOfGame = True
            print('\nYou lose.')
            print(f'The correct answer was {chosen_word}.')
