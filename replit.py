#!/usr/bin/env python3
import os
RUN_PROGRAM = False
if RUN_PROGRAM:
    WRITING_CODE = False
else:
    WRITING_CODE = True

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

if WRITING_CODE:
    os.system('cp /home/runner/Python/pynew /opt/virtualenvs/python3/bin/pynew')
    os.system('chmod +x /opt/virtualenvs/python3/bin/pynew')
    os.system('cp /home/runner/Python/.vimrc /home/runner/.vimrc')

while RUN_PROGRAM:
    days = os.listdir('100 Days of Code')
    choice = input('What do you wanna do?\n1 - List Projects\n2 - Run a project\n')
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
            os.system(f'python3 "{path}"')
        elif choice > len(days):
            print(f'Day {choice} hasn\'t been completed yet.')
        else:
            clear()
            quit()
    else:
        clear()
        quit()
    print('\n')
