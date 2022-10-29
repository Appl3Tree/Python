#!/usr/bin/env python3
from os import name, system
import requests
from datetime import datetime
import time
import smtplib

HOME_LAT = 46.872128
HOME_LONG = -113.994034


def clear():
    if name == 'nt':
        system('cls')
    else:
        system('clear')


clear()
# TODO: Task #1
# response = requests.get(url='http://api.open-notify.org/iss-now.json')
# response.raise_for_status()
#
# data = response.json()
#
# longitude = data['iss_position']['longitude']
# latitude = data['iss_position']['latitude']
#
# iss_position = (longitude, latitude)
# print(iss_position)

# TODO: Task #2
# from tkinter import *
#
#
# def get_quote():
#     response = requests.get(url='https://api.kanye.rest')
#     response.raise_for_status()
#     data = response.json()
#     quote = data['quote']
#     canvas.itemconfig(tagOrId=quote_text, text=quote)
#
#
# window = Tk()
# window.title("Kanye Says...")
# window.config(padx=50, pady=50)
#
# canvas = Canvas(width=300, height=414)
# background_img = PhotoImage(file="background.png")
# canvas.create_image(150, 207, image=background_img)
# quote_text = canvas.create_text(150, 207, text="Kanye Quote Goes HERE", width=250, font=("Arial", 30, "bold"),
#                                 fill="white")
# get_quote()
# canvas.grid(row=0, column=0)
#
# kanye_img = PhotoImage(file="kanye.png")
# kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
# kanye_button.grid(row=1, column=0)
#
# window.mainloop()

# TODO: Task #3
# parameters = {
#     'lat': HOME_LAT,
#     'lng': HOME_LONG,
#     'formatted': 0
# }
# response = requests.get(url='https://api.sunrise-sunset.org/json', params=parameters)
# response.raise_for_status()
# data = response.json()
# sunrise = data['results']['sunrise'].split('T')[1].split(':')[0]
# sunset = data['results']['sunset'].split('T')[1].split(':')[0]
# print(sunrise)
# print(sunset)
#
# time_now = datetime.now()
# print(time_now.hour)


# TODO: Main Task
def iss_is_above():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if HOME_LAT-5 <= iss_latitude <= HOME_LAT+5 and HOME_LONG-5 <= iss_longitude <= HOME_LONG:
        return True


def is_nighttime():
    parameters = {
        "lat": HOME_LAT,
        "lng": HOME_LONG,
        "formatted": 0,
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    time_now = datetime.utcnow()

    if time_now.hour >= sunset or time_now.hour <= sunrise:
        return True


while True:
    if iss_is_above() and is_nighttime():
        with smtplib.SMTP(host='smtp.freesmtpservers.com', port=25) as connection:
            # connection.starttls()
            # connection.login(user=,password=)
            connection.sendmail(
                from_addr='100daysofpython@freesmtpservers.com',
                to_addrs='example@example.com',
                msg='Subject: Look up!\n\nThe ISS is above you in the sky!'
            )
    time.sleep(60)
