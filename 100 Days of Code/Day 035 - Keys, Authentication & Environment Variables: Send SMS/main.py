#!/usr/bin/env python3
from os import name, system, environ
import requests
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient
from secret import *


def clear():
    if name == 'nt':
        system('cls')
    else:
        system('clear')


clear()
# Free tier options
current = 'https://api.openweathermap.org/data/2.5/weather'
# 5-day forecast, broken up in 3 hour chunks
forecast = 'https://api.openweathermap.org/data/2.5/forecast'
weather_params = {
    'lat': 46.872128,
    'lon': -113.994034,
    'appid': api_key
}

response = requests.get(url=forecast, params=weather_params)
response.raise_for_status()
weather_data = response.json()['list']
weather_slice = weather_data[:4]

will_rain = False

for chunk in weather_slice:
    condition_code = chunk['weather'][0]['id']
    if condition_code > 700:
        will_rain = True
if will_rain:
    proxy_client = TwilioHttpClient()
    proxy_client.session.proxies = {'https': environ['https_proxy']}

    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
            body="☔️ Bring an umbrella today! ☔️",
            from_= twilio_number,
            to= personal_number
        )
    print(message.status)
