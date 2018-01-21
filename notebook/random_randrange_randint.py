import random

print(list(range(10)))
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(random.randrange(10))
# 5

print(list(range(10, 20, 2)))
# [10, 12, 14, 16, 18]

print(random.randrange(10, 20, 2))
# 18

print(random.randint(50, 100))
# print(random.randrange(50, 101))
# 74

random.seed(0)
print(random.randint(50, 100))
# 74
