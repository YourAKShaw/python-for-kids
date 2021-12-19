# 2 5 10 17 26 ... till n terms

# Write a program that prints the above series and calculates the sum of all the terms.

# t(i) = i ** 2 + 1
def formula(i):
    return i ** 2 + 1

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
The formula for this series is t(i) = i ** 2 + 1, where t is the term, and i is the position of the term.

For example,
t(1) = 2
t(2) = 5
t(3) = 10
t(4) = 17
t(5) = 26
...
'''