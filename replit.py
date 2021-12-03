#!/usr/bin/env python3
import os
import sys
RUN_PROGRAM = True
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
    # Line below moved 'cause replit doesn't like hard-coded paths past a homedir.
    #daysOfCode = os.listdir('/home/runner/Python/100 Days of Code/')
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
        if choice == 1:
            sys.path.append("100 Days of Code/" + days[choice - 1])
        elif choice == 2:
            sys.path.append("100 Days of Code/" + days[choice - 1])
        elif choice == 3:
            sys.path.append("100 Days of Code/" + days[choice - 1])
        elif choice == 4:
            sys.path.append("100 Days of Code/" + days[choice - 1])
        elif choice == 5:
            sys.path.append("100 Days of Code/" + days[choice - 1])
        elif choice == 6:
            sys.path.append("100 Days of Code/" + days[choice - 1])
        elif choice == 7:
            sys.path.append("100 Days of Code/" + days[choice - 1])
        elif choice == 8:
            sys.path.append("100 Days of Code/" + days[choice - 1])
        elif choice == 9:
            sys.path.append("100 Days of Code/" + days[choice - 1])
        elif choice == 10:
            sys.path.append("100 Days of Code/" + days[choice - 1])
        elif choice == 11:
            sys.path.append("100 Days of Code/" + days[choice - 1])
        elif choice == 12:
            sys.path.append("100 Days of Code/" + days[choice - 1])
        elif choice == 13:
            sys.path.append("100 Days of Code/" + days[choice - 1])
        elif choice == 14:
            sys.path.append("100 Days of Code/" + days[choice - 1])
        elif choice == 15:
            sys.path.append("100 Days of Code/" + days[choice - 1])
        else:
            clear()
            quit()
        import main
    else:
        clear()
        quit()
    print('\n')
