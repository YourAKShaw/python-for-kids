# Find the quotient and remainder on dividing a with b.
# [Note: You need to accept the values for a and b.]

dividend = int(input("dividend = ")) 
divisor =int(input("divisor = ")) 
print()

quotient = dividend // divisor
remainder = dividend - quotient * divisor

print ("On dividing", dividend, "with", divisor, "the result is as follows:")
print ("Quotient =", quotient)
print ("Remainder =", remainder)