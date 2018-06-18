i = 100

s_i = str(i)
print(s_i)
# 100

print(type(s_i))
# <class 'str'>

f = 0.123

s_f = str(f)
print(s_f)
# 0.123

print(type(s_f))
# <class 'str'>

i = 0xFF
print(i)
# 255

s_i = str(i)
print(s_i)
# 255

f = 1.23e+10
print(f)
# 12300000000.0

s_f = str(f)
print(s_f)
# 12300000000.0

s_i_format = format(i, '#X')
print(s_i_format)
# 0XFF

s_f_format = format(f, '.2e')
print(s_f_format)
# 1.23e+10

l = [0, 1, 2]

s_l = str(l)
print(s_l)
# [0, 1, 2]

print(type(s_l))
# <class 'str'>

d = {'a': 1,
     'b': 2,
     'c': 3}

s_d = str(d)

print(s_d)
# {'a': 1, 'b': 2, 'c': 3}

print(type(s_d))
# <class 'str'>

import pprint

dl = {'a': 1, 'b': 2, 'c': [100, 200, 300]}

s_dl = str(dl)
print(s_dl)
# {'a': 1, 'b': 2, 'c': [100, 200, 300]}

p_dl = pprint.pformat(dl, width=10)
print(p_dl)
# {'a': 1,
#  'b': 2,
#  'c': [100,
#        200,
#        300]}

print(type(p_dl))
# <class 'str'>
