# Accept a positive integer and print the reverse of it.

n = int(input("Enter a positive integer: "))    # | n = 123
print()

rev = 0                                         # | rev = 0

while n > 0:                                    # | 123 > 0 = True          | 12 > 0 = True         | 1 > 0 = True              |
    digit = n % 10 # extract the last digit     # | digit = 123 % 10 = 3    | digit = 12 % 10 = 2   | digit = 1 % 10 = 1        |
    rev = rev * 10 + digit # ??                 # | rev = 0 * 10 + 3 = 3    | rev = 3 * 10 + 2 = 32 | rev = 32 * 10 + 1 = 321   |
    n = n // 10 # remove the last digit         # | n = 123 // 10 = 12      | n = 12 // 10 = 1      | n = 1 // 10 = 0           |

print("The reverse of the number is:", rev)
