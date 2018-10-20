print(type(True))
# <class 'bool'>

print(type(False))
# <class 'bool'>

print(issubclass(bool, int))
# True

print(True == 1)
# True

print(False == 0)
# True

print(True + True)
# 2

print(True * 10)
# 10

print(sum([True, False, True]))
# 2

l = [0, 1, 2, 3, 4]

print([i > 2 for i in l])
# [False, False, False, True, True]

print(sum(i > 2 for i in l))
# 2

if 'abc':
    print('True!')
# True!

print(int(True))
print(int(False))
# 1
# 0

print(float(True))
print(float(False))
# 1.0
# 0.0

print(complex(True))
print(complex(False))
# (1+0j)
# 0j

print(str(True))
print(str(False))
# True
# False

print(type(str(True)))
print(type(str(False)))
# <class 'str'>
# <class 'str'>

print(bool(str(False)))
# True

# print(list(True))
# TypeError: 'bool' object is not iterable
