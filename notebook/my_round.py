def my_round(number, ndigits=0):
    p = 10**ndigits
    return (number * p * 2 + 1) // 2 / p

def my_round_int(number):
    return int((number * 2 + 1) // 2)

f = 123.456

print(my_round(f))
# 123.0

print(int(my_round(f)))
# 123

print(my_round(f, 1))
# 123.5

print(my_round(f, 2))
# 123.46

print(my_round_int(f))
# 123

print('0.4 =>', int(my_round(0.4)))
print('0.5 =>', int(my_round(0.5)))
print('0.6 =>', int(my_round(0.6)))
# 0.4 => 0
# 0.5 => 1
# 0.6 => 1

i = 99518

print(int(my_round(i, -1)))
# 99520

print(int(my_round(i, -2)))
# 99500

print(int(my_round(i, -3)))
# 100000

print('4 =>', int(my_round(4, -1)))
print('5 =>', int(my_round(5, -1)))
print('6 =>', int(my_round(6, -1)))
# 4 => 0
# 5 => 10
# 6 => 10

print('-0.4 =>', int(my_round(-0.4)))
print('-0.5 =>', int(my_round(-0.5)))
print('-0.6 =>', int(my_round(-0.6)))
# -0.4 => 0
# -0.5 => 0
# -0.6 => -1

import math

def my_round2(number, ndigits=0):
    p = 10**ndigits
    return (abs(number) * p * 2 + 1) // 2 / p * math.copysign(1, number)

print('-0.4 =>', int(my_round2(-0.4)))
print('-0.5 =>', int(my_round2(-0.5)))
print('-0.6 =>', int(my_round2(-0.6)))
# -0.4 => 0
# -0.5 => -1
# -0.6 => -1
