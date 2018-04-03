for i in range(3):
    print(i)
# 0
# 1
# 2

print(range(3))
print(type(range(3)))
# range(0, 3)
# <class 'range'>

print(list(range(3)))
# [0, 1, 2]

print(list(range(6)))
# [0, 1, 2, 3, 4, 5]

print(list(range(10, 13)))
# [10, 11, 12]

print(list(range(0, 10, 3)))
# [0, 3, 6, 9]

print(list(range(10, 0, -3)))
# [10, 7, 4, 1]

for i in range(10, 0, -3):
    print(i)
# 10
# 7
# 4
# 1
