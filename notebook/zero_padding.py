s = '1234'

s_zero = s.zfill(8)
print(s_zero)
# 00001234

print(type(s_zero))
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

n = 1234

print(type(n))
# <class 'int'>

# print(n.zfill(8))
# AttributeError: 'int' object has no attribute 'zfill'

print(str(n).zfill(8))
# 00001234

s = '1234'

print(s.rjust(8, '0'))
# 00001234

print(s.ljust(8, '0'))
# 12340000

print(s.center(8, '0'))
# 00123400

s = '-1234'

print(s.rjust(8, '0'))
# 000-1234

print(s.ljust(8, '0'))
# -1234000

print(s.center(8, '0'))
# 0-123400

s = '1234'

print(format(s, '0>8'))
# 00001234

print('Zero Padding: {:0>8}'.format(s))
# Zero Padding: 00001234

s = '-1234'

print(format(s, '0>8'))
# 000-1234

print('Zero Padding: {:0>8}'.format(s))
# Zero Padding: 000-1234

print(format(int(s), '08'))
# -0001234

print('Zero Padding: {:0>8}'.format(int(s)))
# Zero Padding: 000-1234

n = 1234

print(format(n, '08'))
# 00001234

print('Zero Padding: {:08}'.format(n))
# Zero Padding: 00001234

print(format(n, '08x'))
# 000004d2

print('Zero Padding: {:08x}'.format(n))
# Zero Padding: 000004d2

n = -1234

print(format(n, '08'))
# -0001234

print('Zero Padding: {:08}'.format(n))
# Zero Padding: -0001234

print(f'Zero Padding: {n:08}')
# Zero Padding: -0001234

n = 1234

print('Zero Padding: %08d' % n)
# Zero Padding: 00001234

n = -1234

print('Zero Padding: %08d' % n)
# Zero Padding: -0001234

s = '1234'

print('Zero Padding: %08s' % s)
# Zero Padding:     1234

print('Zero Padding: %08d' % int(s))
# Zero Padding: 00001234
