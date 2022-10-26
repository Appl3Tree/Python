#!/usr/bin/env python3
from os import name, system
import smtplib
from datetime import datetime
from sys import argv
from random import choice


def clear():
    if name == 'nt':
        system('cls')
    else:
        system('clear')


clear()
# TODO: Task #1
# Email and smtp testing courtesy of https://www.wpoven.com/tools/free-smtp-server-for-testing
# my_email = '100daysofpython@freesmtpservers.com'
# Make sure "Subject: {}" is filled in. {} being whatever your actual subject is. Two newlines required.
# email_content = '''Subject: Testing emails with Python!
# 
# Hello, this is an email sent from {my_email}
# 
# How are you today?
# 
# Best regards,
# Sender'''
# with smtplib.SMTP(host='smtp.freesmtpservers.com', port=25) as connection:
#     # Free SMTP Servers does not allow TLS and doesn't accept authentication. Use this for a legit service that can do these.
#     # connection.starttls()
#     # connection.login(user='', password='')
#     connection.sendmail(from_addr=my_email,
#                         to_addrs='100daysofpython@mailinator.com',
#                         msg=email_content)

# TODO: Task #2
# now = dt.datetime.now()
# try:
#     with open(f'{argv[0][:-7]}quotes.txt') as file:
#         quotes = file.readlines()
# except FileNotFoundError:
#     print('Quotes file is missing.')
# else:
#     if now.weekday() == 0:
#         with smtplib.SMTP(host='smtp.freesmtpservers.com', port=25) as connection:
#             # connection.starttls()
#             # connection.login(user=,password=)
#             connection.sendmail(from_addr='100daysofpython@freesmtpservers.com',
#                                to_addrs='test@test.com',
#                                msg=f'Subject: Monday Quote!\n\n{choice(quotes)}'
#                                )

# TODO: Task #3
csv_data = {}
try:
    import pandas
except ModuleNotFoundError:
    print('Replit doesn\' like pandas so I guess I\'ll use csv...')
    import csv
    with open(f'{argv[0][:-7]}birthdays.csv') as birthday_file:
        data = csv.reader(birthday_file)
        for val in data:
            if val[0] != 'name':
                csv_data[(int(val[3]), int(val[4]))] = [val[0], val[1], int(val[2]), int(val[3]), int(val[4])]
else:
    data = pandas.readcsv(f'{argv[0][:-7]}birthdays.csv')
    csv_data = {(data_row['month'], data_row['day']): data_row for (index, data_row) in data.iterrows()}
placeholder = '[NAME]'
message = ['''Subject: Happy Birthday!

Dear [NAME],

Happy birthday!

All the best for the year!

Tree''',
           '''Subject: Happy Birthday!

Hey [NAME], happy birthday! Have a wonderful time today and eat lots of cake!

Lots of love,

Tree''',
          '''Subject: Happy Birthday!

Dear [NAME],

It's your birthday! Have a great today!

All my love,

Tree''']
today = datetime.now()
today = (today.month, today.day)

if today in csv_data:
    with smtplib.SMTP(host='smtp.freesmtpservers.com', port=25) as connection:
        # connection.starttls()
        # connection.login(user=, password=)
        dest_name = csv_data[today][0]
        dest_email = csv_data[today][1]
        annual_message = choice(message).replace(placeholder, dest_name)
        connection.sendmail(from_addr='100daysofpython@freesmtpservers.com',
                           to_addrs=dest_email,
                           msg=annual_message)
