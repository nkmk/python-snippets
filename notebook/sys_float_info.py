import sys

print(sys.float_info)
# sys.float_info(max=1.7976931348623157e+308, max_exp=1024, max_10_exp=308, min=2.2250738585072014e-308, min_exp=-1021, min_10_exp=-307, dig=15, mant_dig=53, epsilon=2.220446049250313e-16, radix=2, rounds=1)

print(type(sys.float_info))
# <class 'sys.float_info'>

print(sys.float_info.max)
# 1.7976931348623157e+308

print(1.8e+308)
# inf

print(type(1.8e+308))
# <class 'float'>

print(sys.float_info.max.hex())
# 0x1.fffffffffffffp+1023

print(-sys.float_info.max)
# -1.7976931348623157e+308

print(-1.8e+308)
# -inf

print(type(-1.8e+308))
# <class 'float'>

print(sys.float_info.min)
# 2.2250738585072014e-308

print(sys.float_info.min.hex())
# 0x1.0000000000000p-1022

print(float.fromhex('0x0.0000000000001p-1022'))
# 5e-324

print(format(float.fromhex('0x0.0000000000001p-1022'), '.17'))
# 4.9406564584124654e-324

print(1e-323)
# 1e-323

print(1e-324)
# 0.0
