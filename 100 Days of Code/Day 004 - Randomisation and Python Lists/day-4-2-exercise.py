#!/usr/bin/env python3
import random

names_string = input('Give me everybody\'s names, separated by a comma.\n\t')
names = names_string.split(', ')

print(f'{names[random.randint(0, len(names) - 1)]} is going to buy the meal today!')
