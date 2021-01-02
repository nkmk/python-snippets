import math

print(math.gcd(6, 4))
# 2

print(math.lcm(6, 4))
# 12

def my_lcm(x, y):
    return (x * y) // math.gcd(x, y)

print(my_lcm(6, 4))
# 12
