#!/usr/bin/env python3
import os

def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

os.system('cp /home/runner/Python/pynew /opt/virtualenvs/python3/bin/pynew')
os.system('cp /home/runner/Python/.vimrc /home/runner/.vimrc')
#print('The command \'pynew\' is now available for use.\n')
runProgram = False
while runProgram == True:
    daysOfCode = os.listdir('/home/runner/Python/100 Days of Code/')
    choice = int(input('What do you wanna do?\n1 - List Projects\n2 - Run a project\n'))
    clear_screen()
    if choice == 1:
        inc = 0
        for day in daysOfCode:
            print(day)
            inc += 1
            if inc % 10 == 0:
                cont = input('List more? y/n\n')
                if cont == 'y' or cont == 'Y':
                    clear_screen()
                    continue
                else:
                    break
    elif choice == 2:
        choice = int(input('Which day\'s project do you want to run? 1-100\n'))
        if choice == 1:
            os.system('"100 Days of Code/Day 001 - Variables to Manage Data/band-name-generator.py"')
        elif choice == 2:
            os.system('"100 Days of Code/Day 002 - Data Types and How to Manipulate Strings/tip-calculator.py"')
        elif choice == 3:
            os.system('"100 Days of Code/Day 003 - Control Flow and Logical Operators/treasure-island.py"')
        elif choice == 4:
            os.system('"100 Days of Code/Day 004 - Randomisation and Python Lists/rock-paper-scissors.py"')
        elif choice == 5:
            os.system('"100 Days of Code/Day 005 - Python Loops/password-generator.py"')
        elif choice == 6:
            os.system('cat "100 Days of Code/Day 006 - Python Functions & Karel/readme.md"')
        elif choice == 7:
            os.system('"100 Days of Code/Day 007 - Hangman/hangman.py"')
        elif choice == 8:
            os.system('"100 Days of Code/Day 008 - Function Parameters & Caesar Cipher/caesar-cipher.py"')
        elif choice == 9:
            os.system('"100 Days of Code/Day 009 - Dictionaries, Nesting and the Secret Auction/blind-auction.py"')
        elif choice == 10:
            os.system('"100 Days of Code/Day 010 - Functions with Outputs/calculator.py"')
        elif choice == 11:
            os.system('"100 Days of Code/Day 011 - Blackjack Capstone Project/blackjack.py"')
        else:
            clear_screen()
            quit()
    else:
        clear_screen()
        quit()
    print('\n')
    
