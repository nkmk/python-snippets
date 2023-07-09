l1 = [1, 2, 3]
l2 = [10, 20, 30]

t1 = (1, 2, 3)
t2 = (10, 20, 30)

s1 = 'abc'
s2 = 'xyz'

print(l1 + l2)
# [1, 2, 3, 10, 20, 30]

print(t1 + t2)
# (1, 2, 3, 10, 20, 30)

print(s1 + s2)
# abcxyz

# print(l1 + 4)
# TypeError: can only concatenate list (not "int") to list

print(l1 + [4])
# [1, 2, 3, 4]

# print(t1 + 4)
# TypeError: can only concatenate tuple (not "int") to tuple

print(t1 + (4,))
# (1, 2, 3, 4)

l1 += l2
print(l1)
# [1, 2, 3, 10, 20, 30]

t1 += t2
print(t1)
# (1, 2, 3, 10, 20, 30)

s1 += s2
print(s1)
# abcxyz

l = [1, 10, 100]
t = (1, 10, 100)
s = 'Abc'

print(l * 3)
# [1, 10, 100, 1, 10, 100, 1, 10, 100]

print(t * 3)
# (1, 10, 100, 1, 10, 100, 1, 10, 100)

print(s * 3)
# AbcAbcAbc

print(3 * l)
# [1, 10, 100, 1, 10, 100, 1, 10, 100]

# print(l * 0.5)
# TypeError: can't multiply sequence by non-int of type 'float'

print(l * -1)
# []

l *= 3
print(l)
# [1, 10, 100, 1, 10, 100, 1, 10, 100]

t *= 3
print(t)
# (1, 10, 100, 1, 10, 100, 1, 10, 100)

s *= 3
print(s)
# AbcAbcAbc

l1 = [1, 2, 3]
l2 = [10, 20, 30]
print(l1 + l2 * 2)
# [1, 2, 3, 10, 20, 30, 10, 20, 30]

print((l1 + l2) * 2)
# [1, 2, 3, 10, 20, 30, 1, 2, 3, 10, 20, 30]
