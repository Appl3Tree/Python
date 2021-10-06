#!/usr/bin/env python3

age = int(input('What is your current age? '))
yearsLeft = 90 - age
daysLeft = 365 * yearsLeft
weeksLeft = 52 * yearsLeft
monthsLeft = 12 * yearsLeft

print(f'You have {daysLeft} days, {weeksLeft} weeks and {monthsLeft} months left.')
