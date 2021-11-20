# Program to accept a day number and print the respective day

# function to return the day of the week for a given day number
# in case of invalid day number, return "Invalid day number"
def day_number_to_day(day_number):

    # dictionary for day number to day
    days = {
        1: 'Monday',
        2: 'Tuesday',
        3: 'Wednesday',
        4: 'Thursday',
        5: 'Friday',
        6: 'Saturday',
        7: 'Sunday'
    }
    
    # if day number is valid, return the day
    # else return "Invalid day number"
    return days.get(day_number, "Invalid day number")
    
# driver code
day_number = int(input('Enter a day number: '))
print(day_number_to_day(day_number))

'''
Driver code is the part of the program that runs the program OR initiates the program.
'''