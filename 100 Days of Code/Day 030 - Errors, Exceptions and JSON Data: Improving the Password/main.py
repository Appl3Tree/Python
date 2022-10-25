#!/usr/bin/env python3
from os import name, system
# import pandas
from tkinter import *
from tkinter import messagebox, simpledialog
from sys import argv
from random import shuffle, choice
try:
    import pyperclip
except ModuleNotFoundError:
    print('repl sucks and won\'t let me add this module... :/')
import json


def clear():
    if name == 'nt':
        system('cls')
    else:
        system('clear')


clear()
# FileNotFound
# with open('a_file.txt') as file:
#     file.read()
# Fixed
# try:
#     file = open('a_file.txt')
# except FileNotFoundError as error_message:
#     file = open('a_file.txt', 'w')
#     file.write('Something')
#     # file.write('Something')
#     print(error_message)
# else:
#     content = file.read()
#     print(content)
# finally:
#     raise TypeError('This is a made up error')


# KeyError
# a_dictionary = {'key': 'value'}
# value = a_dictionary['non_existent_key']

# IndexError
# fruit_list = ['Apple', 'Banana', 'Pear']
# fruit = fruit_list[3]

# TypeError
# text = 'abc'
# print(text + 5)
# TODO: Code Exercise #1
# height = float(input('Height: '))
# weight = int(input('Weight: '))
#
# if height > 3:
#     raise ValueError('Human Height should not be over 3 meters.')
#
# bmi = weight / height ** 2
# print(bmi)

# TODO: Code Exercise #2
# data = pandas.read_csv('nato_phonetic_alphabet.csv')
# TODO 1. Create a dictionary in this format:
# phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
# print(phonetic_dict)
#
#
# TODO 2. Create a list of the phonetic code words form a word that the user inputs.
# def generate_phonetic():
#     word = input('Enter a word: ').upper()
#     try:
#         output_list = [phonetic_dict[letter] for letter in word]
#     except KeyError:
#         print('Sorry, only letters in the alphabet please.')
#         generate_phonetic()
#     else:
#         print(output_list)
#
#
# generate_phonetic()
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
    global MODE_BG, MODE_FONT, search_button, generate_password_button, add_button
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
        search_button.destroy()
        generate_password_button.destroy()
        add_button.destroy()
        search_button = Button(text='Search', width=13, bg=MODE_BG, fg=MODE_FONT, highlightbackground=MODE_BG)
        search_button.grid(column=2, row=1)
        generate_password_button = Button(text='Generate Password', width=13, bg=MODE_BG, fg=MODE_FONT,
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
        search_button.destroy()
        generate_password_button.destroy()
        add_button.destroy()
        search_button = Button(text='Search', width=13, bg=MODE_BG, fg=MODE_FONT, highlightbackground=MODE_BG)
        search_button.grid(column=2, row=1)
        generate_password_button = Button(text='Generate Password', width=13, bg=MODE_BG, fg=MODE_FONT,
                                          highlightbackground=MODE_BG)
        generate_password_button.grid(column=2, row=3)
        add_button = Button(text='Add', width=36, bg=MODE_BG, fg=MODE_FONT, highlightbackground=MODE_BG)
        add_button.grid(column=1, row=4, columnspan=2)


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    num_letters = simpledialog.askinteger(title='Letters', prompt='How many letters do you want in your password?')
    num_numbers = simpledialog.askinteger(title='Numbers', prompt='How many numbers do you want in your password?')
    num_symbols = simpledialog.askinteger(title='Symbols', prompt='How many symbols do you want in your password?')
    password_letters = ''
    password_numbers = ''
    password_symbols = ''
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+', '{', '}', '[', ']']

    if num_letters:
        password_letters = [choice(letters) for _ in range(num_letters)]
    if num_symbols:
        password_symbols = [choice(symbols) for _ in range(num_symbols)]
    if num_numbers:
        password_numbers = [choice(numbers) for _ in range(num_numbers)]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_entry.get()
    username_email = email_user_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            'email': username_email,
            'password': password
        }
    }

    if website and username_email and password:
        try:
            with open(f'{argv[0][:-7]}data.json', 'r') as data_file:
                # Reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open(f'{argv[0][:-7]}data.json', 'w') as data_file:
                # Saving updated data
                json.dump(new_data, data_file, indent=4)
        except ValueError:
            with open(f'{argv[0][:-7]}data.json', 'w') as data_file:
                # Saving updated data
                json.dump(new_data, data_file, indent=4)
        else:
            try:
                data[website]
            except KeyError:
                pass
            else:
                try:
                    data[website]['old_passwords']
                except KeyError:
                    new_data[website]['old_passwords'] = []
                else:
                    new_data[website]['old_passwords'] = data[website]['old_passwords']
                finally:
                    new_data[website]['old_passwords'].append(data[website]['password'])
            # Updated old data with new data
            data.update(new_data)

            with open(f'{argv[0][:-7]}data.json', 'w') as data_file:
                # Saving updated data
                json.dump(data, data_file, indent=4)
        finally:
            try:
                pyperclip.copy(password)
            except NameError:
                print('repl sucks and won\'t let me add this module... :/')
            website_entry.delete(0, END)
            password_entry.delete(0, END)
            website_entry.focus()
    else:
        messagebox.showerror(title='Oops', message='Please make sure you haven\'t left any fields empty.')


