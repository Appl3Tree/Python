#!/usr/bin/env python3
from os import name, system
from tkinter import *


def clear():
    if name == 'nt':
        system('cls')
    else:
        system('clear')


clear()
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps
    if timer:
        window.after_cancel(timer)
    title_label.config(text='Timer', fg=GREEN)
    check_marks.config(text='')
    canvas.itemconfig(timer_text, text='00:00')
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        start_countdown(long_break_sec)
        title_label.config(text='Break!', fg=RED)
    elif reps % 2 == 0:
        start_countdown(short_break_sec)
        title_label.config(text='Break!', fg=PINK)
    else:
        start_countdown(work_sec)
        title_label.config(text='Work!', fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def start_countdown(total_seconds):
    global reps, timer
    minutes = int(total_seconds // 60)
    seconds = int(total_seconds % 60)
    canvas.itemconfig(timer_text, text=f'{minutes:02d}:{seconds:02d}')
    if total_seconds > 0:
        timer = window.after(1000, start_countdown, total_seconds - 1)
    else:
        start_timer()
        if reps % 2 == 0:
            check_marks['text'] += '✔'


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Pomodoro')
window.config(padx=100, pady=50, bg=YELLOW)


title_label = Label(text='Timer', fg=GREEN, bg=YELLOW, font=(FONT_NAME, 45))
title_label.grid(row=0, column=1)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
canvas_image = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=canvas_image)
timer_text = canvas.create_text(100, 130, text='00:00', fill='white', font=(FONT_NAME, 35, 'bold'))
canvas.grid(row=1, column=1)


start_button = Button(text='Start', width=2, highlightbackground=YELLOW, command=start_timer)
start_button.grid(row=2, column=0)
reset_button = Button(text='Reset', width=2, highlightbackground=YELLOW, command=reset_timer)
reset_button.grid(row=2, column=2)

check_marks = Label(text='', fg=GREEN, bg=YELLOW, font=(FONT_NAME, 20))
check_marks.grid(row=3, column=1)


# Keep at the end.
window.mainloop()
