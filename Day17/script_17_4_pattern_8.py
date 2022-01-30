# For n = 5, print the following pattern:
'''
*
* #
* # *
* # * #
* # * # *
'''
# The pattern should grow for various values of n, and should be symmetrical.
# n should be a positive value.


def print_pattern(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            if (j % 2 == 1):
                print("*", end=' ')
            else:
                print("#", end=' ')
        print()


# driver code
if __name__ == "__main__":
    n = int(input("Enter the value of n: "))
    if (n < 1):
        print("n should be a positive value")
    else:
        print_pattern(n)
