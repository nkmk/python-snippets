import itertools

sum_value = 0

for i in itertools.repeat(10):
    print(i)
    sum_value += i
    if sum_value > 40:
        break
# 10
# 10
# 10
# 10
# 10

for i in itertools.repeat(10, 3):
    print(i)
# 10
# 10
# 10

for l in itertools.repeat([0, 1, 2], 3):
    print(l)
# [0, 1, 2]
# [0, 1, 2]
# [0, 1, 2]

for func in itertools.repeat(len, 3):
    print(func('abc'))
# 3
# 3
# 3

l = [0, 1, 2, 3]

print(list(zip(itertools.repeat(10), l)))
# [(10, 0), (10, 1), (10, 2), (10, 3)]
