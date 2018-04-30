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
