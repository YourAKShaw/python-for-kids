# Write a program to print the pattern
'''
*   *
 * *
  *
 * *
*   * 
'''

n = int(input("Size: "))

s1 = 0
s2 = 2 * n - 3

i = 0

while (i < n):
    if (i < n-1):
        extra = "*"
    else :
        extra = ""
    print(" " * s1 + "*" + " " * s2 + extra)
    s1 += 1
    s2 -= 2
    i += 1

s1 -= 2
s2 += 4
i = 0
while (i < n-1):
    print(" " * s1 + "*" + " " * s2 + "*")
    s1 -= 1
    s2 += 2
    i += 1