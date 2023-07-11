import math

print(math.e)
# 2.718281828459045

print(2**4)
# 16

print(pow(2, 4))
# 16

print(math.pow(2, 4))
# 16.0

print(pow(1 + 1j, 2))
# 2j

# print(math.pow(1 + 1j, 2))
# TypeError: must be real number, not complex

print(pow(2, 4, 5))
# 1

print(2**0.5)
# 1.4142135623730951

print(math.sqrt(2))
# 1.4142135623730951

print(2**0.5 == math.sqrt(2))
# True

print((-3 + 4j) ** 0.5)
# (1.0000000000000002+2j)

# print(math.sqrt(-3 + 4j))
# TypeError: must be real number, not complex

print((-1) ** 0.5)
# (6.123233995736766e-17+1j)

# print(math.sqrt(-1))
# ValueError: math domain error

import cmath

print(cmath.sqrt(-3 + 4j))
# (1+2j)

print(cmath.sqrt(-1))
# 1j

print(math.exp(2))
# 7.38905609893065

print(math.exp(2) == math.e**2)
# False

print(math.log(25, 5))
# 2.0

print(math.log(math.e))
# 1.0

print(math.log10(100000))
# 5.0

print(math.log2(1024))
# 10.0
