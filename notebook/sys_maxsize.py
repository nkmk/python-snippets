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

print(sys.float_info.max)
# 1.7976931348623157e+308

i_e309 = 10**309

print(type(i_e309))
# <class 'int'>

print(i_e309 > sys.float_info.max)
# True

print(float('inf'))
# inf

print(i_e309 > float('inf'))
# False

# int(float('inf'))
# OverflowError: cannot convert float infinity to integer
