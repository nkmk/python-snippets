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

print(int('101', 2))
print(int('70', 8))
print(int('FF', 16))
# 5
# 56
# 255

print(int('0b101', 0))
print(int('0o70', 0))
print(int('0xFF', 0))
# 5
# 56
# 255

print(float('1.23e-4'))
print(type(float('1.23e-4')))
# 0.000123
# <class 'float'>

print(float('1.23e4'))
print(type(float('1.23e4')))
# 12300.0
# <class 'float'>

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
