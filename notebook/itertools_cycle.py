import itertools

l = [1, 10, 100]

sum_value = 0

for i in itertools.cycle(l):
    print(i)
    sum_value += i
    if sum_value > 300:
        break
# 1
# 10
# 100
# 1
# 10
# 100
# 1
# 10
# 100

sum_value = 0

for i in itertools.cycle(range(3)):
    print(i)
    sum_value += i
    if sum_value > 5:
        break
# 0
# 1
# 2
# 0
# 1
# 2

l1 = [1, 10, 100]
l2 = [0, 1, 2, 3, 4, 5, 6]

print(list(zip(itertools.cycle(l1), l2)))
# [(1, 0), (10, 1), (100, 2), (1, 3), (10, 4), (100, 5), (1, 6)]
