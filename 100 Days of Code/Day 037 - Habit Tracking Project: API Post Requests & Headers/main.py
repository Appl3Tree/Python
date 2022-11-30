#!/usr/bin/env python3
import os
import requests
from datetime import datetime

USERNAME = 'appletree'
TOKEN = 'kfjhasldfeb'


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
graph_config = {
    'id': 'graph1',
    'name': 'Cycling Graph',
    'unit': 'Km',
    'type': 'float',
    'color': 'ajisai',
}
headers = {
    'X-USER-TOKEN': TOKEN,
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# response.raise_for_status
# print(response.text)

today = datetime.now().strftime("%Y%m%d")
pixel_creation_endpoint = f'{graph_endpoint}/graph1'
while True:
    try:
        distance_travelled = float(input('How far did you travel today (Km)?\n'))
    except ValueError:
        print('A number is required. Please try again.')
    else:
        break
        
graph_params = {
    'date': today,
    'quantity': distance_travelled,
}

# response = requests.post(url=pixel_creation_endpoint, json=graph_params, headers=headers)
# response.raise_for_status
