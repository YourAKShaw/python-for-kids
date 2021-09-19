'''
Write a program to print the pattern
1
1 0
1 0 1
1 0 1 0
1 0 1 0 1
'''

for i in range(0, 5):
    for j in range(0, i + 1):
        print (abs(j % 2 - 1), end=' ')
    print()