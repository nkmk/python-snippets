import random

l = [0, 1, 2, 3, 4]

print(random.sample(l, 3))
# [3, 1, 0]

print(type(random.sample(l, 3)))
# <class 'list'>

print(random.sample(l, 1))
# [1]

print(random.sample(l, 0))
# []

# print(random.sample(l, 10))
# ValueError: Sample larger than population or is negative

print(random.sample(('xxx', 'yyy', 'zzz'), 2))
# ['zzz', 'xxx']

print(random.sample('abcde', 2))
# ['c', 'd']

print(tuple(random.sample(('xxx', 'yyy', 'zzz'), 2)))
# ('zzz', 'yyy')

print(''.join(random.sample('abcde', 2)))
# be

l_dup = [0, 0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 3]

print(random.sample(l_dup, 3))
# [2, 0, 0]

print(set(l_dup))
# {0, 1, 2, 3}

print(random.sample(list(set(l_dup)), 3))
# [0, 2, 1]
