# if-elif-else ladder

'''
if is a conditional statement that is used to perform different actions based on different conditions.
'''

if (5 < 6):
    print('5 is less than 6')

print()
print()

a = 6
if (a == 5):
    print('a is equal to 5')
else:
    print('a is not equal to 5')
    
print()
print()

a = 6
b = 5

if (a < b):
    print('a is less than b')
elif (a == b):
    print('a is equal to b')
else:
    print('a is greater than b')

# elif stands for `else if`

'''
On comaparing 2 numbers, we get one of the following 3 results:

- a is less than b
- a is equal to b
- a is greater than b
'''

print()
print()

if (a < b):
    print('a is less than b')
elif (a == b):
    print('a is equal to b')
elif (a > b):
    print('a is greater than b')

'''
Conclusion:

    - An if statement states whether to execute some code or not.
    - An elif statement states the same as if, but is executed only if the previous if statement is not true.
    - An else statement is executed if all the previous conditions are not true.
'''

'''
NOTE:

If a if condition is true, then the code under the if block is executed and the successive elif and else blocks are not executed.
'''