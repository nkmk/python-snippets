bin_num = 0b10
oct_num = 0o10
hex_num = 0x10

print(bin_num)
print(oct_num)
print(hex_num)
# 2
# 8
# 16

Bin_num = 0B10
Oct_num = 0O10
Hex_num = 0X10

print(Bin_num)
print(Oct_num)
print(Hex_num)
# 2
# 8
# 16

print(type(bin_num))
print(type(oct_num))
print(type(hex_num))
# <class 'int'>
# <class 'int'>
# <class 'int'>

print(type(Bin_num))
print(type(Oct_num))
print(type(Hex_num))
# <class 'int'>
# <class 'int'>
# <class 'int'>

result = 0b10 * 0o10 + 0x10
print(result)
# 32

print(0b111111111111 == 0b1_1_1_1_1_1_1_1_1_1_1_1)
# True

bin_num = 0b1111_1111_1111
print(bin_num)
# 4095

i = 255

print(bin(i))
print(oct(i))
print(hex(i))
# 0b11111111
# 0o377
# 0xff

print(type(bin(i)))
print(type(oct(i)))
print(type(hex(i)))
# <class 'str'>
# <class 'str'>
# <class 'str'>

print(bin(i)[2:])
print(oct(i)[2:])
print(hex(i)[2:])
# 11111111
# 377
# ff

print(str(i))
# 255

print(type(str(i)))
# <class 'str'>

print(format(i, 'b'))
print(format(i, 'o'))
print(format(i, 'x'))
# 11111111
# 377
# ff

print(type(format(i, 'b')))
print(type(format(i, 'o')))
print(type(format(i, 'x')))
# <class 'str'>
# <class 'str'>
# <class 'str'>

print(format(i, '#b'))
print(format(i, '#o'))
print(format(i, '#x'))
# 0b11111111
# 0o377
# 0xff

print(format(i, '08b'))
print(format(i, '08o'))
print(format(i, '08x'))
# 11111111
# 00000377
# 000000ff

print(format(i, '#010b'))
print(format(i, '#010o'))
print(format(i, '#010x'))
# 0b11111111
# 0o00000377
# 0x000000ff

print('{:08b}'.format(i))
print('{:08o}'.format(i))
print('{:08x}'.format(i))
# 11111111
# 00000377
# 000000ff

print(f'{i:08b}')
print(f'{i:08o}')
print(f'{i:08x}')
# 11111111
# 00000377
# 000000ff

print(int('10'))
print(int('10', 2))
print(int('10', 8))
print(int('10', 16))
# 10
# 2
# 8
# 16

print(type(int('10')))
print(type(int('10', 2)))
print(type(int('10', 8)))
print(type(int('10', 16)))
# <class 'int'>
# <class 'int'>
# <class 'int'>
# <class 'int'>

print(int('0b10', 0))
print(int('0o10', 0))
print(int('0x10', 0))
# 2
# 8
# 16

print(int('0B10', 0))
print(int('0O10', 0))
print(int('0X10', 0))
# 2
# 8
# 16

print(int('10', 0))
# 10

# print(int('010', 0))
# ValueError: invalid literal for int() with base 0: '010'

print(int('010'))
# 10

print(int('00ff', 16))
print(int('0x00ff', 0))
# 255
# 255

# print(int('ff', 2))
# ValueError: invalid literal for int() with base 2: 'ff'

# print(int('0a10', 0))
# ValueError: invalid literal for int() with base 0: '0a10'

# print(int('0bff', 0))
# ValueError: invalid literal for int() with base 0: '0bff'

a = '0b1001'
b = '0b0011'

c = int(a, 0) + int(b, 0)

print(c)
print(bin(c))
# 12
# 0b1100

a_0b = '0b1110001010011'

print(format(int(a, 0), '#010x'))
# 0x00000009

print(format(int(a, 0), '#010o'))
# 0o00000011
