tshirts = 250
Shirts = 900
Trousers = 1900

a = int(input("Enter the number of t-shirts: "))
b = int(input("Enter the number of shirts: "))
c = int(input("Enter the number of trousers: "))

total = tshirts * a + Shirts * b + Trousers * c

if (total >= 5000):
   total = total - total * 0.05

print("The total bill is: ", total)