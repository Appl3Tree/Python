#!/usr/bin/env python3
import os


def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


lastProject = None
while True:
    days = os.listdir('100 Days of Code')
    choice = input('What do you wanna do?\n'
                   '1 - List Projects\n'
                   '2 - Run a project\n'
                   '3 - Just writing code (Dev Only)\n'
                   'r - Run last project again\n'
                   'x - Exit\n')
    clear()
    if choice == '1':
        inc = 0
        for day in os.listdir('100 Days of Code'):
            print(day)
            inc += 1
            if inc % 10 == 0:
                cont = input('List more? y/n\n')
                if cont == 'y' or cont == 'Y':
                    clear()
                    continue
                else:
                    break
    elif choice == '2':
        choice = int(input('Which day\'s project do you want to run? 1-100\n'))
        if type(choice) == int and choice <= len(days):
            path = "100 Days of Code/" + str(days[choice - 1]) + "/main.py"
            if os.path.exists(path):
                lastProject = choice
                os.system(f'python3 "{path}"')
            else:
                print(f'Day {choice} hasn\'t been completed yet.')
        elif choice > len(days):
            print(f'Day {choice} hasn\'t been started yet.')
        else:
            clear()
            quit()
    elif choice == '3':
        os.system('cp /home/runner/Python/pynew /opt/virtualenvs/python3/bin/pynew')
        os.system('chmod +x /opt/virtualenvs/python3/bin/pynew')
        os.system('cp /home/runner/Python/.vimrc /home/runner/.vimrc')
        clear()
        quit()
    elif choice in ['r', 'R']:
        if lastProject:
            path = "100 Days of Code/" + str(days[lastProject - 1]) + "/main.py"
            os.system(f'python3 "{path}"')
    elif choice in ['x', 'X']:
        quit()
    else:
        clear()
