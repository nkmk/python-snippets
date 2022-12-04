s = 'abc'

print(s.rjust(8))
#      abc

print(type(s.rjust(8)))
# <class 'str'>

print(s.rjust(2))
# abc

print(s.rjust(8, '*'))
# *****abc

# print(s.rjust(8, 'ab'))
# TypeError: The fill character must be exactly one character long

s = '-123'

print(s.rjust(8, '0'))
# 0000-123

print(s.zfill(8))
# -0000123

s = 'abc'

print(s.center(8))
#   abc   

print(s.center(8, '*'))
# **abc***

print(s.center(9, '*'))
# ***abc***

print(s.center(10, '*'))
# ***abc****

s = 'abc'

print(s.ljust(8))
# abc     

print(s.ljust(8, '*'))
# abc*****

i = 123

print(type(i))
# <class 'int'>

print(str(i).rjust(8, '*'))
# *****123

print(str(i).center(8, '*'))
# **123***

print(str(i).ljust(8, '*'))
# 123*****

s = 'abc'

print('right : {:*>8}'.format(s))
# right : *****abc

print('center: {:*^8}'.format(s))
# center: **abc***

print('left  : {:*<8}'.format(s))
# left  : abc*****

i = 255

print('right : {:08}'.format(i))
# right : 00000255

print('right : {:08x}'.format(i))
# right : 000000ff

print(f'right : {i:08}')
# right : 00000255

print(f'right : {i:08x}')
# right : 000000ff
