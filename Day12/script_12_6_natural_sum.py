'''
Accept a natural number n and print the sum of the first n natural numbers.

If n = 5, then sum = 1 + 2 + 3 + 4 + 5 = 15
If n = 10, then sum = 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10 = 55

[NOTE: Use for loop to solve this problem.]
'''

n = int(input("Enter the number: "))
total = 0
for i in range(1, n + 1):
    total = total + i
print("Sum of first", n, "natural numbers is:", total)
