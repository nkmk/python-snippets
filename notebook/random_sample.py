import random

l = [0, 1, 2, 3, 4]

print(random.sample(l, 3))
# [1, 3, 2]

print(type(random.sample(l, 3)))
# <class 'list'>

print(random.sample(l, 1))
# [0]

print(random.sample(l, 0))
# []

# print(random.sample(l, 10))
# ValueError: Sample larger than population or is negative

print(random.sample(('xxx', 'yyy', 'zzz'), 2))
# ['xxx', 'yyy']

print(random.sample('abcde', 2))
# ['a', 'e']

print(tuple(random.sample(('xxx', 'yyy', 'zzz'), 2)))
# ('yyy', 'xxx')

print(''.join(random.sample('abcde', 2)))
# de
