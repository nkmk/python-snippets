a = 1
b = 2

a, b = b, a

print('a = ', a)
print('b = ', b)
# a =  2
# b =  1

a, b = 100, 200

print('a = ', a)
print('b = ', b)
# a =  100
# b =  200

a, b, c, d = 0, 1, 2, 3

a, b, c, d = c, d, a, b

print('a = ', a)
print('b = ', b)
print('c = ', c)
print('d = ', d)
# a =  2
# b =  3
# c =  0
# d =  1

l = [0, 1, 2, 3, 4]

l[0], l[3] = l[3], l[0]

print(l)
# [3, 1, 2, 0, 4]

print(sorted(l))
# [0, 1, 2, 3, 4]

print(sorted(l, reverse=True))
# [4, 3, 2, 1, 0]
