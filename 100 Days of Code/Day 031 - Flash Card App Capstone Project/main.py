#!/usr/bin/env python3
from os import name, system
from tkinter import *
from sys import argv
import pandas
from random import choice


def clear():
    if name == 'nt':
        system('cls')
    else:
        system('clear')


clear()
# Read data from word file
try:
    data = pandas.read_csv(f'{argv[0][:-7]}data/words_to_learn.csv')
except (FileNotFoundError, pandas.errors.EmptyDataError):
    data = pandas.read_csv(f'{argv[0][:-7]}data/french_words.csv')
finally:
    to_learn = data.to_dict(orient='records')
current_card = {}
# ---------- Constants ---------- #
BACKGROUND_COLOR = "#B1DDC6"
COUNTDOWN_SECONDS = 3


# ---------- Countdown one second ---------- #
def countdown(seconds):
    flip_card()


# ---------- Generate new word ---------- #
def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    try:
        current_card = choice(to_learn)
    except IndexError:
        pass
    else:
        canvas.itemconfig(tagOrId=card_image, image=card_front_image)
        canvas.itemconfigure(tagOrId=card_title, text='French', fill='black')
        canvas.itemconfigure(tagOrId=card_word, text=current_card['French'], fill='black')
        flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(tagOrId=card_image, image=card_back_image)
    canvas.itemconfigure(tagOrId=card_title, text='English', fill='white')
    canvas.itemconfigure(tagOrId=card_word, text=current_card['English'], fill='white')


def is_known():
    try:
        to_learn.remove(current_card)
    except ValueError:
        canvas.itemconfig(card_title, text='Congratulations!', fill='black', font=('Ariel', 50, 'bold'))
        canvas.itemconfig(card_word, text='You\'ve learned all the words!', fill='black', font=('Ariel', 40, 'normal'))
    else:
        next_card()


# ---------- UI Setup ---------- #
# Window Setup
window = Tk()
window.title('Flashy')
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

# Canvas Setup
canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
card_front_image = PhotoImage(file=f'{argv[0][:-7]}images/card_front.png')
card_back_image = PhotoImage(file=f'{argv[0][:-7]}images/card_back.png')
card_image = canvas.create_image(400, 263, image=card_front_image)
card_title = canvas.create_text(400, 150, text='Title', font=('Ariel', 40, 'italic'))
card_word = canvas.create_text(400, 263, text='Word', font=('Ariel', 60, 'bold'))
canvas.grid(column=0, row=0, columnspan=2)

# Button(s) Setups
wrong_image = PhotoImage(file=f'{argv[0][:-7]}images/wrong.png')
wrong_button = Button(image=wrong_image, highlightbackground=BACKGROUND_COLOR, command=next_card)
right_image = PhotoImage(file=f'{argv[0][:-7]}images/right.png')
right_button = Button(image=right_image, highlightbackground=BACKGROUND_COLOR, command=is_known)
wrong_button.grid(column=0, row=1)
right_button.grid(column=1, row=1)

next_card()

# Leave at the end
window.mainloop()
learn_these = pandas.DataFrame(to_learn)
learn_these.to_csv(f'{argv[0][:-7]}data/words_to_learn.csv', index=False)
