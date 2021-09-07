import random

l = [0, 1, 2, 3, 4]

print(random.choice(l))
# 1

print(random.choice(('xxx', 'yyy', 'zzz')))
# yyy

print(random.choice('abcde'))
# b

# print(random.choice([]))
# IndexError: Cannot choose from an empty sequence

random.seed(0)
print(random.choice(l))
# 3

random.seed(0)
print(random.choice(l))
# 3
