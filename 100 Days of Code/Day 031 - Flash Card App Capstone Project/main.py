#!/usr/bin/env python3
from os import name, system
from tkinter import *
from sys import argv


def clear():
    if name == 'nt':
        system('cls')
    else:
        system('clear')


clear()

# ---------- Constants ---------- #
BACKGROUND_COLOR = "#B1DDC6"

# ---------- UI Setup ---------- #
# Window Setup
window = Tk()
window.title('Flashy')
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Canvas Setup
canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
card_front_image = PhotoImage(file=f'{argv[0][:-7]}images/card_front.png')
canvas.create_image(400, 263, image=card_front_image)
canvas.create_text(400, 150, text='Title', font=('Ariel', 40, 'italic'))
canvas.create_text(400, 263, text='Word', font=('Ariel', 60, 'bold'))
canvas.grid(column=0, row=0, columnspan=3)

# Button(s) Setups
wrong_image = PhotoImage(file=f'{argv[0][:-7]}images/wrong.png')
wrong_button = Button(image=wrong_image, highlightbackground=BACKGROUND_COLOR)
right_image = PhotoImage(file=f'{argv[0][:-7]}images/right.png')
right_button = Button(image=right_image, highlightbackground=BACKGROUND_COLOR)
wrong_button.grid(column=0, row=1)
right_button.grid(column=2, row=1)

# Countdown Label Setup (personal addition)
countdown_label = Label(text='3', bg=BACKGROUND_COLOR, fg='#000000', font=('Ariel', 60))
countdown_label.grid(column=1, row=1)


# Leave at the end
window.mainloop()
