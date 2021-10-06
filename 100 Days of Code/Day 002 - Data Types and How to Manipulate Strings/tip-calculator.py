#!/usr/bin/env python3

print('\t*******************************************')
print('\t*      Welcome to the Tip Calculator      *')
print('\t*******************************************\n')
total = float(input('What was the total bill?\n\t$'))
percentTip = float(input('What percentage tip would you like to give? 10, 12, or 15?\n\t')) / 100
numPeople = int(input('How many people to split the bill?\n\t'))
total = total + (total * percentTip)
totalPerPerson = str(round(total / numPeople, 2))
if totalPerPerson[-2] == '.':
    totalPerPerson += '0'
print(f'Each person should pay: ${totalPerPerson}')
