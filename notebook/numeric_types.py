binary = 0b100
octal = 0o100
hexadecimal = 0x100
print(binary, type(binary))
print(octal, type(octal))
print(hexadecimal, type(hexadecimal))
# 4 <class 'int'>
# 64 <class 'int'>
# 256 <class 'int'>

# number to string
i = 100
print(bin(i), type(bin(i)))
print(oct(i), type(oct(i)))
print(hex(i), type(hex(i)))
# 0b1100100 <class 'str'>
# 0o144 <class 'str'>
# 0x64 <class 'str'>

# string to number
print(int('100', 2))
print(int('100', 8))
print(int('100', 16))
print(int('100'))
# 4
# 64
# 256
# 100

print(int('0b100', 0))
print(int('0o100', 0))
print(int('0x100', 0))
print(int('100', 0))
# 4
# 64
# 256
# 100
