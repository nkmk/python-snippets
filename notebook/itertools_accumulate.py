import itertools
import operator

l = [1, 2, 3, 4, 5, 6]

print(itertools.accumulate(l))
# <itertools.accumulate object at 0x1080e1a80>

print(type(itertools.accumulate(l)))
# <class 'itertools.accumulate'>

for i in itertools.accumulate(l):
    print(i)
# 1
# 3
# 6
# 10
# 15
# 21

print(list(itertools.accumulate(l)))
# [1, 3, 6, 10, 15, 21]

print([0] + list(itertools.accumulate(l)))
# [0, 1, 3, 6, 10, 15, 21]

print(list(itertools.accumulate(reversed(l))))
# [6, 11, 15, 18, 20, 21]

print(operator.mul(2, 3))
# 6

l = [1, 2, 3, 4, 5, 6]

print(list(itertools.accumulate(l, func=operator.mul)))
# [1, 2, 6, 24, 120, 720]

print(list(itertools.accumulate(l, func=operator.sub)))
# [1, -1, -4, -8, -13, -19]

print(list(itertools.accumulate(l, func=operator.truediv)))
# [1, 0.5, 0.16666666666666666, 0.041666666666666664, 0.008333333333333333, 0.001388888888888889]

print(list(itertools.accumulate([1, 3, 2, 6, 5, 4], func=max)))
# [1, 3, 3, 6, 6, 6]

print(list(itertools.accumulate(l, func=lambda x, y: x * y)))
# [1, 2, 6, 24, 120, 720]

print(list(itertools.accumulate(l, func=lambda x, y: int(str(x) + str(y)))))
# [1, 12, 123, 1234, 12345, 123456]

l = [1, 2, 3, 4, 5, 6]

print(list(itertools.accumulate(l)))
# [1, 3, 6, 10, 15, 21]

print(list(itertools.accumulate(l, initial=0)))
# [0, 1, 3, 6, 10, 15, 21]

print(list(itertools.accumulate(l, initial=100)))
# [100, 101, 103, 106, 110, 115, 121]
