# accept an integer and print the digits in reverse

n = int(input("Enter a positive integer: "))
print()

while (n!=0):
    digit = n % 10 # extract the last digit
    print(digit) # print the last digit
    n = n // 10 # remove the last digit

'''

123 / 10

q = 12
r = 3

456 / 10

q = 45
r = 6

q = dividend // divisor
r = dividend % divisor

In case of quotient calculation, where the divisor is 10, the quotient is the number formed by removing the last digit.
In case of remainder calculation, where the divisor is 10, the remainder is the last digit.
'''

'''
In our above example, the loop is executed for every digit in the number. That means that the loop is not fixed, and depends on the input from the user. In such cases, where the loop is not fixed, we can use a while loop.
'''