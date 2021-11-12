#!/usr/bin/env python3
from os import name, system

def clear():
    if name == 'nt':
        system('cls')
    else:
        system('clear')

number = int(input('Which number do you want to check? '))

if number % 2 == 0:
    print('This is an even number.')
else:
    print('This is an odd number.')
