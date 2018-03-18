t = (0, 1, 2)

a, b, c = t

print(a)
print(b)
print(c)
# 0
# 1
# 2

l = [0, 1, 2]

a, b, c = l

print(a)
print(b)
print(c)
# 0
# 1
# 2

a, b = 0, 1

print(a)
print(b)
# 0
# 1

# a, b = t
# ValueError: too many values to unpack (expected 2)

# a, b, c, d = t
# ValueError: not enough values to unpack (expected 4, got 3)

t = (0, 1, (2, 3, 4))

a, b, c = t

print(a)
print(b)
print(c)
# 0
# 1
# (2, 3, 4)

print(type(c))
# <class 'tuple'>

a, b, (c, d, e) = t

print(a)
print(b)
print(c)
print(d)
print(e)
# 0
# 1
# 2
# 3
# 4

t = (0, 1, 2)

a, b, _ = t

print(a)
print(b)
print(_)
# 0
# 1
# 2

t = (0, 1, 2, 3, 4)

a, b, *c = t

print(a)
print(b)
print(c)
# 0
# 1
# [2, 3, 4]

print(type(c))
# <class 'list'>

a, *b, c = t

print(a)
print(b)
print(c)
# 0
# [1, 2, 3]
# 4

*a, b, c = t

print(a)
print(b)
print(c)
# [0, 1, 2]
# 3
# 4

a, b, *_ = t

print(a)
print(b)
print(_)
# 0
# 1
# [2, 3, 4]

a, b = t[0], t[1]

print(a)
print(b)
# 0
# 1

# *a, b, *c = t
# SyntaxError: two starred expressions in assignment

t = (0, 1, 2)

a, b, *c = t

print(a)
print(b)
print(c)
# 0
# 1
# [2]

print(type(c))
# <class 'list'>

a, b, c, *d = t

print(a)
print(b)
print(c)
print(d)
# 0
# 1
# 2
# []
