print(0.1 + 0.1 + 0.1)
# 0.30000000000000004

print(1 / 3)
# 0.3333333333333333

f = 987.6543
print(f)
# 987.6543

print(type(f))
# <class 'float'>

s = str(f)
print(s)
# 987.6543

print(type(s))
# <class 'str'>

f = 987.6543
s = str(f)

print(s.split('.'))
# ['987', '6543']

print(type(s.split('.')))
# <class 'list'>

print(type(s.split('.')[0]))
# <class 'str'>

s_i, s_d = s.split('.')

print(s_i)
# 987

print(s_d)
# 6543

f = 987.6543
s = str(f)
s_i, s_d = s.split('.')

print(len(s_i))
# 3

print(len(s_d))
# 4

print(len(str(f).split('.')[0]))
# 3

print(len(str(f).split('.')[1]))
# 4

f = 0.123

print(str(f).split('.'))
# ['0', '123']

print(len(str(f).split('.')[0]))
# 1

print(str(f).strip('0').split('.'))
# ['', '123']

print(len(str(f).strip('0').split('.')[0]))
# 0

f = 987.6543
s = str(f)
s_i, s_d = s.split('.')

print(s_i[-1])
# 7

print(s_i[-3])
# 9

print(s_d[0])
# 6

print(s_d[3])
# 3

print(type(s_d[3]))
# <class 'str'>

print(int(s_d[3]))
# 3

print(type(int(s_d[3])))
# <class 'int'>

print(str(f).split('.')[0][-3])
# 9

print(int(str(f).split('.')[0][-3]))
# 9

print(str(f).split('.')[1][3])
# 3

print(int(str(f).split('.')[1][3]))
# 3

print(str(0.0001))
# 0.0001

print(str(0.00001))
# 1e-05

s_format = format(0.00001, '.8f')
print(s_format)
# 0.00001000

print(type(s_format))
# <class 'str'>

print('{:.8f}'.format(0.00001))
# 0.00001000

print(f'{0.00001:.8f}')
# 0.00001000

s_rstrip = s_format.rstrip('0')
print(s_rstrip)
# 0.00001

print(format(0.1, '.8f').rstrip('0'))
# 0.1

print(format(0.0001, '.8f').rstrip('0'))
# 0.0001

print(format(0.00000001, '.8f').rstrip('0'))
# 0.00000001

print(format(0.000000001, '.8f').rstrip('0'))
# 0.

print(format(0.00001, '.8f').strip('0'))
# .00001

s_i, s_d = format(0.00001, '.8f').strip('0').split('.')

print(s_i)
# 

print(type(s_i))
# <class 'str'>

print(len(s_i))
# 0

print(s_d)
# 00001

s_i, s_d = format(1.00001, '.8f').strip('0').split('.')

print(s_i)
# 1

print(s_d)
# 00001
