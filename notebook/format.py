s = format(255, '04x')
print(s)
print(type(s))
# 00ff
# <class 'str'>

print(format('center', '*^16'))
# *****center*****

s = '{:04x}'.format(255)
print(s)
print(type(s))
# 00ff
# <class 'str'>

print('{:*^16}'.format('center'))
# *****center*****

print('{}-{}-{}'.format('100', '二百', 300))
# 100-二百-300

print('{0}-{1}-{0}'.format('foo', 'bar'))
# foo-bar-foo

print('{year}年{month}月{day}日'.format(year=2018, month=1, day=11))
# 2018年1月11日

person1 = {'name': 'Alice', 'age': 20}
person2 = {'name': 'Bob', 'age': 30}
print('{0[name]} is {0[age]} years old.{1[name]} is {1[age]} years old.'.format(person1, person2))
# Alice is 20 years old.Bob is 30 years old.

print('{num:x}'.format(num=255))
# ff

print('{year}年{month:02}月{day:02}日'.format(year=2018, month=1, day=11))
# 2018年01月11日

print('{{}}-{num}-{{{num}}}'.format(num=100))
# {}-100-{100}

print('left  : {:<10}'.format(100))
print('center: {:^10}'.format(100))
print('right : {:>10}'.format(100))
# left  : 100       
# center:    100    
# right :        100

print('left  : {:*<10}'.format(100))
print('center: {:a^10}'.format(100))
print('right : {:鬼>10}'.format(100))
# left  : 100*******
# center: aaa100aaaa
# right : 鬼鬼鬼鬼鬼鬼鬼100

print('zero padding: {:0>10}'.format(100))
print('zero padding: {:010}'.format(100))
# zero padding: 0000000100
# zero padding: 0000000100

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

print('{:,}'.format(100000000))
# 100,000,000

print('{:_}'.format(100000000))
# 100_000_000

print('bin: {:b}'.format(255))
print('oct: {:o}'.format(255))
print('dec: {:d}'.format(255))
print('hex: {:x}'.format(255))
print('HEX: {:X}'.format(255))
# bin: 11111111
# oct: 377
# dec: 255
# hex: ff
# HEX: FF

print('bin: {:08b}'.format(255))
print('oct: {:08o}'.format(255))
print('dec: {:08d}'.format(255))
print('hex: {:08x}'.format(255))
print('HEX: {:08X}'.format(255))
# bin: 11111111
# oct: 00000377
# dec: 00000255
# hex: 000000ff
# HEX: 000000FF

print('bin: {:#010b}'.format(255))
print('oct: {:#010o}'.format(255))
print('dec: {:#010d}'.format(255))
print('hex: {:#010x}'.format(255))
print('HEX: {:#010X}'.format(255))
# bin: 0b11111111
# oct: 0o00000377
# dec: 0000000255
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

print('{:.2}'.format(1.234))
print('{:.5}'.format(1.234))
print('{:.5f}'.format(1.234))
# 1.2
# 1.234
# 1.23400

print('{}'.format(0.0001234))
print('{}'.format(0.00001234))
# 0.0001234
# 1.234e-05

print('{}'.format(1234000000000000.0))
print('{}'.format(12340000000000000.0))
print('{}'.format(12340000000000000000000000))
# 1234000000000000.0
# 1.234e+16
# 12340000000000000000000000

print('{:e}'.format(0.0001234))
print('{:E}'.format(0.0001234))
# 1.234000e-04
# 1.234000E-04

print('{:.4e}'.format(0.0001234))
print('{:.2E}'.format(0.0001234))
# 1.2340e-04
# 1.23E-04

print('{:%}'.format(0.12345))
print('{:.2%}'.format(0.12345))
# 12.345000%
# 12.35%

print('{:%}'.format(10))
print('{:.2%}'.format(10))
# 1000.000000%
# 1000.00%
