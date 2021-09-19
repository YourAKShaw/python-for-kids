# Write a program in which input a string and check whether it is palindrome or not.

string = input("Enter a string: ")

if (string == string[::-1]):
    print("This is palindrome.")
else:
    print("This is not palindrome.")