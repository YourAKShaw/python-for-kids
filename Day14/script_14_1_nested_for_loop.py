n = 5

for i in range(1, n + 1):
    print("\n", i, "\n")
    for j in range(1, i + 1):
        print(j)
    print()

'''
For every iteration of the outer loop, the inner loop will be executed.

The print statement above is only used for visualizing the values of i and j.

For n = 5, the values of i is 1 to 5.
For every value of i, the values of j is 1 to i.
When i = 1, j = 1
When i = 2, j = 1, 2
When i = 3, j = 1, 2, 3
When i = 4, j = 1, 2, 3, 4
When i = 5, j = 1, 2, 3, 4, 5
'''
