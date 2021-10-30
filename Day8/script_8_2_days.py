day_number = int(input("Enter the day number: "))

if day_number == 1:
    print("Monday")
if day_number == 2:
    print("Tuesday")
if day_number == 3:
    print("Wednesday")
if day_number == 4:
    print("Thursday")
if day_number == 5:
    print("Friday")
if day_number == 6:
    print("Saturday")
if day_number == 7:
    print("Sunday")

'''
The above code works, but it is not very efficient.

The reason is that, every time the code is executed, all the if conditions are checked.

This can be improved by using an if-elif-else ladder.
'''