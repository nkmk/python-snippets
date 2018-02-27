import math

a = 6
b = 4

print(math.gcd(a, b))
# 2

def lcm(x, y):
    return (x * y) // math.gcd(x, y)

print(lcm(a, b))
# 12
