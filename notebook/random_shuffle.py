import random

l = [0, 1, 2, 3, 4]

random.shuffle(l)
print(l)
# [0, 3, 2, 4, 1]

l = [0, 1, 2, 3, 4]

l_shuffled = random.sample(l, len(l))
print(l_shuffled)
# [4, 3, 0, 1, 2]

print(l)
# [0, 1, 2, 3, 4]

s = 'abcde'

# random.shuffle(s)
# TypeError: 'str' object does not support item assignment

t = (0, 1, 2, 3, 4)

# random.shuffle(t)
# TypeError: 'tuple' object does not support item assignment

s_shuffled = ''.join(random.sample(s, len(s)))
print(s_shuffled)
# aedcb

t_shuffled = tuple(random.sample(t, len(l)))
print(t_shuffled)
# (4, 1, 2, 0, 3)

l = ['apple', 'banana', 'cherry', 'date']

l_shuffled = random.sample(l, len(l))
print(l_shuffled)
# ['cherry', 'banana', 'apple', 'date']

random.shuffle(l)
print(l)
# ['date', 'apple', 'cherry', 'banana']

l = [0, 1, 2, 3, 4]
random.seed(0)
random.shuffle(l)
print(l)
# [2, 1, 0, 4, 3]

l = [0, 1, 2, 3, 4]
random.seed(0)
random.shuffle(l)
print(l)
# [2, 1, 0, 4, 3]
