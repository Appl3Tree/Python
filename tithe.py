#!/usr/bin/env python3
from os import name, system
hours x pay rate = gross

PAY_RATE = 20.4213

payRateChanged = input(f'Has your pay rate changes from ${PAY_RATE}? ')
if payRateChanged == 'y' or payRateChanged == 'Y':
    PAY_RATE = float(input('What has it changed to? '))


def clear():
    if name == 'nt':
        system('cls')
    else:
        system('clear')

hours = int(input('How many hours will you work? '))
grossPay = PAY_RATE * hours
PERSCI = grossPay * .079003
taxablePay = grossPay - PERSCI
socialSecurityTax = taxablePay * 0.062000
medicareTax = taxablePay * 0.014500

#1a taxablePay
#1b 26
#1c 0
#1d 0 / 26 = 0
#1e taxablePay + 0
#1f 0
#1g 0 / 26 = 0
#1h adjusted wage amount = taxablePay - 0

#2a 1021
#2b 89.76
#2c 22%
#2d taxablePay - 1021 = 0
#2e #2d * #2c
#2f tentative withholding amount = 89.76 + #2e (196.1600262354)

#3a 0
#3b 0 / 26
#3c 0

