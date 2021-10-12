#!/usr/bin/env python3

student_heights = input('Input a list of student heights: ').split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights)

totalHeight = 0
numStudents = 0
for height in student_heights:
    totalHeight += height
    numStudents += 1
averageHeight = round(totalHeight / numStudents)
print(f'The average height is: {averageHeight}.')
