#!/usr/bin/env python3
from os import name, system
# import csv
# import turtle
import pandas


def clear():
    if name == 'nt':
        system('cls')
    else:
        system('clear')


clear()
# TODO: Task #1 (Day 26)
# numbers = [1, 2, 3]
# Normal way of adding to a list
# new_list = []
# for n in list:
#     add_1 = n + 1
#     new_list.append(add_1)

# List comprehension
# new_list = [n + 1 for n in numbers]

# TODO: Task #2 (Day 26)



# Day 25 tasks below here.
# TODO: Task #1
# with open('weather_data.csv', 'r') as data_file:
#     data = data_file.readlines()
# print(data)

# with open('weather_data.csv') as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1].isnumeric():
#             temperatures.append(int(row[1]))
#     print(temperatures)

# TODO: Task #2
# data = pandas.read_csv('weather_data.csv')
# print(type(data))
# print(type(data['temp']))
#
# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = data['temp'].to_list()
# print(temp_list)
#
# print(f'The mean temperature is: {data["temp"].mean()}')
# print(f'The median temperature is: {data["temp"].median()}')
# print(f'The minimum temperature is: {data["temp"].min()}')
# print(f'The maximum temperature is: {data["temp"].max()}')
#
# # Get Data in Columns
# print(data['condition'])
# print(data.condition)
#
# # Get Data in Rows
# print(data[data.day == 'Monday'])
# print(data[data.temp == data.temp.max()])
# monday = data[data.day == 'Monday']
# print(monday.condition)
#
# monday_temp = int(monday.temp)
# print(f'Monday\'s temperature in Fahrenheit is: {monday_temp * (9/5) + 32 }')
#
# # Create a dataframe from scratch
# data_dict = {
#     'student': ['Amy', 'James', 'Angela'],
#     'scores': [76, 56, 65]
# }
# data = pandas.DataFrame(data_dict)
# data.to_csv('new_data.csv')

# TODO: Task #3
# data = pandas.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
# grey_squirrels = len(data[data['Primary Fur Color'] == 'Gray'])
# red_squirrels = len(data[data['Primary Fur Color'] == 'Cinnamon'])
# black_squirrels = len(data[data['Primary Fur Color'] == 'Black'])
#
# data_dict = {
#     'Fur Color': ['Grey', 'Red', 'Black'],
#     'Count': [grey_squirrels, red_squirrels, black_squirrels]
# }
# squirrel_data = pandas.DataFrame(data_dict)
# squirrel_data.to_csv('squirrel_count.csv')
# print('2018 Central Park Squirrel Census - Squirrel Data')
# print(squirrel_data)

# TODO: U.S. States Game
# screen = turtle.Screen()
# screen.title('U.S. States Game')
# screen.setup(width=825, height=566)
# screen.screensize(canvwidth=725, canvheight=491)
# image = 'blank_states_img.gif'
#
# screen.addshape(image)
# image_turtle = turtle.Turtle()
# image_turtle.shape(image)
#
# states_data = pandas.read_csv('50_states.csv')
# state_names_list = states_data['state'].tolist()
#
# correct_guesses = []
#
# while len(correct_guesses) < 50:
#     answer_state = screen.textinput(title=f'{len(correct_guesses)}/50 States Correct!',
#                                     prompt='What\'s another state\'s name?')
#     if answer_state:
#         answer_state = answer_state.title()
#     if answer_state == 'Exit':
#         # States to learn.csv
#         states_to_learn = [state for state in state_names_list if state not in correct_guesses]
#         # Replaced by above list comprehension.
#         # for state in state_names_list:
#         #     if state not in correct_guesses:
#         #         states_to_learn.append(state)
#         learn_these = pandas.DataFrame(states_to_learn)
#         learn_these.to_csv('states_to_learn.csv')
#         break
#
#     if (answer_state in state_names_list) and (answer_state not in correct_guesses):
#         state = states_data[states_data['state'] == answer_state]
#         penboi = turtle.Turtle()
#         penboi.hideturtle()
#         penboi.speed('fastest')
#         penboi.penup()
#         penboi.goto(int(state.x), int(state.y))
#         penboi.write(f'{answer_state}', align='center', font=('Courier', 12, 'normal'))
#
#         correct_guesses.append(answer_state)

# TODO: NATO Alphabet Game


# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }

# Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     pass

# student_data_frame = pandas.DataFrame(student_dict)

# Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
data = pandas.read_csv('nato_phonetic_alphabet.csv')
alphabet = {nato.letter: nato.code for (index, nato) in data.iterrows()}

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
# result = [alphabet[letter] for letter in input('Enter a word: ').upper()]
# print(result)
print([alphabet[letter] for letter in input('Enter a word: ').upper()])
