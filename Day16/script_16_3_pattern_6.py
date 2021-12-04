# For n = 5, print the following pattern:
'''
2
2 1
2 1 2
2 1 2 1
2 1 2 1 2
'''
# The pattern should grow for various values of n, and should be symmetrical.
# n should be a positive value.


def print_pattern(n):
    pass


# driver code
if __name__ == "__main__":
    n = int(input("Enter the value of n: "))
    if (n < 1):
        print("n should be a positive value")
    else:
        print_pattern(n)
