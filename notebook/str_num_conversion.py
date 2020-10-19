print(int('100'))
print(type(int('100')))
# 100
# <class 'int'>

# print(int('1.23'))
# ValueError: invalid literal for int() with base 10: '1.23'

# print(int('10,000'))
# ValueError: invalid literal for int() with base 10: '10,000'

print(int('10,000'.replace(',', '')))
# 10000

print(float('1.23'))
print(type(float('1.23')))
# 1.23
# <class 'float'>

print(float('.23'))
# 0.23

print(float('100'))
print(type(float('100')))
# 100.0
# <class 'float'>

print(int('100', 2))
print(int('100', 8))
print(int('100', 16))
# 4
# 64
# 256

print(int('100', 10))
print(int('100'))
# 100
# 100

print(int('0b100', 0))
print(int('0o100', 0))
print(int('0x100', 0))
# 4
# 64
# 256

print(int('FF', 16))
print(int('ff', 16))
# 255
# 255

print(int('0xFF', 0))
print(int('0XFF', 0))
print(int('0xff', 0))
print(int('0Xff', 0))
# 255
# 255
# 255
# 255

print(float('1.23e-4'))
print(type(float('1.23e-4')))
# 0.000123
# <class 'float'>

print(float('1.23e4'))
print(type(float('1.23e4')))
# 12300.0
# <class 'float'>

print(float('1.23E-4'))
# 0.000123

print(int('１００'))
print(type(int('１００')))
# 100
# <class 'int'>

print(float('１００'))
print(type(float('１００')))
# 100.0
# <class 'float'>

# print(float('ー１．２３'))
# ValueError: could not convert string to float: '１．２３'

print(float('-１.２３'))
# -1.23

print(float('ー１．２３'.replace('ー', '-').replace('．', '.')))
# -1.23
