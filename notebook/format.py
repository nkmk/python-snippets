i = 255

print(format(i, '#04x'))
print(type(format(i, '#04x')))
# 0xff
# <class 'str'>

s = 'abc'

print(format(s, '*^10'))
# ***abc****

print('{:#04x}'.format(i))
print(type('{:#04x}'.format(i)))
# 0xff
# <class 'str'>

print('{:*^10}'.format(s))
# ***abc****

print('{}-{}-{}'.format(255, 'abc', 1.23))
# 255-abc-1.23

print('{}-{}'.format(255, 'abc', 1.23))
# 255-abc

# print('{}-{}-{}-{}'.format(255, 'abc', 1.23))
# IndexError: Replacement index 3 out of range for positional args tuple

print('{0}-{1}-{0}'.format(255, 'abc'))
# 255-abc-255

print('{name} is {age} years old.'.format(name='Alice', age=20))
# Alice is 20 years old.

l = ['one', 'two', 'three']
print('{0[0]}-{0[1]}-{0[2]}'.format(l))
# one-two-three

d1 = {'name': 'Alice', 'age': 20}
d2 = {'name': 'Bob', 'age': 30}
print('{0[name]} is {0[age]} years old.\n{1[name]} is {1[age]} years old.'.format(d1, d2))
# Alice is 20 years old.
# Bob is 30 years old.

l = ['one', 'two', 'three']
print('{}-{}-{}'.format(*l))
# one-two-three

d = {'name': 'Alice', 'age': 20}
print('{name} is {age} years old.'.format(**d))
# Alice is 20 years old.

print('{{}}-{num}-{{{num}}}'.format(num=100))
# {}-100-{100}

print('{num} = {num:#x} = {num:#b}'.format(num=255))
# 255 = 0xff = 0b11111111

print('left  : {:<10}'.format(100))
print('center: {:^10}'.format(100))
print('right : {:>10}'.format(100))
# left  : 100       
# center:    100    
# right :        100

print('left  : {:*<10}'.format(100))
print('center: {:*^10}'.format(100))
print('right : {:*>10}'.format(100))
# left  : 100*******
# center: ***100****
# right : *******100

print('sign: {:0>10}'.format(-100))
print('sign: {:0=10}'.format(-100))
# sign: 000000-100
# sign: -000000100

# print('sign: {:0=10}'.format('-100'))
# ValueError: '=' alignment not allowed in string format specifier

print('sign: {:0=10}'.format(int('-100')))
# sign: -000000100

print('zero padding: {:0=10}'.format(100))
print('zero padding: {:010}'.format(100))
# zero padding: 0000000100
# zero padding: 0000000100

print('zero padding: {:0=10}'.format(-100))
print('zero padding: {:010}'.format(-100))
# zero padding: -000000100
# zero padding: -000000100

# print('zero padding: {:010}'.format('-100'))
# ValueError: '=' alignment not allowed in string format specifier

print('sign: {}'.format(100))
print('sign: {}'.format(-100))
# sign: 100
# sign: -100

print('sign: {:+}'.format(100))
print('sign: {:+}'.format(-100))
# sign: +100
# sign: -100

print('sign: {: }'.format(100))
print('sign: {: }'.format(-100))
# sign:  100
# sign: -100

print('sign: {:06}'.format(100))
print('sign: {:06}'.format(-100))
# sign: 000100
# sign: -00100

print('sign: {:+06}'.format(100))
print('sign: {:+06}'.format(-100))
# sign: +00100
# sign: -00100

print('sign: {: 06}'.format(100))
print('sign: {: 06}'.format(-100))
# sign:  00100
# sign: -00100

print('sign: {:*>6}'.format(100))
print('sign: {:*>6}'.format(-100))
# sign: ***100
# sign: **-100

print('sign: {:*>+6}'.format(100))
print('sign: {:*>+6}'.format(-100))
# sign: **+100
# sign: **-100

print('sign: {:*> 6}'.format(100))
print('sign: {:*> 6}'.format(-100))
# sign: ** 100
# sign: **-100

print('{:,}'.format(100000000))
print('{:_}'.format(100000000))
# 100,000,000
# 100_000_000

print('{:,}'.format(1234.56789))
print('{:_}'.format(1234.56789))
# 1,234.56789
# 1_234.56789

print('bin: {:b}'.format(255))
print('oct: {:o}'.format(255))
print('hex: {:x}'.format(255))
print('HEX: {:X}'.format(255))
# bin: 11111111
# oct: 377
# hex: ff
# HEX: FF

print('bin: {:08b}'.format(255))
print('oct: {:08o}'.format(255))
print('hex: {:08x}'.format(255))
print('HEX: {:08X}'.format(255))
# bin: 11111111
# oct: 00000377
# hex: 000000ff
# HEX: 000000FF

print('bin: {:#b}'.format(255))
print('oct: {:#o}'.format(255))
print('hex: {:#x}'.format(255))
print('HEX: {:#X}'.format(255))
# bin: 0b11111111
# oct: 0o377
# hex: 0xff
# HEX: 0XFF

