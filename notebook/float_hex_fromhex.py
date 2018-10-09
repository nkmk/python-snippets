f = 256.0

print(f.hex())
# 0x1.0000000000000p+8

print(type(f.hex()))
# <class 'str'>

print(256.0.hex())
# 0x1.0000000000000p+8

print(0.5.hex())
# 0x1.0000000000000p-1

print(42.195.hex())
# 0x1.518f5c28f5c29p+5

i = 256

# print(i.hex())
# AttributeError: 'int' object has no attribute 'hex'

s = '0x1.0000000000000p+8'

print(float.fromhex(s))
# 256.0

print(type(float.fromhex(s)))
# <class 'float'>

print(float.fromhex('0x1p+8'))
# 256.0

print(float.fromhex('1p+8'))
# 256.0

print(float.fromhex('0x100'))
# 256.0

print(float.fromhex('100'))
# 256.0

print(float.fromhex('0xf2.f8p-10'))
# 0.237274169921875

print((15 * 16**1 + 2 * 16**0 + 15 * 16**-1 + 8 * 16**-2) * 2**-10)
# 0.237274169921875

import sys

f_max = sys.float_info.max

print(f_max)
# 1.7976931348623157e+308

print(f_max.hex())
# 0x1.fffffffffffffp+1023

print(float.fromhex('0x1.fffffffffffffp+1023'))
# 1.7976931348623157e+308

# print(float.fromhex('0x1.0000000000000p+1024'))
# OverflowError: hexadecimal value too large to represent as a float

# print(float.fromhex('0x2.0000000000000p+1023'))
# OverflowError: hexadecimal value too large to represent as a float

f_min = sys.float_info.min

print(f_min)
# 2.2250738585072014e-308

print(f_min.hex())
# 0x1.0000000000000p-1022

print(float.fromhex('0x1.0000000000000p-1022'))
# 2.2250738585072014e-308

print(float.fromhex('0x0.0000000000001p-1022'))
# 5e-324

print(format(float.fromhex('0x0.0000000000001p-1022'), '.17'))
# 4.9406564584124654e-324

print(float.fromhex('0x0.0000000000001p-1023'))
# 0.0
