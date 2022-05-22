# Rohit buys t-shirts costing 250 each, 
# shirts costing 900 each, trousers costing 
# 1900 each. He gets a discount of 5% 
# if the total amount is equal and above 
# 5000. Print the bill.

tshirts = 250
Shirts = 900
Trousers = 1900

a = int(input("Enter the number of t-shirts: "))
b = int(input("Enter the number of shirts: "))
c = int(input("Enter the number of trousers: "))

total = tshirts * a + Shirts * b + Trousers * c

if (total >= 5000):
   total = total * 0.95

print("The total bill is:", total)