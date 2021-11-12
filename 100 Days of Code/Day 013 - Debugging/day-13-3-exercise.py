#!/usr/bin/env python3
from os import name, system

def clear():
    if name == 'nt':
        system('cls')
    else:
        system('clear')

for number in range(1, 101):
    if number % 3 == 0 or number % 5 == 0:
        print("FizzBuzz")
    if number % 3 == 0:
        print('Fizz')
    if number % 5 == 0:
        print('Buzz')
    else:
        print(number)
