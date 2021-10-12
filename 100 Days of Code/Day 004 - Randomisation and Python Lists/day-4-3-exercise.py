#!/usr/bin/env python3
row1 = ['X', 'X', 'X']
row2 = ['X', 'X', 'X']
row3 = ['X', 'X', 'X']
map = [row1, row2, row3]
print(f'{row1}\n{row2}\n{row3}')
position = input('Where do you want to put the treasure? ')

col = int(position[0]) - 1
row = int(position[1]) - 1

map[row][col] = 'C'
print(f'{row1}\n{row2}\n{row3}')
