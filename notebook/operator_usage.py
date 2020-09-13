import operator

print(2 + 3)
# 5

print(operator.add(2, 3))
# 5

print(operator.sub(2, 3))  # 2 - 3
# -1

print(operator.mul(2, 3))  # 2 * 3
# 6

print(operator.truediv(2, 3))  # 2 / 3
# 0.6666666666666666

print(operator.floordiv(2, 3))  # 2 // 3
# 0

print(operator.lt(2, 3))  # 2 < 3
# True

print(operator.le(2, 3))  # 2 <= 3
# True

print(operator.gt(2, 3))  # 2 > 3
# False

print(operator.ge(2, 3))  # 2 >= 3
# False

print(operator.eq(2, 3))  # 2 == 3
# False

print(operator.ne(2, 3))  # 2 != 3
# True

print(bin(0b1100 & 0b1010))
# 0b1000

print(bin(operator.and_(0b1100, 0b1010)))
# 0b1000

print(bin(0b1100 | 0b1010))
# 0b1110

print(bin(operator.or_(0b1100, 0b1010)))
# 0b1110

print(bin(0b1100 ^ 0b1010))
# 0b110

print(bin(operator.xor(0b1100, 0b1010)))
# 0b110

print(bin(0b1100 and 0b1010))
# 0b1010

print(bin(0b1100 or 0b1010))
# 0b1100

l = [0, 10, 20, 30, 40, 50]

print(l[3])
# 30

f = operator.itemgetter(3)
print(f(l))
# 30

print(operator.itemgetter(3)(l))
# 30

print(l[-1])
# 50

print(operator.itemgetter(-1)(l))
# 50

print(l[1:4])
# [10, 20, 30]

print(operator.itemgetter(slice(1, 4))(l))
# [10, 20, 30]

print(l[1::2])
# [10, 30, 50]

print(operator.itemgetter(slice(1, None, 2))(l))
# [10, 30, 50]

print(operator.itemgetter(0, slice(1, 4), -1)(l))
# (0, [10, 20, 30], 50)

print(type(operator.itemgetter(0, slice(1, 4), -1)(l)))
# <class 'tuple'>

d = {'k1': 0, 'k2': 10, 'k3': 20}

print(d['k2'])
# 10

print(operator.itemgetter('k2')(d))
# 10

print(operator.itemgetter('k2', 'k1')(d))
# (10, 0)

import datetime

dt = datetime.date(2001, 10, 20)
print(dt)
# 2001-10-20

print(type(dt))
# <class 'datetime.date'>

print(dt.year)
# 2001

f = operator.attrgetter('year')
print(f(dt))
# 2001

print(operator.attrgetter('year', 'month', 'day')(dt))
# (2001, 10, 20)

s = 'xxxAyyyAzzz'

print(s.upper())
# XXXAYYYAZZZ

f = operator.methodcaller('upper')
print(f(s))
# XXXAYYYAZZZ

print(s.split('A', maxsplit=1))
# ['xxx', 'yyyAzzz']

print(operator.methodcaller('split', 'A', maxsplit=1)(s))
# ['xxx', 'yyyAzzz']
