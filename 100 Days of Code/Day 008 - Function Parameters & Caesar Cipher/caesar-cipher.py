#!/usr/bin/env python3

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
logo = '''

'''

direction = input('Type \'encode\' to encrypt, type \'decode\' to decrypt:\n').lower()
text = input('Type your message:\n').lower()
shift = int(input('Type the shift number:\n'))

def encrypt(plaintext, shift):
    ciphertext = ''
    for letter in plaintext:
        position = alphabet.index(letter)
<<<<<<< HEAD
        if position + shift > 25:
            position -= 26
=======
>>>>>>> origin/main
        new_position = position + shift
        new_letter = alphabet[new_position]
        ciphertext += new_letter
    print(f'The encoded text is: {ciphertext}')

def decrypt(ciphertext, shift):
    plaintext = ''
    for letter in ciphertext:
        position = alphabet.index(letter)
<<<<<<< HEAD
        if position - shift < 0:
            position += 26
=======
>>>>>>> origin/main
        new_position = position - shift
        new_letter = alphabet[new_position]
        plaintext += new_letter
    print(f'The decoded text is: {plaintext}')

if direction == 'encode':
    encrypt(text, shift)
elif direction == 'decode':
    decrypt(text, shift)
else:
    print(f'{text} is not \'encode\' or \'decode\'')
