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
WHITE = '#FFFFFF'
BLACK = '#000000'
MODE_BG = WHITE
MODE_FONT = BLACK


# ---------------------------- MODE TOGGLE------------------------------- #
def toggle_mode():
    global MODE_BG, MODE_FONT, generate_password_button, add_button
    if mode_state.get():
        MODE_BG = BLACK
        MODE_FONT = WHITE
        window.config(bg=MODE_BG)
        canvas.config(bg=MODE_BG)
        website_label.config(bg=MODE_BG, fg=MODE_FONT)
        website_entry.config(bg=MODE_BG, fg=MODE_FONT)
        email_user_label.config(bg=MODE_BG, fg=MODE_FONT)
        email_user_entry.config(bg=MODE_BG, fg=MODE_FONT)
        password_label.config(bg=MODE_BG, fg=MODE_FONT)
        password_entry.config(bg=MODE_BG, fg=MODE_FONT)
        light_mode_toggle.config(bg=MODE_BG, fg=MODE_FONT)
        dark_mode_toggle.config(bg=MODE_BG, fg=MODE_FONT)
        generate_password_button.destroy()
        add_button.destroy()
        generate_password_button = Button(text='Generate Password', width=12, bg=MODE_BG, fg=MODE_FONT,
                                          highlightbackground=MODE_BG)
        generate_password_button.grid(column=2, row=3)
        add_button = Button(text='Add', width=36, bg=MODE_BG, fg=MODE_FONT, highlightbackground=MODE_BG)
        add_button.grid(column=1, row=4, columnspan=2)
    else:
        MODE_BG = WHITE
        MODE_FONT = BLACK
        window.config(bg=MODE_BG)
        canvas.config(bg=MODE_BG)
        website_label.config(bg=MODE_BG, fg=MODE_FONT)
        website_entry.config(bg=MODE_BG, fg=MODE_FONT)
        email_user_label.config(bg=MODE_BG, fg=MODE_FONT)
        email_user_entry.config(bg=MODE_BG, fg=MODE_FONT)
        password_label.config(bg=MODE_BG, fg=MODE_FONT)
        password_entry.config(bg=MODE_BG, fg=MODE_FONT)
        light_mode_toggle.config(bg=MODE_BG, fg=MODE_FONT)
        dark_mode_toggle.config(bg=MODE_BG, fg=MODE_FONT)
        generate_password_button.destroy()
        add_button.destroy()
        generate_password_button = Button(text='Generate Password', width=12, bg=MODE_BG, fg=MODE_FONT,
                                          highlightbackground=MODE_BG)
        generate_password_button.grid(column=2, row=3)
        add_button = Button(text='Add', width=36, bg=MODE_BG, fg=MODE_FONT, highlightbackground=MODE_BG)
        add_button.grid(column=1, row=4, columnspan=2)


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Password Manager')
window.config(padx=50, pady=50, bg=MODE_BG)

canvas = Canvas(width=200, height=200, bg=MODE_BG, highlightthickness=0)
logo_img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text='Website:', bg=MODE_BG, fg=MODE_FONT)
website_label.grid(column=0, row=1, sticky=E)
email_user_label = Label(text='Email/Username:', bg=MODE_BG, fg=MODE_FONT)
email_user_label.grid(column=0, row=2, sticky=E)
password_label = Label(text='Password:', bg=MODE_BG, fg=MODE_FONT)
password_label.grid(column=0, row=3, sticky=E)

# Mode Radiobuttons
mode_state = IntVar()
light_mode_toggle = Radiobutton(text='Light Mode', value=0, bg=MODE_BG, fg=MODE_FONT, variable=mode_state,
                                command=toggle_mode)
dark_mode_toggle = Radiobutton(text='Dark Mode', value=1, bg=MODE_BG, fg=MODE_FONT, variable=mode_state,
                               command=toggle_mode)
light_mode_toggle.grid(column=0, row=5, sticky=W)
dark_mode_toggle.grid(column=0, row=6, sticky=W)

# Entries
website_entry = Entry(width=39, bg=MODE_BG, fg=MODE_FONT, highlightthickness=0)
website_entry.grid(column=1, row=1, columnspan=2, sticky=W)
website_entry.focus_set()
email_user_entry = Entry(width=39, bg=MODE_BG, fg=MODE_FONT, highlightthickness=0)
email_user_entry.grid(column=1, row=2, columnspan=2, sticky=W)
password_entry = Entry(width=21, bg=MODE_BG, fg=MODE_FONT, highlightthickness=0)
password_entry.grid(column=1, row=3, sticky=W)

# Buttons
generate_password_button = Button(text='Generate Password', bg=MODE_BG, fg=MODE_FONT, highlightbackground=MODE_BG)
generate_password_button.grid(column=2, row=3)
add_button = Button(text='Add', width=36, bg=MODE_BG, fg=MODE_FONT, highlightbackground=MODE_BG)
add_button.grid(column=1, row=4, columnspan=2)


# Keep at the bottom
window.mainloop()
