a = 100
b = 200

print(a)
# 100

print(b)
# 200

a, b = 100, 200

print(a)
# 100

print(b)
# 200

a, b, c = 0.1, 100, 'string'

print(a)
# 0.1

print(b)
# 100

print(c)
# string

a = 100, 200

print(a)
print(type(a))
# (100, 200)
# <class 'tuple'>

# a, b = 100, 200, 300
# ValueError: too many values to unpack (expected 2)

# a, b, c = 100, 200
# ValueError: not enough values to unpack (expected 3, got 2)

a, *b = 100, 200, 300

print(a)
print(type(a))
# 100
# <class 'int'>

print(b)
print(type(b))
# [200, 300]
# <class 'list'>

*a, b = 100, 200, 300

print(a)
print(type(a))
# [100, 200]
# <class 'list'>

print(b)
print(type(b))
# 300
# <class 'int'>

a = b = 100

print(a)
# 100

print(b)
# 100

a = 200

print(a)
# 200

print(b)
# 100

a = b = c = 'string'

print(a)
# string

print(b)
# string

print(c)
# string

a = b = [0, 1, 2]

print(a is b)
# True

a[0] = 100
print(a)
# [100, 1, 2]

print(b)
# [100, 1, 2]

b = [0, 1, 2]
a = b

print(a is b)
# True

a[0] = 100
print(a)
# [100, 1, 2]

print(b)
# [100, 1, 2]

a = [0, 1, 2]
b = [0, 1, 2]

print(a is b)
# False

a[0] = 100
print(a)
# [100, 1, 2]

print(b)
# [0, 1, 2]
