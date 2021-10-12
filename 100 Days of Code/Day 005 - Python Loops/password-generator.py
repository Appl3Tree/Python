#!/usr/bin/env python3
#   Modules
import random

#   Variables
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '^', '(', ')', '*', '+']

#   Banner
print('''
*******************************************************************************
*                     Welcome to the PyPassword Generator                     *
*******************************************************************************
''')
nr_letters = int(input('How many letters would you like in your password?\n\t'))
nr_symbols = int(input('How many symbols would you like in your password?\n\t'))
nr_numbers = int(input('How many numbers would you like in your password?\n\t'))

#   Easy
easyPassword = ''
for l in range(nr_letters):
    easyPassword += random.choice(letters)
for s in range(nr_symbols):
    easyPassword += random.choice(symbols)
for n in range(nr_numbers):
    easyPassword += random.choice(numbers)
print(f'Here is your easy password: {easyPassword}')

#   Hard
hardPassword = list(easyPassword)
random.shuffle(hardPassword)
hardPassword = ''.join(hardPassword)
print(f'Here is your hard password: {hardPassword}')