print('bin: {:#010b}'.format(255))
print('oct: {:#010o}'.format(255))
print('hex: {:#010x}'.format(255))
print('HEX: {:#010X}'.format(255))
# bin: 0b11111111
# oct: 0o00000377
# hex: 0x000000ff
# HEX: 0X000000FF

print('hex: {:08x}'.format(255))
print('hex: {:09_x}'.format(255))
print('hex: {:#011_x}'.format(255))
# hex: 000000ff
# hex: 0000_00ff
# hex: 0x0000_00ff

# print('hex: {:08x}'.format('255'))
# ValueError: Unknown format code 'X' for object of type 'str'

print('hex: {:08x}'.format(int('255')))
# hex: 000000ff

print('{}'.format(0.00001234))
print('{}'.format(12340000000000000.0))
print('{:f}'.format(0.00001234))
print('{:f}'.format(12340000000000000.0))
# 1.234e-05
# 1.234e+16
# 0.000012
# 12340000000000000.000000

print('{:.2f}'.format(123.456))
print('{:.5f}'.format(123.456))
print('{:.3f}'.format(0.0001234))
# 123.46
# 123.45600
# 0.000

print('{:.0f}'.format(0.4))
print('{:.0f}'.format(0.5))
print('{:.0f}'.format(0.6))
# 0
# 0
# 1

print('{:.5f}'.format(10e1000))
print('{:.5F}'.format(10e1000))
# inf
# INF

print('{:e}'.format(0.0001234))
print('{:E}'.format(0.0001234))
# 1.234000e-04
# 1.234000E-04

print('{:.5e}'.format(0.0001234))
print('{:.2e}'.format(0.0001234))
# 1.23400e-04
# 1.23e-04

print('{:.5e}'.format(987.65))
print('{:.2e}'.format(987.65))
# 9.87650e+02
# 9.88e+02

print('{:>12.5e}'.format(987.65))
print('{:012.2e}'.format(987.65))
#  9.87650e+02
# 00009.88e+02

print('{:g}'.format(0.0001234))
print('{:g}'.format(0.00001234))
# 0.0001234
# 1.234e-05

print('{:.2g}'.format(123.456))
print('{:.3g}'.format(123.456))
print('{:.8g}'.format(123.456))
print('{:.3g}'.format(0.0001234))
# 1.2e+02
# 123
# 123.456
# 0.000123

print('{:#.2g}'.format(123.456))
print('{:#.3g}'.format(123.456))
print('{:#.8g}'.format(123.456))
print('{:#.3g}'.format(0.0001234))
# 1.2e+02
# 123.
# 123.45600
# 0.000123

print('{:.2}'.format(123.456))
print('{:.3}'.format(123.456))
print('{:.8}'.format(123.456))
print('{:.3}'.format(0.0001234))
# 1.2e+02
# 1.23e+02
# 123.456
# 0.000123

print('{:#.2}'.format(123.456))
print('{:#.3}'.format(123.456))
print('{:#.8}'.format(123.456))
print('{:#.3}'.format(0.0001234))
# 1.2e+02
# 1.23e+02
# 123.45600
# 0.000123

print('{:.3f}'.format(123.456))
print('{:.3e}'.format(123.456))
print('{:.3g}'.format(123.456))
print('{:.3}'.format(123.456))
# 123.456
# 1.235e+02
# 123
# 1.23e+02

print('{:.8f}'.format(123.456))
print('{:.8e}'.format(123.456))
print('{:.8g}'.format(123.456))
print('{:.8}'.format(123.456))
# 123.45600000
# 1.23456000e+02
# 123.456
# 123.456

print('{:.4e}'.format(123.456))
print('{:.4e}'.format(0.000012345))
print('{:.4e}'.format(12))
# 1.2346e+02
# 1.2345e-05
# 1.2000e+01

print('{:.2g}'.format(123.456))
print('{:.2g}'.format(10e1000))
print('{:.2G}'.format(123.456))
print('{:.2G}'.format(10e1000))
# 1.2e+02
# inf
# 1.2E+02
# INF

print('{:%}'.format(0.12345))
print('{:.2%}'.format(0.12345))
# 12.345000%
# 12.35%

print('{:%}'.format(10))
print('{:.2%}'.format(10))
# 1000.000000%
# 1000.00%

print('{:>10.2%}'.format(0.12345))
print('{:010.2%}'.format(0.12345))
#     12.35%
# 000012.35%

import datetime

dt = datetime.datetime(2020, 1, 5, 20, 15, 30)

print('datetime: {}'.format(dt))
# datetime: 2020-01-05 20:15:30

print('datetime: {:%A, %m/%d/%Y %I:%M:%S %p}'.format(dt))
# datetime: Sunday, 01/05/2020 08:15:30 PM

print('datetime: {}'.format(dt.isoformat()))
# datetime: 2020-01-05T20:15:30
