# 2 5 10 17 26 ... till n terms

# Write a program that prints the above series and calculates the sum of all the terms.

# t(i) = ?
def formula(i):
    pass

if __name__ == "__main__":
    n = int(input("Enter the number of terms: "))
    print()
    print("The series is:")
    print()
    sum = 0
    for i in range(1, n + 1):
        term = formula(i)
        print(term, end=" ")
        sum += term
    print()
    print()
    print("The sum of all the terms is:", sum)
        

'''
The formula for this series is t(i) = ?, where t is the term, and i is the position of the term.

For example,
t(1) = 2
t(2) = 5
t(3) = 10
t(4) = 17
t(5) = 26
...
'''