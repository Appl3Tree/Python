#!/usr/bin/env python3
import os
import requests
USERNAME = 'appletree'
TOKEN = 'kfjhasldfeb',


def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


clear()
pixela_endpoint = 'https://pixe.la/v1/users'
user_params = {
    'token': TOKEN,
    'username': USERNAME,
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes',
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# response.raise_for_status
# print(response.text)

graph_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs'



response = requests.post()
response.raise_for_status
print(response.text)
