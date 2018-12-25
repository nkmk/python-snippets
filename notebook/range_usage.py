# print(xrange(3))
# NameError: name 'xrange' is not defined

print(range(3))
# range(0, 3)

print(type(range(3)))
# <class 'range'>

for i in range(3):
    print(i)
# 0
# 1
# 2

print(list(range(3)))
# [0, 1, 2]

print(list(range(10)))
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(list(range(-3)))
# []

print(list(range(3, 10)))
# [3, 4, 5, 6, 7, 8, 9]

print(list(range(10, 3)))
# []

print(list(range(-3, 3)))
# [-3, -2, -1, 0, 1, 2]

print(list(range(3, -3)))
# []

print(range(0, 3) == range(3))
# True

print(list(range(3, 10, 2)))
# [3, 5, 7, 9]

print(list(range(10, 3, 2)))
# []

print(list(range(10, 3, -2)))
# [10, 8, 6, 4]

print(list(range(3, 10, -2)))
# []

print(range(3, 10, 1) == range(3, 10))
# True

print(range(0, 10, 1) == range(0, 10) == range(10))
# True

print(list(range(3, 10, 2)))
# [3, 5, 7, 9]

print(list(range(9, 2, -2)))
# [9, 7, 5, 3]

print(list(reversed(range(3, 10, 2))))
# [9, 7, 5, 3]

for i in reversed(range(3, 10, 2)):
    print(i)
# 9
# 7
# 5
# 3

# print(list(range(0.3, 1.0, 0.2)))
# TypeError: 'float' object cannot be interpreted as an integer

print([i / 10 for i in range(3, 10, 2)])
# [0.3, 0.5, 0.7, 0.9]

print([i * 0.1 for i in range(3, 10, 2)])
# [0.30000000000000004, 0.5, 0.7000000000000001, 0.9]

print([round(i * 0.1, 1) for i in range(3, 10, 2)])
# [0.3, 0.5, 0.7, 0.9]
