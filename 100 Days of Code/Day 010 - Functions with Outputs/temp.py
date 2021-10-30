#!/usr/bin/env python3

def format_name(fName, lName):
    formatted_fName = fName.title()
    formatted_lName = lName.title()
    return f'{formatted_fName} {formatted_lName}'

print(format_name('fOrReSt', 'CONNELLY'))