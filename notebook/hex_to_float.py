import struct
import binascii

f_max_s = '7fefffffffffffff'

print(binascii.unhexlify(f_max_s))
# b'\x7f\xef\xff\xff\xff\xff\xff\xff'

print(type(binascii.unhexlify(f_max_s)))
# <class 'bytes'>

print(struct.unpack('>d', binascii.unhexlify(f_max_s)))
# (1.7976931348623157e+308,)

print(struct.unpack('>d', binascii.unhexlify(f_max_s))[0])
# 1.7976931348623157e+308

print(type(struct.unpack('>d', binascii.unhexlify(f_max_s))[0]))
# <class 'float'>

def hex_to_double(s):
    if s.startswith('0x'):
        s = s[2:]
    s = s.replace(' ', '')
    return struct.unpack('>d', binascii.unhexlify(s))[0]

print(hex_to_double('7fefffffffffffff'))
# 1.7976931348623157e+308

print(hex_to_double('0x7fefffffffffffff'))
# 1.7976931348623157e+308

print(hex_to_double('0x7fef ffff ffff ffff'))
# 1.7976931348623157e+308

print(hex_to_double('0x4045 18f5 c28f 5c29'))
# 42.195

print(hex_to_double('7ff0000000000000'))
# inf

print(hex_to_double('7ff0000000000001'))
# nan

print(hex_to_double('0000000000000001'))
# 5e-324

# print(hex_to_double('ffff ffff ffff ffff ff'))
# error: unpack requires a buffer of 8 bytes

# print(hex_to_double('ffff ffff ffff ff'))
# error: unpack requires a buffer of 8 bytes

def hex_to_float(s):
    if s.startswith('0x'):
        s = s[2:]
    s = s.replace(' ', '')
    return struct.unpack('>f', binascii.unhexlify(s))[0]

print(hex_to_float('0x4228c7ae'))
# 42.19499969482422
