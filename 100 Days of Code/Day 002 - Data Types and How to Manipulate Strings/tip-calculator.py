#!/usr/bin/env python3

#   Banner
print('\t*******************************************')
print('\t*      Welcome to the Tip Calculator      *')
print('\t*******************************************\n')

#   Inputs
total = float(input('What was the total bill?\n\t$'))
percentTip = int(input('What percentage tip would you like to give? 10, 12, or 15?\n\t')) / 100
numPeople = int(input('How many people to split the bill?\n\t'))

#   Do math things
total = total + (total * percentTip)
totalPerPerson = "{:.2f}".format(total / numPeople)

#   Display the price per person.
print(f'Each person should pay: ${totalPerPerson}')
