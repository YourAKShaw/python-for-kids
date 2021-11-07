# Palindrome

'''
A palindrome is a word, phrase, number, or other sequence of characters which reads the same backward or forward. Which means that, if you reverse the sequence of characters in a string, you get the original string.

The following are palindromes:

- madam
- 101
- racecar
'''

# Write a program to accept a positive integer and check whether it's a positive palindrome integer.

n = int(input("Enter a positive integer: "))

original = n
rev = 0

while(n > 0):
    digit = n % 10 
    rev = rev * 10 + digit     
    n = n // 10 

if (original==rev):
    print("The number is a palindrome.")
else:
    print("The number is not a palindrome.")
