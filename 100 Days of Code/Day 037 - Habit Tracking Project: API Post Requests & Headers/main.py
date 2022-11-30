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

now = datetime.now()
today = now.strftime("%Y%m%d")
graph_url = f'{graph_endpoint}/graph1'
graph_params = {
    'date': today,
    'quantity': '1',
}

response = requests.post(url=graph_url, json=graph_params, headers=headers)
response.raise_for_status
print(response.text)