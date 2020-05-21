import sys

print(sys.maxsize)
# 9223372036854775807

print(type(sys.maxsize))
# <class 'int'>

print(sys.maxsize == 2**63 - 1)
# True

print(bin(sys.maxsize))
# 0b111111111111111111111111111111111111111111111111111111111111111

print(hex(sys.maxsize))
# 0x7fffffffffffffff

i = 10**100

print(i)
# 10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000

print(i > sys.maxsize)
# True

print(float('inf'))
# inf

print(i > float('inf'))
# False