# ---------------------------- SAVE PASSWORD ------------------------------- #
def search():
    website = website_entry.get()
    try:
        with open(f'{argv[0][:-7]}data.json') as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showerror(title='No file', message='There is no data file to search for passwords.')
    except ValueError:
        messagebox.showerror(title='No data', message='There are no currently saved passwords.')
    else:
        try:
            website_data = data[website]
        except KeyError:
            messagebox.showerror(title='Not found', message=f'No saved credentials found for "{website}".')
        else:
            user_email = website_data['email']
            password = website_data['password']
            messagebox.showerror(title='Credentials found!', message=f'Website: {website}\n'
                                                                     f'Email/Username: {user_email}\n'
                                                                     f'Password: {password}')


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Password Manager')
window.config(padx=50, pady=50, bg=MODE_BG)

canvas = Canvas(width=200, height=200, bg=MODE_BG, highlightthickness=0)
logo_img = PhotoImage(file=f'{argv[0][:-7]}logo.png')
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
website_entry = Entry(width=24, bg=MODE_BG, fg=MODE_FONT, highlightthickness=0)
website_entry.grid(column=1, row=1, sticky=W)
website_entry.focus()
email_user_entry = Entry(width=41, bg=MODE_BG, fg=MODE_FONT, highlightthickness=0)
email_user_entry.insert(0, 'example@email.com')
email_user_entry.grid(column=1, row=2, columnspan=2, sticky=W)
password_entry = Entry(width=24, bg=MODE_BG, fg=MODE_FONT, highlightthickness=0)
password_entry.grid(column=1, row=3, sticky=W)

# Buttons
search_button = Button(text='Search', width=13, bg=MODE_BG, fg=MODE_FONT, highlightbackground=MODE_BG, command=search)
search_button.grid(column=2, row=1)
generate_password_button = Button(text='Generate Password', width=13, bg=MODE_BG, fg=MODE_FONT,
                                  highlightbackground=MODE_BG, command=generate_password)
generate_password_button.grid(column=2, row=3)
add_button = Button(text='Add', width=38, bg=MODE_BG, fg=MODE_FONT, highlightbackground=MODE_BG, command=save_password)
add_button.grid(column=1, row=4, columnspan=2)

messagebox.showwarning(title='Warning', message='This application saves data to data.json which is viewable by anyone '
                                                'browsing the repl.it repl.\n'
                                                'DO NOT PUT YOUR ACTUAL CREDENTIALS IN HERE.')

# Keep at the bottom
window.mainloop()
