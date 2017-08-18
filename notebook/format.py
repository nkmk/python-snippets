# https://docs.python.jp/3/library/string.html#format-string-syntax
# https://docs.python.jp/3/library/string.html#formatspec
# https://docs.python.jp/3/library/string.html#format-examples

print('{}'.format('foo'))
# foo

print('{}, {}, {}'.format('one', 'two', 'three'))
# one, two, three

print('{0}, {1}, {0}'.format('foo', 'bar'))
# foo, bar, foo

print('{word1}, {word2}, {word1}'.format(word1='one', word2='two'))
# one, two, one

person1 = {'name': 'Alice', 'age': 20}
person2 = {'name': 'Bob', 'age': 30}
print('{0[name]} is {0[age]} years old. {1[name]} is {1[age]} years old.'.format(person1, person2))
# Alice is 20 years old. Bob is 30 years old.

print('{number:0>5}'.format(number=123))
# 00123

i = 100
print('left  : {:<10}'.format(i))
print('center: {:^10}'.format(i))
print('right : {:>10}'.format(i))
# left  : 100       
# center:    100    
# right :        100

print('left  : {:*<10}'.format(i))
print('center: {:*^10}'.format(i))
print('right : {:*>10}'.format(i))
# left  : 100*******
# center: ***100****
# right : *******100

print('zero padding 1: {:0>10}'.format(i))
print('zero padding 2: {:010}'.format(i))
# zero padding 1: 0000000100
# zero padding 2: 0000000100

i = 255
print('bin: {:b}'.format(i))
print('oct: {:o}'.format(i))
print('dec: {:d}'.format(i))
print('hex: {:x}'.format(i))
print('HEX: {:X}'.format(i))
# bin: 11111111
# oct: 377
# dec: 255
# hex: ff
# HEX: FF

print('bin: {:08b}'.format(i))
print('oct: {:08o}'.format(i))
print('dec: {:08d}'.format(i))
print('hex: {:08x}'.format(i))
print('HEX: {:08X}'.format(i))
# bin: 11111111
# oct: 00000377
# dec: 00000255
# hex: 000000ff
# HEX: 000000FF

i = 100000000
print('{:,}'.format(i))
# 100,000,000

print('{:e}'.format(i))
print('{:E}'.format(i))
# 1.000000e+08
# 1.000000E+08

ratio = 0.4567
print('{:.2}'.format(ratio))
print('{:.5}'.format(ratio))
print('{:.5f}'.format(ratio))
# 0.46
# 0.4567
# 0.45670

print('{:%}'.format(ratio))
print('{:.1%}'.format(ratio))
# 45.670000%
# 45.7%
