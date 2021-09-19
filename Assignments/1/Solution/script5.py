'''
Enter the basic salary of a person. If he get Da at 121% of basic, HRA at
2% of Basic and income tax is deducted as follows-
If salary received> 1,00,000 income tax is deducted at 20% of the total
salary.
If it is less than 1 lakh but greater than 50,000, 5% of the total salary is
deducted.
If total salary is greater than 20,000 but lesser than 50,000 I.T is deducted
at 2% of the total salary.
If it is 20000> then no income tax is deducted.
'''

basic = float(input("Enter the basic salary: "))

da = basic * 121 / 100
hra = basic * 2 / 100

gross = basic + da + hra

tax = 0

if (gross > 100000):
    tax = gross * 20 / 100
elif (gross > 50000):
    tax = gross * 5 / 100
elif (gross > 20000):
    tax = gross * 2 / 100
else:
    tax = 0

print("\nTotal salary: ", gross)
print("Deduction: ", tax)
print("Net salary: ", gross - tax)