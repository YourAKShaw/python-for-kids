# Prepare a bill on the basis of the following information-
# If number of electricity units consumed is less than 50, no charges have
# to be paid.
# If it is between 50 and 100, 1 re. per unit consumed.
# If it is between 100 to 200 units , 2.5 re per unit.
# If it is between 200 to 400, 4 re. per unit.
# If it is between 400-800 then 6 re. per unit.
# If it is above 800 then 8 re. per unit.
# Every consumer has to pay a meter rent of Rs.700 and GST is charged at
# 2% on the number of units consumed.

units = int(input("Enter the number of units consumed: "))

charge = 0

if (units < 50):
    charge = 0
elif (units >= 50 and units <= 100):
    charge = 50 * 0 + (units - 50) * 1
elif (units >= 100 and units <= 200):
    charge = 50 * 0 + 50 * 1 + (units - 100) * 2.5
elif (units >= 200 and units <= 400):
    charge = 50 * 0 + 50 * 1 + 100 * 2.5 + (units - 200) * 4
elif (units >= 400 and units <= 800):
    charge = 50 * 0 + 50 * 1 + 100 * 2.5 + 200 * 4 + (units - 400) * 6
elif (units >= 800):
    charge = 50 * 0 + 50 * 1 + 100 * 2.5 + \
        200 * 4 + 400 * 6 + (units - 800) * 8

meter_rent = 700
gst = units * 0.02

print()
print("Charge:", charge)
print("Meter rent:", meter_rent)
print("GST:", gst)
print("Total:", charge + meter_rent + gst)

# The '\' character is used at the end when we need to type the rest of the line in the next line.
