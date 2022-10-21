#!/usr/bin/env python3
from os import name, system


def clear():
    if name == 'nt':
        system('cls')
    else:
        system('clear')


clear()

def add(*args):
    total = 0
    for num in args:
        total += num
    return total

def calculate(n, **kwargs):
    print(kwargs)
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    n += kwargs['add']
    n *= kwargs['multiply']
    print(n)

class Car:
    def __init__(self, **kw):
        self.make = kw.get('make')
        self.model = kw.get('model')
        self.seats = kw.get('seats')
        self.color = kw.get('color')

my_car = Car(make = 'Nissan', color = 'Black', model = 'Altima', seats = 4)
print(my_car.make, my_car.model, my_car.seats, my_car.color)
calculate(2, add=3, multiply=5)