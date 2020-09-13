import operator

l_2d = [[2, 10], [1, -30], [-3, 20]]

print(sorted(l_2d, key=operator.itemgetter(1)))
# [[1, -30], [2, 10], [-3, 20]]

f = operator.itemgetter(1)
print(f([2, 10]))
# 10

print(operator.itemgetter(1)([2, 10]))
# 10

print(sorted(l_2d, key=lambda x: x[1]))
# [[1, -30], [2, 10], [-3, 20]]

l_dict = [{'k1': 2, 'k2': 10}, {'k1': 1}, {'k1': 3}]

# print(sorted(l_dict))
# TypeError: '<' not supported between instances of 'dict' and 'dict'

print(sorted(l_dict, key=operator.itemgetter('k1')))
# [{'k1': 1}, {'k1': 2, 'k2': 10}, {'k1': 3}]

# print(sorted(l_dict, key=operator.itemgetter('k2')))
# KeyError: 'k2'

print(sorted(l_dict, key=lambda x: x['k1']))
# [{'k1': 1}, {'k1': 2, 'k2': 10}, {'k1': 3}]

l_dict = [{'k1': 2, 'k2': 'ccc'}, {'k1': 1, 'k2': 'ccc'}, {'k1': 2, 'k2': 'aaa'}]

print(operator.itemgetter('k1', 'k2')(l_dict[0]))
# (2, 'ccc')

print(sorted(l_dict, key=operator.itemgetter('k1')))
# [{'k1': 1, 'k2': 'ccc'}, {'k1': 2, 'k2': 'ccc'}, {'k1': 2, 'k2': 'aaa'}]

print(sorted(l_dict, key=operator.itemgetter('k1', 'k2')))
# [{'k1': 1, 'k2': 'ccc'}, {'k1': 2, 'k2': 'aaa'}, {'k1': 2, 'k2': 'ccc'}]

print(sorted(l_dict, key=operator.itemgetter('k2', 'k1')))
# [{'k1': 2, 'k2': 'aaa'}, {'k1': 1, 'k2': 'ccc'}, {'k1': 2, 'k2': 'ccc'}]

print(sorted(l_dict, key=lambda x: (x['k1'], x['k2'])))
# [{'k1': 1, 'k2': 'ccc'}, {'k1': 2, 'k2': 'aaa'}, {'k1': 2, 'k2': 'ccc'}]

import datetime

l_dt = [datetime.date(2003, 2, 10), datetime.date(2001, 3, 20), datetime.date(2002, 1, 30)]

print(l_dt[0])
# 2003-02-10

print(l_dt[0].day)
# 10

f = operator.attrgetter('day')
print(f(l_dt[0]))
# 10

print(sorted(l_dt))
# [datetime.date(2001, 3, 20), datetime.date(2002, 1, 30), datetime.date(2003, 2, 10)]

print(sorted(l_dt, key=operator.attrgetter('day')))
# [datetime.date(2003, 2, 10), datetime.date(2001, 3, 20), datetime.date(2002, 1, 30)]

print(sorted(l_dt, key=lambda x: x.day))
# [datetime.date(2003, 2, 10), datetime.date(2001, 3, 20), datetime.date(2002, 1, 30)]

l_str = ['0_xxxxA', '1_Axxxx', '2_xxAxx']

print(l_str[0])
# 0_xxxxA

print(l_str[0].find('A'))
# 6

f = operator.methodcaller('find', 'A')
print(f(l_str[0]))
# 6

print(sorted(l_str))
# ['0_xxxxA', '1_Axxxx', '2_xxAxx']

print(sorted(l_str, key=operator.methodcaller('find', 'A')))
# ['1_Axxxx', '2_xxAxx', '0_xxxxA']

print(sorted(l_str, key=lambda x: x.find('A')))
# ['1_Axxxx', '2_xxAxx', '0_xxxxA']
