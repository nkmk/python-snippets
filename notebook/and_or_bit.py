x = 12  # 0b1100
y = 10  # 0b1010

print(x & y)
print(bin(x & y))
# 8
# 0b1000

x = 12  # 0b1100
y = 10  # 0b1010

print(x | y)
print(bin(x | y))
# 14
# 0b1110

x = 12  # 0b1100
y = 10  # 0b1010

print(x ^ y)
print(bin(x ^ y))
# 6
# 0b110

x = -9

print(x)
print(bin(x))
# -9
# -0b1001

print(bin(x & 0xFF))
print(format(x & 0xFF, 'b'))
# 0b11110111
# 11110111

print(bin(x & 0b1111))
print(format(x & 0b1111, 'b'))
# 0b111
# 111

print(format(x & 0b1111, '#06b'))
print(format(x & 0b1111, '04b'))
# 0b0111
# 0111

x = 9  # 0b1001

print(~x)
print(bin(~x))
# -10
# -0b1010

print(bin(~x & 0xFF))
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
print(bin(x & 0xFF))
# -0b1001
# 0b11110111

print(x << 1)
print(bin(x << 1))
print(bin((x << 1) & 0xFF))
# -18
# -0b10010
# 0b11101110

print(x >> 1)
print(bin(x >> 1))
print(bin((x >> 1) & 0xFF))
# -5
# -0b101
# 0b11111011
