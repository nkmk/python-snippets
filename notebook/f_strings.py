a = 123
b = 'abc'

print('{} and {}'.format(a, b))
# 123 and abc

print('{first} and {second}'.format(first=a, second=b))
# 123 and abc

print(f'{a} and {b}')
# 123 and abc

print(F'{a} and {b}')
# 123 and abc

print(f"{a} and {b}")
# 123 and abc

print(f'''{a} and {b}''')
# 123 and abc

print(f"""{a} and {b}""")
# 123 and abc

s = 'abc'

print(f'right : {s:*>8}')
print(f'center: {s:*^8}')
print(f'left  : {s:*<8}')
# right : *****abc
# center: **abc***
# left  : abc*****

i = 1234

print(f'zero padding: {i:08}')
# zero padding: 00001234

i = 1234567890

print(f'comma: {i:,}')
# comma: 1,234,567,890

i = 255

print(f'bin       : {i:b}')
print(f'oct       : {i:o}')
print(f'hex(lower): {i:x}')
print(f'hex(upper): {i:X}')
# bin       : 11111111
# oct       : 377
# hex(lower): ff
# hex(upper): FF

print(f'bin       : {i:08b}')
print(f'oct       : {i:08o}')
print(f'hex(lower): {i:08x}')
print(f'hex(upper): {i:08X}')
# bin       : 11111111
# oct       : 00000377
# hex(lower): 000000ff
# hex(upper): 000000FF

print(f'bin       : {i:#010b}')
print(f'oct       : {i:#010o}')
print(f'hex(lower): {i:#010x}')
print(f'hex(upper): {i:#010X}')
# bin       : 0b11111111
# oct       : 0o00000377
# hex(lower): 0x000000ff
# hex(upper): 0X000000FF

f = 12.3456

print(f'decimal places    : {f:.3f}')
print(f'significant digits: {f:.3g}')
# decimal places    : 12.346
# significant digits: 12.3

f = 12.3456

print(f'exponent(lower): {f:.3e}')
print(f'exponent(upper): {f:.3E}')
# exponent(lower): 1.235e+01
# exponent(upper): 1.235E+01

f = 0.123

print(f'percent: {f:.2%}')
# percent: 12.30%

import datetime

dt = datetime.datetime(2020, 1, 5, 20, 15, 30)

print(f'datetime: {dt}')
# datetime: 2020-01-05 20:15:30

print(f'datetime: {dt:%A, %m/%d/%Y %I:%M:%S %p}')
# datetime: Sunday, 01/05/2020 08:15:30 PM

print(f'datetime: {dt.isoformat()}')
# datetime: 2020-01-05T20:15:30

n = 123

print(f'{{}}-{n}-{{{n}}}')
# {}-123-{123}

n = 123
i = 8

print('{n:0{i}}'.format(n=n, i=i))
# 00000123

print(f'{n:0{i}}')
# 00000123

f = 1.2345

for i in range(5):
    print(f'{f:.{i}f}')
# 1
# 1.2
# 1.23
# 1.234
# 1.2345

print('x\ty')
# x	y

print(r'x\ty')
# x\ty

x = 'XXX'
y = 'YYY'

print(f'{x}\t{y}')
# XXX	YYY

print(rf'{x}\t{y}')
# XXX\tYYY

print(FR'{x}\t{y}')
# XXX\tYYY

a = 3
b = 4

# print('{a} + {b} = {a + b}'.format(a=a, b=b))
# KeyError: 'a + b'

print(f'{a} + {b} = {a + b}')
# 3 + 4 = 7

print(f'{a} * {b} = {a * b}')
# 3 * 4 = 12

print(f'{a} / {b} = {a / b:.2e}')
# 3 / 4 = 7.50e-01

d = {'key1': 10, 'key2': 20}

print('{0[key1]}, {0[key2]}'.format(d))
# 10, 20

# print('{0["key1"]}, {0["key2"]}'.format(d))
# KeyError: '"key1"'

print(f'{d["key1"]}, {d["key2"]}')
# 10, 20

# print(f'{d[key1]}, {d[key2]}')
# NameError: name 'key1' is not defined

# print(f'{d['key1']}, {d['key2']}')
# SyntaxError: invalid syntax

print(f"{d['key1']}, {d['key2']}")
# 10, 20

# print(f'{d[\'key1\']}, {d[\'key2\']}')
# SyntaxError: f-string expression part cannot include a backslash

i = 123

print(f'{i=}')
# i=123

print(f'{i = }')
# i = 123

print(f'{ i  =   }')
#  i  =   123

print(f'{i = :#b}')
# i = 0b1111011

print(f'{i * 2 = }')
# i * 2 = 246

l = [0, 10, 20]

print(f'{l = }, {l[1] = }')
# l = [0, 10, 20], l[1] = 10

d = {'key1': 10, 'key2': 20}

print(f'{d = }, {d["key1"] = }')
# d = {'key1': 10, 'key2': 20}, d["key1"] = 10
