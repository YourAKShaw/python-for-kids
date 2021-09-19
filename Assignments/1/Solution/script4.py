'''
Rohit buys t-shirts costing 250 each, shirts costing 900 each, trousers
costing 1900 each. He gets a discount of 5% if the total amount is equal
and above 5000. Print the bill.
'''

tshirts = 250
shirts = 900
trousers = 1900

x = int(input("Enter the number of t-shirts: "))
y = int(input("Enter the number of shirts: "))
z = int(input("Enter the number of trousers: "))

total = tshirts * x + shirts * y + trousers * z

if (total >= 5000):
    total = total - total * 0.05

print("\nBill: ", total)
