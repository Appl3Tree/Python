#!/usr/bin/env python3

a = input("a:")
b = input("b:")

#   Easy option would be to create a third variable to store one variable then do some switcheroo stuff.
a = int(a) + int(b)
b = int(a) - int(b)
a = a - b


print("a = " + str(a))
print("b = " + str(b))
