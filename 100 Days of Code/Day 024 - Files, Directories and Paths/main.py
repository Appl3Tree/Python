#!/usr/bin/env python3
# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
from os import name, system


def clear():
    if name == 'nt':
        system('cls')
    else:
        system('clear')


with open('Input/Letters/starting_letter.txt') as template:
    base_letter = template.read()

with open('Input/Names/invited_names.txt') as name_list:
    invitees = name_list.readlines()

for name in invitees:
    stripped_name = name.strip('\n')
    with open(f'Output/ReadyToSend/letter_for_{stripped_name}', 'w') as new_letter:
        temp_letter = base_letter.replace('[name]', stripped_name)
        new_letter.write(temp_letter)
