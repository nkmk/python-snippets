i = 100
print(bin(i))
# 0b1100100

print(i.bit_count())
# 3

i = 255
print(bin(i))
# 0b11111111

print(i.bit_count())
# 8

i = -100
print(bin(i))
# -0b1100100

print(i.bit_count())
# 3

i = -255
print(bin(i))
# -0b11111111

print(i.bit_count())
# 8

def bit_count(self):
    return bin(self).count("1")

print(bit_count(100))
# 3

print(bit_count(255))
# 8

print(bit_count(-100))
# 3

print(bit_count(-255))
# 8
