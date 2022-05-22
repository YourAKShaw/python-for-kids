units = int(input("Enter the number of units consumed: "))

charge = 0

if (units < 50):
    charge = 0
elif (units >= 50 and units <= 100):
    charge = units * 1
elif (units >= 100 and units <= 200):
    charge = units * 2.5
elif (units >= 200 and units <= 400):
    charge = units * 4
elif (units >= 400 and units <= 800):
    charge = units * 6
elif (units >= 800):
    charge = units * 8

meter_rent = 700

gst = units * 0.02

print("Charge: ", charge)

print("Meter rent: ", meter_rent)

print("GST: ", gst)

print("Total: ", charge + meter_rent + gst)