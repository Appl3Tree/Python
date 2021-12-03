#!/usr/bin/env python3
from os import name, system
from art import logo
import random

# Functions
def clear_screen():
    '''Clears the screen.'''
    if name == 'nt':
        system('cls')
    else:
        system('clear')

def deal_card():
    '''Returns a random card from the deck'''
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def getScore(hand):
    '''Take hand of cards and return the total score from the cards.'''
    if sum(hand) == 21 and len(hand) == 2:
        return 0
    if 11 in hand and sum(hand) > 21:
        hand.remove(11)
        hand.append(1)
    return sum(hand)

def compare(userScore, computerScore):
    '''Compare the user's total score to the computer's total score and return a string regarding the result.'''
    if userScore == computerScore:
        return 'Draw :|'
    elif computerScore == 0:
        return 'Lose, opponent has Blackjack!'
    elif userScore == 0:
        return 'Win with a Blackjack ;)'
    elif userScore > 21:
        return 'You went over. You lose :\'('
    elif computerScore > 21:
        return 'Opponent went over. You win! :D'
    elif userScore > computerScore:
        return 'You win :D'
    else:
        return 'You lose D:'
def playGame():
    print(logo)
    userHand = []
    computerHand = []
    for _ in range(2):
        userHand.append(deal_card())
        computerHand.append(deal_card())

    gameOver = False
    while not gameOver:
        userScore = getScore(userHand)
        computerScore = getScore(computerHand)
        print(f'    Your cards: {userHand}, current score: {userScore}')
        print(f'    Computer\'s first card: {computerHand[0]}')

        if userScore == 0 or computerScore == 0 or userScore > 21:
            gameOver = True
        else:
            userShouldDeal = input('Type \'y\' to get another card, type \'n\' to pass: ')
            if userShouldDeal == 'y':
                userHand.append(deal_card())
                computerHand.append(deal_card())
            else:
                gameOver = True
    while computerScore != 0 and computerScore < 17:
        computerHand.append(deal_card())
        computerScore = getScore(computerHand)

    print(f'\n    Your final hand: {userHand}, final score: {userScore}')
    print(f'    Computer\'s final hand: {computerHand}, final score: {computerScore}')
    print(compare(userScore, computerScore))


clear_screen()
while input('Do you want to play a game of Blackjack? Type \'y\' or \'n\': ') == 'y':
    clear_screen()
    playGame()
