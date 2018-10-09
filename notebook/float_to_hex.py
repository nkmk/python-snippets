import struct
import sys

f_max = sys.float_info.max

print(f_max)
# 1.7976931348623157e+308

print(struct.pack('>d', f_max))
# b'\x7f\xef\xff\xff\xff\xff\xff\xff'

print(type(struct.pack('>d', f_max)))
# <class 'bytes'>

print(struct.pack('<d', f_max))
# b'\xff\xff\xff\xff\xff\xff\xef\x7f'

print(struct.unpack('>Q', struct.pack('>d', f_max)))
# (9218868437227405311,)

print(type(struct.unpack('>Q', struct.pack('>d', f_max))))
# <class 'tuple'>

print(struct.unpack('>Q', struct.pack('>d', f_max))[0])
# 9218868437227405311

print(type(struct.unpack('>Q', struct.pack('>d', f_max))[0]))
# <class 'int'>

print(struct.unpack('>d', struct.pack('>d', f_max))[0])
# 1.7976931348623157e+308

print(hex(struct.unpack('>Q', struct.pack('>d', f_max))[0]))
# 0x7fefffffffffffff

print(type(hex(struct.unpack('>Q', struct.pack('>d', f_max))[0])))
# <class 'str'>

def double_to_hex(f):
    return hex(struct.unpack('>Q', struct.pack('>d', f))[0])

print(double_to_hex(f_max))
# 0x7fefffffffffffff

print(double_to_hex(42.195))
# 0x404518f5c28f5c29

print(double_to_hex(1e500))
# 0x7ff0000000000000

print(double_to_hex(1e-500))
# 0x0

print(int(double_to_hex(f_max), 16))
# 9218868437227405311

print(bin(int(double_to_hex(f_max), 16)))
# 0b111111111101111111111111111111111111111111111111111111111111111

print(oct(int(double_to_hex(f_max), 16)))
# 0o777577777777777777777

def double_to_bin(f):
    return bin(struct.unpack('>Q', struct.pack('>d', f))[0])

def double_to_oct(f):
    return oct(struct.unpack('>Q', struct.pack('>d', f))[0])

print(double_to_bin(f_max))
# 0b111111111101111111111111111111111111111111111111111111111111111

print(double_to_oct(f_max))
# 0o777577777777777777777

def float_to_hex(f):
    return hex(struct.unpack('>I', struct.pack('>f', f))[0])

print(float_to_hex(42.195))
# 0x4228c7ae
