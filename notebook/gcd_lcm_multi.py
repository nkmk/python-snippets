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

import functools

def my_gcd(*integers):
    return functools.reduce(math.gcd, integers)

print(my_gcd(27, 18, 9))
# 9

print(my_gcd(27, 18, 9, 3))
# 3

l = [27, 18, 9, 3]
print(my_gcd(*l))
# 3

def my_lcm_base(x, y):
    return (x * y) // math.gcd(x, y)

def my_lcm(*integers):
    return functools.reduce(my_lcm_base, integers)

print(my_lcm(27, 9, 3))
# 27

print(my_lcm(27, 18, 9, 3))
# 54

l = [27, 18, 9, 3]
print(my_lcm(*l))
# 54

print(math.gcd())
# 0

print(math.lcm())
# 1

# print(my_gcd())
# TypeError: reduce() of empty iterable with no initial value

# print(my_lcm())
# TypeError: reduce() of empty iterable with no initial value

def my_gcd_init(*integers):
    return functools.reduce(math.gcd, integers, 0)

print(my_gcd_init())
# 0

print(my_gcd_init(27, 18, 9, 3))
# 3

def my_lcm_init(*integers):
    return functools.reduce(my_lcm_base, integers, 1)

print(my_lcm_init())
# 1

print(my_lcm_init(27, 18, 9, 3))
# 54
