# Write a program to find the area of a triangle using Heron’s formula.

a = float(input("Enter the length of side a: "))
b = float(input("Enter the length of side b: "))
c = float(input("Enter the length of side c: "))

s = (a + b + c) / 2

area = (s * (s - a) * (s - b) * (s - c)) ** 0.5

print("\nThe area of the triangle is: ", area)
