# range()

'''
range() is function which is used to create various ranges of lists
'''

l = list(range(10))

print('list(range(10))', l)

'''
range(x, y, z)

x - is the starting value; default value is 0 (zero)
y - is the upper bound or lower bound, greater than the highest value in the range or lesser than the least value in the range; this value should always be given
z - is the step value, default value is 1 

Other forms of using range is range(x, y) and range(y)
'''

l = list(range(0, 10, 1))

print('list(range(0, 10, 1))', l)

l = list(range(0, 10, 2))
print('list(range(0, 10, 2))', l)

l = list(range(10, 0, -1))
print('list(range(10, 0, -1))', l)

l = list(range(1, 6))
print('list(range(1, 6))', l)