x = -9

print(x)
print(bin(x))
# -9
# -0b1001

print(bin(x & 0xff))
print(format(x & 0xffff, 'x'))
# 0b11110111
# fff7

x = 9   # 0b1001
y = 10  # 0b1010

print(x & y)
print(bin(x & y))
# 8
# 0b1000

print(x | y)
print(bin(x | y))
# 11
# 0b1011

print(x ^ y)
print(bin(x ^ y))
# 3
# 0b11

x = 9  # 0b1001

print(~x)
print(bin(~x))
# -10
# -0b1010

print(bin(~x & 0xff))
print(format(~x & 0b1111, '04b'))
# 0b11110110
# 0110

x = 9  # 0b1001

print(x << 1)
print(bin(x << 1))
# 18
# 0b10010

print(x >> 1)
print(bin(x >> 1))
# 4
# 0b100

x = -9
print(bin(x))
print(bin(x & 0xff))
# -0b1001
# 0b11110111

print(x << 1)
print(bin(x << 1))
print(bin((x << 1) & 0xff))
# -18
# -0b10010
# 0b11101110

print(x >> 1)
print(bin(x >> 1))
print(bin((x >> 1) & 0xff))
# -5
# -0b101
# 0b11111011
