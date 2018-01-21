def my_round(val, digit=0):
    p = 10 ** digit
    return (val * p * 2 + 1) // 2 / p

my_round_int = lambda x: int((x * 2 + 1) // 2)

f = 123.456

print(int(my_round(f)))
# 123

print(my_round_int(f))
# 123

print(my_round(f, 1))
# 123.5

print(my_round(f, 2))
# 123.46

print(int(my_round(0.4)))
print(int(my_round(0.5)))
print(int(my_round(0.6)))
# 0
# 1
# 1

i = 99518

print(int(my_round(i, -1)))
# 99520

print(int(my_round(i, -2)))
# 99500

print(int(my_round(i, -3)))
# 100000

print(int(my_round(4, -1)))
print(int(my_round(5, -1)))
print(int(my_round(6, -1)))
# 0
# 10
# 10

print(int(my_round(-0.4)))
print(int(my_round(-0.5)))
print(int(my_round(-0.6)))
# 0
# 0
# -1

import math

def my_round2(val, digit=0):
    p = 10 ** digit
    s = math.copysign(1, val)
    return (s * val * p * 2 + 1) // 2 / p * s

print(int(my_round2(-0.4)))
print(int(my_round2(-0.5)))
print(int(my_round2(-0.6)))
# 0
# -1
# -1
