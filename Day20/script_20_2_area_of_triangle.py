# Write a program to find the area of a triangle using Heron’s formula.

from math import sqrt

a = int(input('Enter first side: '))
b = int(input('Enter second side: '))
c = int(input('Enter third side: '))

s = (a + b + c) / 2
area = sqrt((s*(s-a)*(s-b)*(s-c)))
print("The area of the triangle is", area)
