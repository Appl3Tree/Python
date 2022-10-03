#!/usr/bin/env python3
from os import name, system

def clear():
    if name == 'nt':
        system('cls')
    else:
        system('clear')

MENU = {
    'espresso': {
        'ingredients': {
            'water': 50,
            'coffee': 18,
        },
        'cost': 1.5,
    },
    'latte': {
        'ingredients': {
            'water': 200,
            'milk': 150,
            'coffee': 24,
        },
        'cost': 2.5,
    },
    'cappuccino': {
        'ingredients': {
            'water': 250,
            'milk': 100,
            'coffee': 24,
        },
        'cost': 3.0,
    }
}

resources = {
    'water': 300,
    'milk': 200,
    'coffee': 100,
    'money': 0,
}

# TODO 1: Prompt user by asking "What would you like? (espresso/latte/cappuccino): "
def getUserDrink():
    return input('What would you like? (espresso/latte/cappuccino): ').lower()


def displayReport(machineResources):
    currentWater = machineResources['water']
    currentMilk = machineResources['milk']
    currentCoffee = machineResources['coffee']
    currentMoney = "{:.2f}".format(machineResources['money'])
    currentResources = f'''
    Water: {currentWater}ml
    Milk: {currentMilk}ml
    Coffee: {currentCoffee}g
    Money: ${currentMoney}
    '''
    print(currentResources)


def resourcesAvailable(drink):
    if MENU[drink]['ingredients']['water'] > resources['water']:
        print('Sorry, there is not enough water.')
        return 0
    elif 'milk' in MENU[drink]['ingredients'] and (MENU[drink]['ingredients']['milk'] > resources['milk']):
        print('Sorry, there is not enough milk.')
        return 0
    elif MENU[drink]['ingredients']['coffee'] > resources['coffee']:
        print('Sorry, there is not enough coffee.')
        return 0
    else:
        return 1

def processCoins(quarters, dimes, nickles, pennies):
    total = quarters * 0.25
    total += dimes * 0.10
    total += nickles * 0.05
    total += pennies * 0.01
    return total

def showMenu():
    print('''
    **********************
    *        MENU        *
    *____________________*
    * Espresso   - $1.50 *
    * Latte      - $2.50 *
    * Cappuccino - $3.00 *
    **********************
    ''')

coffeeMachine = 'on'


clear()
while coffeeMachine == 'on':
    choice = getUserDrink()
    if choice == 'off':
        exit()
    elif choice == 'report':
        displayReport(resources)
    elif choice == 'menu':
        showMenu()
    elif choice != 'espresso' and choice != 'latte' and choice != 'cappuccino':
        print(f'{choice} is not a valid option.')
    elif resourcesAvailable(choice):
        print('Please insert coins.')
        numQuarters = int(input('How many quarters?: '))
        numDimes = int(input('How many dimes?: '))
        numNickles = int(input('How many nickels?: '))
        numPennies = int(input('How many pennies?: '))
        payment = processCoins(numQuarters, numDimes, numNickles, numPennies)

        if payment and (payment < MENU[choice]['cost']):
            print('Sorry, that\'s not enough money. Money refunded.\n')
        else:
            if payment > MENU[choice]['cost']:
                refund = "{:.2f}".format(payment - MENU[choice]['cost'])
                print(f'Here is ${refund} in change.')
            print(f'Here is your latte ☕️ Enjoy!\n')
            resources['water'] -= MENU[choice]['ingredients']['water']
            if 'milk' in MENU[choice]['ingredients']:
                resources['milk'] -= MENU[choice]['ingredients']['milk']
            resources['coffee'] -= MENU[choice]['ingredients']['coffee']
            resources['money'] += MENU[choice]['cost']
clear()