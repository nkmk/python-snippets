s = 'abc'

s_rjust = s.rjust(8)

print(s_rjust)
#      abc

print(type(s_rjust))
# <class 'str'>

print(s.rjust(2))
# abc

print(s.rjust(8, '+'))
# +++++abc

print(s.rjust(8, '漢'))
# 漢漢漢漢漢abc

# print(s.rjust(8, 'xyz'))
# TypeError: The fill character must be exactly one character long

s_n = '-123'

print(s_n.rjust(8, '0'))
# 0000-123

print(s_n.zfill(8))
# -0000123

s = 'abc'

print(s.center(8))
#   abc   

print(s.center(8, '+'))
# ++abc+++

print(s.center(9, '+'))
# +++abc+++

print(s.center(10, '+'))
# +++abc++++

s = 'abc'

print(s.ljust(8))
# abc     

print(s.ljust(8, '+'))
# abc+++++

n = 123

print(type(n))
# <class 'int'>

print(str(n).rjust(8, '@'))
# @@@@@123

print(str(n).center(8, '@'))
# @@123@@@

print(str(n).ljust(8, '@'))
# 123@@@@@

s = 'abc'

print('right : {:@>8}'.format(s))
# right : @@@@@abc

print('center: {:@^8}'.format(s))
# center: @@abc@@@

print('left  : {:@<8}'.format(s))
# left  : abc@@@@@

n = 255

print('right : {:08}'.format(n))
# right : 00000255

print('right : {:08x}'.format(n))
# right : 000000ff

print(f'right : {n:08}')
# right : 00000255

print(f'right : {n:08x}')
# right : 000000ff
