s = '1234'

print(s.zfill(8))
# 00001234

print(type(s.zfill(8)))
# <class 'str'>

print(s.zfill(3))
# 1234

s = '-1234'
print(s.zfill(8))
# -0001234

s = '+1234'
print(s.zfill(8))
# +0001234

s = 'abcd'
print(s.zfill(8))
# 0000abcd

i = 1234

print(type(i))
# <class 'int'>

# print(i.zfill(8))
# AttributeError: 'int' object has no attribute 'zfill'

print(str(i).zfill(8))
# 00001234

s = '1234'

print(s.rjust(8, '0'))
# 00001234

print(s.center(8, '0'))
# 00123400

print(s.ljust(8, '0'))
# 12340000

s = '-1234'

print(s.rjust(8, '0'))
# 000-1234

print(s.center(8, '0'))
# 0-123400

print(s.ljust(8, '0'))
# -1234000

s = '1234'

print('Zero Padding: {:0>8}'.format(s))
# Zero Padding: 00001234

s = '-1234'

print('Zero Padding: {:0>8}'.format(s))
# Zero Padding: 000-1234

s = '-1234'

print('Zero Padding: {:08}'.format(int(s)))
# Zero Padding: -0001234

i = 255

print('Zero Padding: {:08}'.format(i))
# Zero Padding: 00000255

print('Zero Padding: {:08x}'.format(i))
# Zero Padding: 000000ff

i = -1234

print('Zero Padding: {:08}'.format(i))
# Zero Padding: -0001234

print(f'Zero Padding: {i:08}')
# Zero Padding: -0001234

i = 1234

print('Zero Padding: %08d' % i)
# Zero Padding: 00001234

i = -1234

print('Zero Padding: %08d' % i)
# Zero Padding: -0001234

s = '1234'

print('Zero Padding: %08s' % s)
# Zero Padding:     1234

print('Zero Padding: %08d' % int(s))
# Zero Padding: 00001234
