# https://docs.python.jp/3/library/string.html#format-string-syntax
# https://docs.python.jp/3/library/string.html#formatspec
# https://docs.python.jp/3/library/string.html#format-examples

print('{0}'.format('foo'))
# foo

print('{}'.format('foo'))
# foo

print('{}, {}, {}'.format('one', 'two', 'three'))
# one, two, three

print('{0}, {1}, {0}'.format('foo', 'bar'))
# foo, bar, foo

print('{word1}, {word2}, {word1}'.format(word1='one', word2='two'))
# one, two, one

person = {'name': 'ALice', 'age': 20}
print('{0[name]} is {0[age]} years old.'.format(person))
# ALice is 20 years old.

i = 100
print('left  : {:<10}'.format(i))
print('center: {:^10}'.format(i))
print('right : {:>10}'.format(i))
# left  : 100       
# center:    100    
# right :        100

i = 100
print('left  : {:*<10}'.format(i))
print('center: {:*^10}'.format(i))
print('right : {:*>10}'.format(i))
# left  : 100*******
# center: ***100****
# right : *******100

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

i = 255
print('bin: {:0>8b}'.format(i))
print('oct: {:0>8o}'.format(i))
print('dec: {:0>8d}'.format(i))
print('hex: {:0>8x}'.format(i))
print('HEX: {:0>8X}'.format(i))
# bin: 11111111
# oct: 00000377
# dec: 00000255
# hex: 000000ff
# HEX: 000000FF

i = 100000000
print('{:,}'.format(i))
# 100,000,000

ratio = 0.4567
print('{:.2}'.format(ratio))
print('{:.5}'.format(ratio))
print('{:.5f}'.format(ratio))
print('{:%}'.format(ratio))
print('{:.1%}'.format(ratio))
# 0.46
# 0.4567
# 0.45670
# 45.670000%
# 45.7%
