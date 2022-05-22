'''
Accept a day number from the user, and display the day of the week that day is.

    1. If the user enters a number between 1 and 7, then display the day of the week that number represents.
    2. If the user enters a number that is less than 1 or greater than 7, then display an error message.

NOTE: Make use of an if-elif-else ladder.
'''

day_number = int(input("Enter the day number: "))

if day_number == 1:
    print("Monday")
elif day_number == 2:
    print("Tuesday")
elif day_number == 3:
    print("Wednesday")
elif day_number == 4:
    print("Thursday")
elif day_number == 5:
    print("Friday")
elif day_number == 6:
    print("Saturday")
elif day_number == 7:
    print("Sunday")
else:
    print("Invalid option!")
