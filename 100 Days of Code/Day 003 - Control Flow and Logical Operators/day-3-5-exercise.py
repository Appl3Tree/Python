#!/usr/bin/env python3

print('Welcome to the Love Calculator!')
name1 = input('What is your name?\n')
name2 = input('What is their name?\n')

combined_names = name1 + name2
lower_case_string = combined_names.lower()
true = 0
love = 0

true += lower_case_string.count('t')
true += lower_case_string.count('r')
true += lower_case_string.count('u')
true += lower_case_string.count('e')

love += lower_case_string.count('l')
love += lower_case_string.count('o')
love += lower_case_string.count('v')
love += lower_case_string.count('e')

if love >= 10:
    true += 1
    love = 0

score = int(str(true) + str(love))

if score < 10 or score > 90:
    print(f'Your score is {score}, you go together like coke and mentos.')
elif score >= 40 and score <= 50:
    print(f'Your score is {score}, you are alright together.')
else:
    print(f'Your score is {score}.')
