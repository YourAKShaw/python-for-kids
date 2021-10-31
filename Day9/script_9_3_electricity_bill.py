'''
Given an integer U denoting the amount of KWh (Kilo-Watt-hour) units of electricity consumed, the task is to calculate the electricity bill with the help of the below charges: 

1 to 100 units – Rs. 10/unit
100 to 200 units – Rs. 15/unit
200 to 300 units – Rs. 20/unit
above 300 units – Rs. 25/unit
'''

units_consumed = int(input("Enter the units consumed: "))

if (units_consumed >= 1 and units_consumed <= 100):
    bill = units_consumed * 10
elif (units_consumed >= 101 and units_consumed <= 200):
    bill = 100 * 10 + (units_consumed - 100) * 15
elif (units_consumed >= 201 and units_consumed <= 300):
    bill = 100 * 10 + 100 * 15 + (units_consumed - 200) * 20
elif (units_consumed >= 301):
    bill = 100 * 10 + 100 * 15 + 100 * 20 + (units_consumed - 300) * 20

print("The electricity bill is: ", bill)