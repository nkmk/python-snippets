import csv
import pprint

with open('data/src/sample.csv') as f:
    print(f.read())
# 11,12,13,14
# 21,22,23,24
# 31,32,33,34

with open('data/src/sample.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
# ['11', '12', '13', '14']
# ['21', '22', '23', '24']
# ['31', '32', '33', '34']

with open('data/src/sample.csv') as f:
    reader = csv.reader(f)
    l = [row for row in reader]

print(l)
# [['11', '12', '13', '14'], ['21', '22', '23', '24'], ['31', '32', '33', '34']]

print(l[1])
# ['21', '22', '23', '24']

print(l[1][1])
# 22

l_T = [list(x) for x in zip(*l)]
print(l_T)
# [['11', '21', '31'], ['12', '22', '32'], ['13', '23', '33'], ['14', '24', '34']]

print(l_T[1])
# ['12', '22', '32']

print(l[0][0])
# 11

print(type(l[0][0]))
# <class 'str'>

r = l[0]
print(r)
# ['11', '12', '13', '14']

print([int(v) for v in r])
# [11, 12, 13, 14]

print([[int(v) for v in row] for row in l])
# [[11, 12, 13, 14], [21, 22, 23, 24], [31, 32, 33, 34]]

with open('data/src/sample.csv') as f:
    reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
    l_f = [row for row in reader]

print(l_f)
# [[11.0, 12.0, 13.0, 14.0], [21.0, 22.0, 23.0, 24.0], [31.0, 32.0, 33.0, 34.0]]

print(l_f[0][0])
# 11.0

print(type(l_f[0][0]))
# <class 'float'>

with open('data/src/sample.txt') as f:
    print(f.read())
# 11 12 13 14
# 21 22 23 24
# 31 32 33 34

with open('data/src/sample.txt') as f:
    reader = csv.reader(f, delimiter=' ')
    l = [row for row in reader]

print(l)
# [['11', '12', '13', '14'], ['21', '22', '23', '24'], ['31', '32', '33', '34']]

with open('data/src/sample_quote.csv') as f:
    print(f.read())
# 1,2,"3"
# "a,b,c",x,y

with open('data/src/sample_quote.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
# ['1', '2', '3']
# ['a,b,c', 'x', 'y']

with open('data/src/sample_quote.csv') as f:
    reader = csv.reader(f, quoting=csv.QUOTE_NONE)
    for row in reader:
        print(row)
# ['1', '2', '"3"']
# ['"a', 'b', 'c"', 'x', 'y']

with open('data/src/sample_linebreak.csv') as f:
    print(f.read())
# 1,2,"3"
# "a
# b",x,y

with open('data/src/sample_linebreak.csv', newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
# ['1', '2', '3']
# ['a\nb', 'x', 'y']

with open('data/src/sample_header_index.csv') as f:
    print(f.read())
# ,a,b,c,d
# ONE,11,12,13,14
# TWO,21,22,23,24
# THREE,31,32,33,34

with open('data/src/sample_header_index.csv') as f:
    reader = csv.reader(f)
    l = [row for row in reader]

pprint.pprint(l)
# [['', 'a', 'b', 'c', 'd'],
#  ['ONE', '11', '12', '13', '14'],
#  ['TWO', '21', '22', '23', '24'],
#  ['THREE', '31', '32', '33', '34']]

print([row[1:] for row in l[1:]])
# [['11', '12', '13', '14'], ['21', '22', '23', '24'], ['31', '32', '33', '34']]

print([[int(v) for v in row[1:]] for row in l[1:]])
# [[11, 12, 13, 14], [21, 22, 23, 24], [31, 32, 33, 34]]
