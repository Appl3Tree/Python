#!/usr/bin/env python3
from art import logo
from os import name, system

#   Basic function to clear screen depending on OS.
def clear():
    if name == 'nt':
        system('cls')
    else:
        system('clear')

#   Function to determine highest bidder.
def findHighestBidder(biddingRecord):
    highestBid = 0
    for bidder in biddingRecord:
        bidAmount = biddingRecord[bidder]
        if bidAmount > highestBid:
            highestBid = bidAmount
            winner = bidder
    highestBid = "{:.2f}".format(highestBid)
    print(f'The winner of the silent auction is {winner} with a bid of ${highestBid}.')

#   Clear screen and display blind auction logo.
clear()
print(logo)

#   Declare necessary variables.
bids = {}
biddingFinished = False

while not biddingFinished:
    print('Welcome to the secret auction program.')
    name = input('What is your name?: ')
    price = float(input('What\'s your bid?: $'))
    bids[name] = price
    shouldContinue = input('Are there any other bidders? Type \'yes\' or \'no\'.\n')
    if shouldContinue == 'no':
        biddingFinished = True
        clear()
        print(logo)
        findHighestBidder(bids)
    else:
        clear()
