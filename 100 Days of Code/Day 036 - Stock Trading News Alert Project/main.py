#!/usr/bin/env python3
import os
import re
import requests
from secrets import *
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient
from bs4 import BeautifulSoup


def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


clear()
STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

# STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
parameters = {
    'function': 'TIME_SERIES_DAILY',
    'symbol': STOCK_NAME,
    'outputsize': 'compact',
    'apikey': stocks_api_key
}

# TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries.
#  e.g. [new_value for (key, value) in dictionary.items()]
response = requests.get(url=STOCK_ENDPOINT, params=parameters)
response.raise_for_status()
data = response.json()['Time Series (Daily)']
data_list = [value for (key, value) in data.items()][:2]
yesterday_closing_price = float(data_list[0]['4. close'])
# print(f'yesterdays closing price: {yesterday_closing_price}')

# TODO 2. - Get the day before yesterday's closing stock price
yesterday_eve_closing_price = float(data_list[1]['4. close'])
# print(f'yesterday eves closing price: {yesterday_eve_closing_price}')

# TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20.
#  Hint: https://www.w3schools.com/python/ref_func_abs.asp
difference = abs(yesterday_closing_price - yesterday_eve_closing_price)
# print(f'difference: {difference}')

# TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day
#  before yesterday.
difference_percent = (yesterday_closing_price / yesterday_eve_closing_price) * 100
# print(f'difference %: {difference_percent}')

# TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").
# if abs(difference_percent - 100) > 5:
#     print("Get News")

# STEP 2: https://newsapi.org/
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

# TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.
# if abs(difference_percent - 100) > 5:
url = 'https://newsapi.org/v2/everything'
parameters = {
    'apiKey': news_api_key,
    'q': COMPANY_NAME,
    'pageSize': 3
}
response = requests.get(url=url, params=parameters)
response.raise_for_status()
data = response.json()['articles']
# print(data)

# TODO 7. - Use Python slice operator to create a list that contains the first 3 articles.
#  Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation
# Unnecessary because of the pageSize parameter.

# STEP 3: Use twilio.com/docs/sms/quickstart/python
# to send a separate message with each article's title and description to your phone number.

# TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.
formatted_messages = [f"Headline: {article['title']}. \nBrief: {article['description']}" for article in data]

# TODO 9. - Send each article as a separate message via Twilio.
for message in formatted_messages:
    message = re.sub('<[^<]+?>', '', message)
    # proxy_client = TwilioHttpClient()
    # proxy_client.session.proxies = {'https': os.environ['https_proxy']}
    if difference_percent - 100 > 0:
        change_icon = '📈'
    else:
        change_icon = '📉'
    #     client = Client(account_sid, auth_token)
    #     message = client.messages \
    #         .create(
    #         body=f"{STOCK_NAME}: {change_icon} {round(abs(difference_percent - 100))}%\n{message}",
    print(f"{STOCK_NAME}: {change_icon} {round(abs(difference_percent - 100))}%\n{message}")
#         from_=twilio_number,
#         to=personal_number
#     )
#     print(message.status)
# Optional TODO: Format the message like this:
# """
# TSLA: 🔺2%
# Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?.
# Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to
# file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height
# of the coronavirus market crash.
# or
# "TSLA: 🔻5%
# Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?.
# Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to
# file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height
# of the coronavirus market crash.
# """
