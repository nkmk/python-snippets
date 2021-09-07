import random

l = list(range(5))
print(l)
# [0, 1, 2, 3, 4]

random.shuffle(l)
print(l)
# [1, 0, 4, 3, 2]

l = list(range(5))
print(l)
# [0, 1, 2, 3, 4]

lr = random.sample(l, len(l))
print(lr)
# [0, 3, 1, 4, 2]

print(l)
# [0, 1, 2, 3, 4]

s = 'abcde'

# random.shuffle(s)
# TypeError: 'str' object does not support item assignment

t = tuple(range(5))
print(t)
# (0, 1, 2, 3, 4)

# random.shuffle(t)
# TypeError: 'tuple' object does not support item assignment

sr = ''.join(random.sample(s, len(s)))
print(sr)
# bedca

tr = tuple(random.sample(t, len(l)))
print(tr)
# (0, 1, 2, 4, 3)

l = list(range(5))
random.seed(0)
random.shuffle(l)
print(l)
# [2, 1, 0, 4, 3]

l = list(range(5))
random.seed(0)
random.shuffle(l)
print(l)
# [2, 1, 0, 4, 3]
