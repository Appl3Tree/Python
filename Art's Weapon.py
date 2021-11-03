#!/usr/bin/env python3
from os import name, system
import random

def clear():
    if name == 'nt':
        system('cls')
    else:
        system('clear')

weapons = [
    'toothpick',
    'RPG',
    'ak47',
    'sword',
    'knife',
    'a child'
]

def getWeapon():
    roll = random.randint(0, 5)
    return weapons[roll]

print(f'Your weapon: {getWeapon()}')
# Flat damage 1-30
# Roll damage 1-10
# Skill: power, brawn, accuracy, hand-to-hand
# Skill bonus 1-6
# Damage class: Energy, physical, quantum
# Damage type: Piercing, slashing, concussive, impact
# Secondary damage type: corrosive if lucky.
   # If corrosive, 1-4.
# Range 1-10

















