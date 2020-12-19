print(True and True)
# True

print(True and False)
# False

print(False and True)
# False

print(False and False)
# False

a = 10
print(0 < a)
# True

print(a < 100)
# True

print(0 < a and a < 100)
# True

print(0 < a < 100)
# True

print(True or True)
# True

print(True or False)
# True

print(False or True)
# True

print(False or False)
# False

print(not True)
# False

print(not False)
# True

print(True or True and False)
# True

print(True or (True and False))
# True

print((True or True) and False)
# False

print(bool(10))
# True

print(bool(0))
# False

print(bool(''))
# False

print(bool('0'))
# True

print(bool('False'))
# True

print(bool([]))
# False

print(bool([False]))
# True

x = 10  # True
y = 0  # False

print(x and y)
# 0

print(x or y)
# 10

print(not x)
# False

x = 10  # True
y = 100  # True

print(x and y)
# 100

print(y and x)
# 10

print(x or y)
# 10

print(y or x)
# 100

x = 0  # False
y = 0.0  # False

print(x and y)
# 0

print(y and x)
# 0.0

print(x or y)
# 0.0

print(y or x)
# 0

print(bool(x and y))
# False
