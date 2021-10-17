#!/usr/bin/env python3
import art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print(art.logo)

direction = input('Type \'encode\' to encrypt, type \'decode\' to decrypt:\n').lower()
text = input('Type your message:\n').lower()
shift = int(input('Type the shift number:\n'))

def caesar(start_text, shift_amount, cipher_direction):
    end_text = ''
    if cipher_direction == 'decode':
        shift_amount *= -1
    for letter in start_text:
        position = alphabet.index(letter)
        if position + shift_amount > 25 and cipher_direction == 'encode':
            position -= 26
        elif position - shift_amount < 0 and cipher_direction == 'decode':
            position += 26
        new_position = position + shift_amount
        end_text += alphabet[new_position]
    print(f'The {direction}d text is {end_text}.')

caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
