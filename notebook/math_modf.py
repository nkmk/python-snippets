import math

print(math.modf(1.5))
print(type(math.modf(1.5)))
# (0.5, 1.0)
# <class 'tuple'>

f, i = math.modf(1.5)

print(i)
print(f)
# 1.0
# 0.5

print(type(i))
print(type(f))
# <class 'float'>
# <class 'float'>

f, i = math.modf(-1.5)

print(i)
print(f)
# -1.0
# -0.5

f, i = math.modf(100)

print(i)
print(f)
# 100.0
# 0.0

a = 1.5

i = int(a)
f = a - int(a)

print(i)
print(f)
# 1
# 0.5

print(type(i))
print(type(f))
# <class 'int'>
# <class 'float'>
