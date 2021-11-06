# Accept a positive integer and print the reverse of it.

n = int(input("Enter a positive integer: "))
print()

rev = 0

while n > 0:
    digit = n % 10 # extract the last digit
    rev = rev * 10 + digit # revering formula    
    n = n // 10 # remove the last digit

print("The reverse of the number is:", rev)
