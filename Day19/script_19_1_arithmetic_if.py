'''
Accept two numbers from user and a character.

If the character is '+' then add the two numbers and print the result.
If the character is '-' then subtract the two numbers and print the result.
If the character is '*' then multiply the two numbers and print the result.
If the character is '/' then divide the two numbers and print the result.

In case of any other character print "Invalid input"
'''

a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
c = input("Enter the action character: ")
print()

if c == '+':
    print("The sum result of the two numbers is: ", a + b)
elif c == '-':
    print("The difference result of the two numbers is: ", a - b)
elif c == '*':
    print("The product result of the two numbers is: ", a * b)
elif c == '/':
    print("The division result of the two numbers is: ", a / b)
else:
    print("Invalid Input!")
