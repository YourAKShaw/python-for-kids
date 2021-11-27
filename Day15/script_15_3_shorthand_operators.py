# Shorthand Operators in Python

# Shorthand Operators are used to assign values to variables.
# These are also called assignment operators.

# a += b means a = a + b
# a -= b means a = a - b
# a *= b means a = a * b
# a /= b means a = a / b
# a //= b means a = a // b
# a %= b means a = a % b
# a **= b means a = a ** b

a = 5
b = 6
print("a =", a)
print("b =", b)
print()

a = 5
a += b
print('a += b ->', a)

a = 5
a -= b
print('a -= b ->', a)

a = 5
a *= b
print('a *= b ->', a)

a = 5
a /= b
print('a /= b ->', a)

a = 5
a //= b
print('a //= b ->', a)

a = 5
a %= b
print('a %= b ->', a)

a = 5
a **= b
print('a **= b ->', a)

print()
print('All the above values are stored in \'a\' after the operation.')
print('Hence, they are termed as shorthand or assignment operators.')