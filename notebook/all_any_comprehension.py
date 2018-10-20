l = [0, 1, 2, 3, 4]

print([i > 2 for i in l])
# [False, False, False, True, True]

print(all([i > 2 for i in l]))
# False

print(any([i > 2 for i in l]))
# True

print(type([i > 2 for i in l]))
# <class 'list'>

print(type((i > 2 for i in l)))
# <class 'generator'>

print(type(i > 2 for i in l))
# <class 'generator'>

print(all(i > 2 for i in l))
# False

print(any(i > 2 for i in l))
# True

print(sum(i > 2 for i in l))
# 2

print(sum(not (i > 2) for i in l))
# 3
