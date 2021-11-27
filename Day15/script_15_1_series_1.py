# 1 2 3 4 5 ... till n terms

# Write a program that prints the above series and calculates the sum of all the terms.

# t(i) = i
def formula(i):
    return i

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
The formula for this series is t(i) = i, where t is the term, and i is the position of the term.

For example,
t(1) = 1
t(2) = 2
t(3) = 3
t(4) = 4
t(5) = 5
...
'''