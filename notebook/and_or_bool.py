x = True
y = False

print(x and y)
# False

print(x or y)
# True

print(not x)
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
