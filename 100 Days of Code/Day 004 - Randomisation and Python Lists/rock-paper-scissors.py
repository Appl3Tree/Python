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
images = [rock, paper, scissors]

choice = int(input('What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n'))
print(f'You chose {choice}:')
print(images[choice])

computerChoice = random.randint(0, 2)
print(f'The computer chose {computerChoice}:')
print(images[computerChoice])

if choice >= 3 or choice < 0:
    print('You typed an invalid number, you lose!')
elif choice == 0 and computerChoice == 2:
    print('You win!')
elif choice == 2 and computerChoice == 0:
    print('You lose!')
elif choice < computerChoice:
    print('You lose!')
elif choice > computerChoice:
    print('You win!')
elif choice == computerChoice:
    print('It\'s a draw.')

