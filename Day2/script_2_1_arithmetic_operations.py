print("Arithmetic operations in Python")
print()

# Initializing a variable `a` with the integer value 5
a = 5

# Initializing a variable `b` with the integer value 6
b = 6

print("The value of a is", a)
print("The value of b is", b)
print()

# Addition operation
sum = a + b

print("Sum of a and b is", sum)
print()

# Subtraction operation
minus = a - b

print("On subtracting b from a we get", minus)
print()

# Multiplication operation
multiplication = a * b

print("Product of a and b is", multiplication)
print()

# Division operation
division = a / b

print("On dividing a with b we get", division)
print()

'''
In case of division, whenever the dividend is lesser than 
the divisor, then the value of division will give us a 
value in decimals, which is lesser than 1.
'''

# Floor division operation
floor_division = a // b

print("On dividing a with b, the quotient is", floor_division)
print()

# Floor division is actually calculating the quotient.

# The following statements find the quotient and remainder 
# of the division of 17 with 5.
dividend = 17
divisor = 5
quotient = dividend // divisor
remainder = dividend - quotient * divisor

print("On dividing 17 with 5, the quotient is", quotient)
print("On dividing 17 with 5, the remainder is", remainder)
print()

# Exponentiation operation
exponentiation = a ** b

print("On exponentiation of a to the power b, we get", exponentiation)
print()

# Exponentiation of 2 ** 3 means 2 * 2 * 2 = 8.

# 2 ^ 3 and 2 ** 3 means the same thing in 
# general mathematical presentation.
# But, in Python, 2 ^ 3 and 2 ** 3, have two different meanings. 

# 2 ** 2 is also called: 
# -> '2 to the power 2', or 
# -> '2 square', or 
# -> 'square of 2'.

# 2 ** 3 is also called: 
# -> '2 to the power 3', or 
# -> '2 cube', or 
# -> 'cube of 2'. 

# 2 ** 4 is also called '2 to the power 4', and so on.