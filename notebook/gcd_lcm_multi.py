import math

print(math.gcd(27, 18, 9))
# 9

print(math.gcd(27, 18, 9, 3))
# 3

print(math.lcm(27, 9, 3))
# 27

print(math.lcm(27, 18, 9, 3))
# 54

l = [27, 18, 9, 3]
print(math.gcd(*l))
# 3

print(math.lcm(*l))
# 54

from functools import reduce

def my_gcd(*numbers):
    return reduce(math.gcd, numbers)

print(my_gcd(27, 18, 9))
# 9

print(my_gcd(27, 18, 9, 3))
# 3

l = [27, 18, 9, 3]
print(my_gcd(*l))
# 3

def my_lcm_base(x, y):
    return (x * y) // math.gcd(x, y)

def my_lcm(*numbers):
    return reduce(my_lcm_base, numbers, 1)

print(my_lcm(27, 9, 3))
# 27

print(my_lcm(27, 18, 9, 3))
# 54

l = [27, 18, 9, 3]
print(my_lcm(*l))
# 54
