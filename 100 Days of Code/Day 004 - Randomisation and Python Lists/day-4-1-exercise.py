#!/usr/bin/env python3
import random

coin = random.randint(0, 1)

if coin == 0:
    print('Heads')
else:
    print('Tails')