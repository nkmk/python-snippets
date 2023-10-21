i = int('1' * 5)
print(i)
# 11111

i = int('1' * 4300)

# i = int('1' * 4301)
# ValueError: Exceeds the limit (4300 digits) for integer string conversion: value has 4301 digits; use sys.set_int_max_str_digits() to increase the limit

s = str(10**5)
print(s)
# 100000

s = str(10**4299)

# s = str(10**4300)
# ValueError: Exceeds the limit (4300 digits) for integer string conversion; use sys.set_int_max_str_digits() to increase the limit

i = 10**10000
# print(i)
# ValueError: Exceeds the limit (4300 digits) for integer string conversion; use sys.set_int_max_str_digits() to increase the limit

i = int('1' * 10000, base=16)

s = hex(10**10000)

import sys

sys.set_int_max_str_digits(1000)

# i = int('1' * 1001)
# ValueError: Exceeds the limit (1000 digits) for integer string conversion: value has 1001 digits; use sys.set_int_max_str_digits() to increase the limit

sys.set_int_max_str_digits(0)

i = int('1' * 100000)
