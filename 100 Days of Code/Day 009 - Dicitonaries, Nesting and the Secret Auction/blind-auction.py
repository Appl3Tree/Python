#!/usr/bin/env python3
from art import logo
from os import name, system

def clear():
    if name == 'nt':
        system('cls')
    else:
        system('clear')
clear()
print(logo)
bids = []
moreBidders = 'yes'
while moreBidders != 'no':
    print('Welcome to the secret auction program.')
    bidderName = input('What is your name?: ')
    bid = float(input('What\'s your bid?: $'))
    bids.append({'Name': bidderName, 'Bid': bid})
    moreBidders = input('Are there any other bidders? Type \'yes\' or \'no\'.\n')
    clear()

highestBid = 0
winner = ''
for bidder in bids:
    if bidder['Bid'] > highestBid:
        winner = bidder['Name']
        highestBid = bidder['Bid']
highestBid = "{:.2f}".format(highestBid)
print(f'The winner of the blind auction is {winner} with a bid of ${highestBid}.\n')
