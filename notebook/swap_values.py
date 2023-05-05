a = 1
b = 2

a, b = b, a

print(f'{a = }')
print(f'{b = }')
# a = 2
# b = 1

a, b = 100, 200

print(f'{a = }')
print(f'{b = }')
# a = 100
# b = 200

a, b, c, d = 0, 1, 2, 3

a, b, c, d = d, c, b, a

print(f'{a = }')
print(f'{b = }')
print(f'{c = }')
print(f'{d = }')
# a = 3
# b = 2
# c = 1
# d = 0

l = [0, 1, 2, 3, 4]

l[0], l[3] = l[3], l[0]

print(l)
# [3, 1, 2, 0, 4]

print(sorted(l))
# [0, 1, 2, 3, 4]

print(sorted(l, reverse=True))
# [4, 3, 2, 1, 0]
