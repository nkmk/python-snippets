import csv
import pprint

with open('data/src/sample_header.csv') as f:
    print(f.read())
# a,b,c,d
# 11,12,13,14
# 21,22,23,24
# 31,32,33,34

with open('data/src/sample_header.csv') as f:
    reader = csv.DictReader(f)
    l = [row for row in reader]

pprint.pprint(l)
# [OrderedDict([('a', '11'), ('b', '12'), ('c', '13'), ('d', '14')]),
#  OrderedDict([('a', '21'), ('b', '22'), ('c', '23'), ('d', '24')]),
#  OrderedDict([('a', '31'), ('b', '32'), ('c', '33'), ('d', '34')])]

print(l[1])
# OrderedDict([('a', '21'), ('b', '22'), ('c', '23'), ('d', '24')])

print(l[1]['c'])
# 23

with open('data/src/sample.csv') as f:
    print(f.read())
# 11,12,13,14
# 21,22,23,24
# 31,32,33,34

with open('data/src/sample.csv') as f:
    reader = csv.DictReader(f, fieldnames=['a', 'b', 'c', 'd'], )
    for row in reader:
        print(row)
# OrderedDict([('a', '11'), ('b', '12'), ('c', '13'), ('d', '14')])
# OrderedDict([('a', '21'), ('b', '22'), ('c', '23'), ('d', '24')])
# OrderedDict([('a', '31'), ('b', '32'), ('c', '33'), ('d', '34')])

with open('data/src/sample_header_index.csv') as f:
    print(f.read())
# ,a,b,c,d
# ONE,11,12,13,14
# TWO,21,22,23,24
# THREE,31,32,33,34

with open('data/src/sample_header_index.csv') as f:
    reader = csv.DictReader(f)
    l = [row for row in reader]

pprint.pprint(l, width=100)
# [OrderedDict([('', 'ONE'), ('a', '11'), ('b', '12'), ('c', '13'), ('d', '14')]),
#  OrderedDict([('', 'TWO'), ('a', '21'), ('b', '22'), ('c', '23'), ('d', '24')]),
#  OrderedDict([('', 'THREE'), ('a', '31'), ('b', '32'), ('c', '33'), ('d', '34')])]

print([od.pop('') for od in l])
# ['ONE', 'TWO', 'THREE']

pprint.pprint(l)
# [OrderedDict([('a', '11'), ('b', '12'), ('c', '13'), ('d', '14')]),
#  OrderedDict([('a', '21'), ('b', '22'), ('c', '23'), ('d', '24')]),
#  OrderedDict([('a', '31'), ('b', '32'), ('c', '33'), ('d', '34')])]
