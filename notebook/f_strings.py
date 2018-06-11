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

print(f'right : {s:_>8}')
print(f'center: {s:_^8}')
print(f'left  : {s:_<8}')
# right : _____abc
# center: __abc___
# left  : abc_____

i = 1234

print(f'zero padding: {i:08}')
# zero padding: 00001234

print(f'comma: {i:,}')
# comma: 1,234

print(f'bin: {i:b}')
print(f'oct: {i:o}')
print(f'hex: {i:x}')
# bin: 10011010010
# oct: 2322
# hex: 4d2

print(f'bin: {i:#b}')
print(f'oct: {i:#o}')
print(f'hex: {i:#x}')
# bin: 0b10011010010
# oct: 0o2322
# hex: 0x4d2

f = 12.3456

print(f'digit(decimal): {f:.3f}')
print(f'digit(all)    : {f:.3g}')
# digit(decimal): 12.346
# digit(all)    : 12.3

print(f'exponen: {f:.3e}')
# exponen: 1.235e+01

f = 0.123

print(f'percent: {f:.2%}')
# percent: 12.30%

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

print(fr'{x}\t{y}')
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

d = {'key1': 3, 'key2': 4}

print('{0[key1]}, {0[key2]}'.format(d))
# 3, 4

# print('{0["key1"]}, {0["key2"]}'.format(d))
# KeyError: '"key1"'

print(f'{d["key1"]}, {d["key2"]}')
# 3, 4

# print(f'{d[key1]}, {d[key2]}')
# NameError: name 'key1' is not defined

# print(f'{d['key1']}, {d['key2']}')
# SyntaxError: invalid syntax

print(f"{d['key1']}, {d['key2']}")
# 3, 4

# print(f'{d[\'key1\']}, {d[\'key2\']}')
# SyntaxError: f-string expression part cannot include a backslash
