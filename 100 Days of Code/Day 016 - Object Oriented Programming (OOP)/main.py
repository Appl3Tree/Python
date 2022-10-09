#!/usr/bin/env python3
from os import name, system
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


def clear():
    if name == 'nt':
        system('cls')
    else:
        system('clear')


#def get_user_drink():
#    return input(f'What would you like? ({current_menu.get_items()}): ').lower()

# My program
#power = 'on'
#coffee_machine = CoffeeMaker()
#current_menu = Menu()
#cash_register = MoneyMachine()
#clear()
#while power == 'on':
#    choice = get_user_drink()
#    if choice == 'off':
#        exit()
#    elif choice == 'report':
#        coffee_machine.report()
#        cash_register.report()
#    else:
#        drink = current_menu.find_drink(choice)
#        if drink:
#            if coffee_machine.is_resource_sufficient(drink):
#                if cash_register.make_payment(drink.cost):
#                    coffee_machine.make_coffee(drink)

# Program re-written with guidance.
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

is_on = True

while is_on:
    options = menu.get_items()
    choice = input(f'What would you like? ({options}): ')
    if choice == 'off':
        is_on = False
    elif choice == 'report':
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
