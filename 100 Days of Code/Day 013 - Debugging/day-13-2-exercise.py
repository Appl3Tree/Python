#!/usr/bin/env python3
from os import name, system

def clear():
    if name == 'nt':
        system('cls')
    else:
        system('clear')

year = int(input('Which year do you want to check? '))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print('Leap year.')
        else:
            print('Not leap year.')
    else:
        print('Leap year.')
else:
    print('Not leap year.')
