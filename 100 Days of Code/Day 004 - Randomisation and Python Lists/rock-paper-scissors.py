#!/usr/bin/env python3
import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choice = int(input('What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n'))
print(f'You chose {choice}:')
if choice == 0:
    print(rock)
elif choice == 1:
    print(paper)
else:
    print(scissors)

computerChoice = random.randint(0, 2)
print(f'The computer chose {computerChoice}:')
if computerChoice == 0:
    print(rock)
elif computerChoice == 1:
    print(paper)
else:
    print(scissors)

if choice == 0:
    if computerChoice == 0:
        print('It\'s a draw!')
    elif computerChoice == 1:
        print('You lose.')
    else:
        print('You win!')
elif choice == 1:
    if computerChoice == 0:
        print('You win!')
    elif computerChoice == 1:
        print('It\'s a draw!')
    else:
        print('You lose.')
else:
    if computerChoice == 0:
        print('You lose.')
    elif computerChoice == 1:
        print('You win!')
    else:
        print('It\'s a draw.')
