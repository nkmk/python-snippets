import pprint

l = [{'Name': 'Alice XXX', 'Age': 40, 'Points': [80, 20]}, 
     {'Name': 'Bob YYY', 'Age': 20, 'Points': [90, 10]},
     {'Name': 'Charlie ZZZ', 'Age': 30, 'Points': [70, 30]}]

print(l)
# [{'Name': 'Alice XXX', 'Age': 40, 'Points': [80, 20]}, {'Name': 'Bob YYY', 'Age': 20, 'Points': [90, 10]}, {'Name': 'Charlie ZZZ', 'Age': 30, 'Points': [70, 30]}]

pprint.pprint(l)
# [{'Age': 40, 'Name': 'Alice XXX', 'Points': [80, 20]},
#  {'Age': 20, 'Name': 'Bob YYY', 'Points': [90, 10]},
#  {'Age': 30, 'Name': 'Charlie ZZZ', 'Points': [70, 30]}]

pprint.pprint(l, width=40)
# [{'Age': 40,
#   'Name': 'Alice XXX',
#   'Points': [80, 20]},
#  {'Age': 20,
#   'Name': 'Bob YYY',
#   'Points': [90, 10]},
#  {'Age': 30,
#   'Name': 'Charlie ZZZ',
#   'Points': [70, 30]}]

pprint.pprint(l, width=200)
# [{'Age': 40, 'Name': 'Alice XXX', 'Points': [80, 20]}, {'Age': 20, 'Name': 'Bob YYY', 'Points': [90, 10]}, {'Age': 30, 'Name': 'Charlie ZZZ', 'Points': [70, 30]}]

pprint.pprint(l, width=1)
# [{'Age': 40,
#   'Name': 'Alice '
#           'XXX',
#   'Points': [80,
#              20]},
#  {'Age': 20,
#   'Name': 'Bob '
#           'YYY',
#   'Points': [90,
#              10]},
#  {'Age': 30,
#   'Name': 'Charlie '
#           'ZZZ',
#   'Points': [70,
#              30]}]

pprint.pprint(l, depth=1)
# [{...}, {...}, {...}]

pprint.pprint(l, depth=2)
# [{'Age': 40, 'Name': 'Alice XXX', 'Points': [...]},
#  {'Age': 20, 'Name': 'Bob YYY', 'Points': [...]},
#  {'Age': 30, 'Name': 'Charlie ZZZ', 'Points': [...]}]

pprint.pprint(l, depth=2, width=40)
# [{'Age': 40,
#   'Name': 'Alice XXX',
#   'Points': [...]},
#  {'Age': 20,
#   'Name': 'Bob YYY',
#   'Points': [...]},
#  {'Age': 30,
#   'Name': 'Charlie ZZZ',
#   'Points': [...]}]

pprint.pprint(l, indent=4, width=4)
# [   {   'Age': 40,
#         'Name': 'Alice '
#                 'XXX',
#         'Points': [   80,
#                       20]},
#     {   'Age': 20,
#         'Name': 'Bob '
#                 'YYY',
#         'Points': [   90,
#                       10]},
#     {   'Age': 30,
#         'Name': 'Charlie '
#                 'ZZZ',
#         'Points': [   70,
#                       30]}]

l_long = [list(range(10)), list(range(100, 110))]

print(l_long)
# [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [100, 101, 102, 103, 104, 105, 106, 107, 108, 109]]

pprint.pprint(l_long, width=40)
# [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
#  [100,
#   101,
#   102,
#   103,
#   104,
#   105,
#   106,
#   107,
#   108,
#   109]]

pprint.pprint(l_long, width=40, compact=True)
# [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
#  [100, 101, 102, 103, 104, 105, 106,
#   107, 108, 109]]

s_normal = str(l)
print(s_normal)
# [{'Name': 'Alice XXX', 'Age': 40, 'Points': [80, 20]}, {'Name': 'Bob YYY', 'Age': 20, 'Points': [90, 10]}, {'Name': 'Charlie ZZZ', 'Age': 30, 'Points': [70, 30]}]

print(type(s_normal))
# <class 'str'>

s_pp = pprint.pformat(l)
print(s_pp)
# [{'Age': 40, 'Name': 'Alice XXX', 'Points': [80, 20]},
#  {'Age': 20, 'Name': 'Bob YYY', 'Points': [90, 10]},
#  {'Age': 30, 'Name': 'Charlie ZZZ', 'Points': [70, 30]}]

print(type(s_pp))
# <class 'str'>

s_pp = pprint.pformat(l, depth=2, width=40, indent=2)
print(s_pp)
# [ { 'Age': 40,
#     'Name': 'Alice XXX',
#     'Points': [...]},
#   { 'Age': 20,
#     'Name': 'Bob YYY',
#     'Points': [...]},
#   { 'Age': 30,
#     'Name': 'Charlie ZZZ',
#     'Points': [...]}]

l_2d = [list(range(10)), list(range(10)), list(range(10))]

print(l_2d)
# [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]]

pprint.pprint(l_2d)
# [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
#  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
#  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]]

l_2d = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]

print(l_2d)
# [[0, 1, 2], [3, 4, 5], [6, 7, 8]]

pprint.pprint(l_2d)
# [[0, 1, 2], [3, 4, 5], [6, 7, 8]]

pprint.pprint(l_2d, width=20)
# [[0, 1, 2],
#  [3, 4, 5],
#  [6, 7, 8]]

s = pprint.pformat(l_2d, width=20)
print(s)
# [[0, 1, 2],
#  [3, 4, 5],
#  [6, 7, 8]]

print(type(s))
# <class 'str'>
