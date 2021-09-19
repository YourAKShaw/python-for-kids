# Write a program to print the series : s=1+x^2/2!+x^3/3!+.........+x^n/n!

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

n = int(input("Enter the number of terms: "))
print('\n1')
x = 2
s = 1
while x <= n:
    t = x**x/factorial(x)
    s = s + t
    print(t)
    x+=1
print('\nsum =', s)