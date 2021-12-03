#!/usr/bin/env python3
import os
from art import logo

### Calculator Functions

# Add
def add(n1, n2):
    return n1 + n2

# Subtract
def subtract(n1, n2):
    return n1 - n2

# Multiply
def multiply(n1, n2):
    return n1 * n2

# Divide
def divide(n1, n2):
    return n1 / n2

def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
}

def calculator():
    clear_screen()
    print(logo)

    num1 = float(input('What\'s the first number?: '))
    for operator in operations:
        print(operator)
    should_continue = True

    while should_continue:
        operation_symbol = input('Pick an operation: ')
        num2 = float(input('What\'s the next number?: '))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)

        print(f'{num1} {operation_symbol} {num2} = {answer}')
        choice = input(f'Type \'y\' to continue calculating with {answer}, or type \'n\' to start a new calculation\n')
        if choice == 'y':
            num1 = answer
        elif choice == 'quit':
            clear_screen()
            break
        else:
            should_continue = False
            calculator()

calculator()
