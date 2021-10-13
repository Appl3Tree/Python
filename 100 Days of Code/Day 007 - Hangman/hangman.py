#!/usr/bin/env python3
import random
import os

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
word_list = ['ardvark', 'baboon', 'camel']
chosen_word = random.choice(word_list)
if os.name == 'nt':
    os.system('cls')
else:
    os.system('clear')
print('''
  _
 | |
 | |__   __ _ _ __   __ _ _ __ ___   __ _ _ __
 | '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \\
 | | | | (_| | | | | (_| | | | | | | (_| | | | |
 |_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                     __/ |
                    |___/
''')

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
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
    letterInGuess = False
    alreadyGuessed = False
    for position in range(word_length):
        letter= display[position]
        if letter == guess:
            alreadyGuessed = True
    if alreadyGuessed:
        print('You must choose a different letter.')
    else:
        for position in range(word_length):
            letter = chosen_word[position]
            if letter == guess:
                display[position] = letter
                letterInGuess = True
        if letterInGuess == False:
            lives -= 1
        print(stages[lives])
        guessedLetters += guess
        print(f"Currently guessed characters: {' '.join(guessedLetters)}")
        print(f'Incorrect guesses left: {lives}')
        print(f"{' '.join(display)}")
        if '_' not in display:
            endOfGame = True
            print('You win!')
        if lives == 0:
            endOfGame = True
            print('You lose.')
