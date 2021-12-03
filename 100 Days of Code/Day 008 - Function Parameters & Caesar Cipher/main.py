#!/usr/bin/env python3
import art

#alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print(art.logo)

direction = input('Type \'encode\' to encrypt, type \'decode\' to decrypt:\n').lower()
if direction != 'encode' and direction != 'decode':
    quit()
text = input('Type your message:\n')
shift = int(input('Type the shift number:\n'))

def caesar(start_text, shift_amount, cipher_direction):
    end_text = ''
    ord_values = ''
    if cipher_direction == 'decode':
        shift_amount *= -1
    for letter in start_text:
        value = ord(letter)
        new_value = value + shift_amount
        end_text += chr(new_value)
        ord_values += str(new_value) + ' '
    print(f'The {direction}d text is "{end_text}".')
    print(f'The ord values of the {direction}d text is "{ord_values}".')

caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
