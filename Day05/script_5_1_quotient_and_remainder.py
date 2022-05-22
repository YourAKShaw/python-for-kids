# Find the quotient and remainder on dividing a with b.
# [Note: You need to accept the values for a and b.]

dividend = int(input("dividend = ")) 
divisor = int(input("divisor = ")) 
print()

quotient = dividend // divisor
remainder = dividend % divisor

# The '%' is known as the modulus operator (MOD or mod in short).
# It is used for calculating the remainder.
# Hence the statements below are equivalent: 
# -> remainder = dividend - quotient * divisor
# -> remainder = dividend % divisor

print ("On dividing", dividend, "with", divisor, "the result is as follows:")
print ("Quotient =", quotient)
print ("Remainder =", remainder)