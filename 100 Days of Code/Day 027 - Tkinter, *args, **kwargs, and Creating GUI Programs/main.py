#!/usr/bin/env python3
from os import name, system
import tkinter
# import tkinter.font


def clear():
    if name == 'nt':
        system('cls')
    else:
        system('clear')


# def button_clicked():
#     label['text'] = entry.get()
#
#
# def spinbox_used():
#     # Gets the current value in spinbox.
#     print(spinbox.get())
#
#
# def scale_used(value):
#     print(value)
#
#
# def checkbutton_used():
#     # Print 1 if butt is checked, otherwise 0.
#     print(checked_state.get())
#
#
# def radio_used():
#     print(radio_state.get())
#
#
# def listbox_used(event):
#     # Gets current selection from listbox
#     print(listbox.get(listbox.curselection()))


clear()
# Creating a new window and configurations
window = tkinter.Tk()
window.title('Miles to Kilometer Converter')
# window.minsize(width=500, height=300)
window.config(padx=20, pady=20)
#
# Labels
# label = tkinter.Label(text='This is old text')
# label['text'] = 'This is new text'
# Other way to do the above is below.
# my_label.config(text='This is new text')
# pack() puts this object on the screen.
# label.pack()
# label.place(x=100, y=200)
# label.grid(column=0, row=0)
# label.config(padx=50, pady=50)
#
#
# Buttons
# Calls button_clicked() when pressed.
# button = tkinter.Button(text='Click Me', command=button_clicked)
# button.pack()
# button.grid(column=1, row=1)
#
# new_button = tkinter.Button(text='New Button', command=button_clicked)
# new_button.grid(column=2, row=0)
#
# Entries
# entry = tkinter.Entry(width=10)
# Add some text to begin with.
# entry.insert(tkinter.END, string='Some text.')
# Gets text in entry.
# print(entry.get())
# entry.pack()
# entry.grid(column=3, row=2)
#
# Text
# text = tkinter.Text(height=5, width=30)
# Puts cursor in textbox.
# text.focus()
# Adds some text to begin with.
# text.insert(tkinter.END, 'Example of multi-line text entry.')
# Gets current value in textbox at line 1, character 0.
# print(text.get('1.0', tkinter.END))
# text.pack()
#
#
# Spinbox
# spinbox = tkinter.Spinbox(from_=0, to=10, width=5, command=spinbox_used)
# spinbox.pack()
#
#
# Scale
# Called with current scale value.
# scale = tkinter.Scale(from_=0, to=100, command=scale_used)
# scale.pack()
#
#
# Checkbutton
# checked_state = tkinter.IntVar()
# checkbutton = tkinter.Checkbutton(text='Is on?', variable=checked_state, command=checkbutton_used)
# checked_state.get()
# checkbutton.pack()
#
#
# Radiobutton
# radio_state = tkinter.IntVar()
# radiobutton1 = tkinter.Radiobutton(text='Option 1', value=1, variable=radio_state, command=radio_used)
# radiobutton2 = tkinter.Radiobutton(text='Option 2', value=2, variable=radio_state, command=radio_used)
# radiobutton1.pack()
# radiobutton2.pack()
#
#
# Listbox
# listbox = tkinter.Listbox(height=4)
# fruits = ['Apple', 'Pear', 'Orange', 'Banana']
# for item in fruits:
#     listbox.insert(fruits.index(item), item)
# listbox.bind('<<ListboxSelect>>', listbox_used)
# listbox.pack()


def calculate_km():
    miles = num_miles.get()
    if miles.isnumeric():
        num_kms['text'] = round(int(miles) * 1.60934)
        error['text'] = ''
    else:
        error.config(fg='red')
        error['text'] = 'The number of miles must be a valid integer.'


# Creating objects
miles_label = tkinter.Label(text='Miles')
km_label = tkinter.Label(text='Km')
equal_to_label = tkinter.Label(text='is equal to')
num_kms = tkinter.Label(text=0)
num_miles = tkinter.Entry(width=7)
num_miles.insert(tkinter.END, '0')
calculate_button = tkinter.Button(text='Calculate', command=calculate_km)
error = tkinter.Label()

# Placing objects on grid
equal_to_label.grid(column=0, row=1)
num_miles.grid(column=1, row=0)
num_kms.grid(column=1, row=1)
calculate_button.grid(column=1, row=2)
error.grid(column=1, row=3)
miles_label.grid(column=2, row=0)
km_label.grid(column=2, row=1)


# Keep at end
window.mainloop()
