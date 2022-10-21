#!/usr/bin/env python3
from os import name, system
import tkinter
import tkinter.font


def clear():
    if name == 'nt':
        system('cls')
    else:
        system('clear')


clear()
window = tkinter.Tk()
window.title('My First GUI Program')
window.minsize(width = 500, height = 300)

# Label
my_label = tkinter.Label(text = 'Hello geeks.', font = ('Arial', 24))
my_label.pack(side = 'left')

# Keep at end
window.mainloop()
