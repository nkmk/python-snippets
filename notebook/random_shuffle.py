import random

l = list(range(5))
print(l)
# [0, 1, 2, 3, 4]

random.shuffle(l)
print(l)
# [0, 3, 1, 4, 2]

l = list(range(5))
print(l)
# [0, 1, 2, 3, 4]

lr = random.sample(l, len(l))
print(lr)
# [4, 2, 3, 1, 0]

print(l)
# [0, 1, 2, 3, 4]

t = tuple(range(5))
print(t)
# (0, 1, 2, 3, 4)

tr = tuple(random.sample(t, len(l)))
print(tr)
# (0, 4, 3, 1, 2)

random.seed(0)
l = list(range(5))
random.shuffle(l)
print(l)
# [2, 1, 0, 4, 3]
