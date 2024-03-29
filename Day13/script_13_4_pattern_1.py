# For n = 5, print the following pattern:
'''
1
1   2
1   2   3
1   2   3   4
1   2   3   4   5
'''
# The pattern should grow for various values of n, and should be symmetrical.
# n should be a positive value.


def print_pattern(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end="\t")
        print()


# driver code
if __name__ == "__main__":
    n = int(input("Enter the value of n: "))
    if (n < 1):
        print("n should be a positive value")
    else:
        print_pattern(n)

'''
print() is equivalent to print(end = "\n")
print(j) is equivalent to print(j, end = "\n")

That's the reason why we chose to use print(j, end = "\t") instead of print(j)
'''