import json
from collections import OrderedDict
import pprint

s = r'{"C": "\u3042", "A": {"i": 1, "j": 2}, "B": [{"X": 1, "Y": 10}, {"X": 2, "Y": 20}]}'

print(s)
# {"C": "\u3042", "A": {"i": 1, "j": 2}, "B": [{"X": 1, "Y": 10}, {"X": 2, "Y": 20}]}

d = json.loads(s)

pprint.pprint(d, width=40)
# {'A': {'i': 1, 'j': 2},
#  'B': [{'X': 1, 'Y': 10},
#        {'X': 2, 'Y': 20}],
#  'C': 'あ'}

print(type(d))
# <class 'dict'>

od = json.loads(s, object_pairs_hook=OrderedDict)

pprint.pprint(od)
# OrderedDict([('C', 'あ'),
#              ('A', OrderedDict([('i', 1), ('j', 2)])),
#              ('B',
#               [OrderedDict([('X', 1), ('Y', 10)]),
#                OrderedDict([('X', 2), ('Y', 20)])])])

b = s.encode()

print(b)
# b'{"C": "\\u3042", "A": {"i": 1, "j": 2}, "B": [{"X": 1, "Y": 10}, {"X": 2, "Y": 20}]}'

print(type(b))
# <class 'bytes'>

db = json.loads(b)

pprint.pprint(db, width=40)
# {'A': {'i': 1, 'j': 2},
#  'B': [{'X': 1, 'Y': 10},
#        {'X': 2, 'Y': 20}],
#  'C': 'あ'}

print(type(db))
# <class 'dict'>

sb = b.decode()

print(sb)
# {"C": "\u3042", "A": {"i": 1, "j": 2}, "B": [{"X": 1, "Y": 10}, {"X": 2, "Y": 20}]}

print(type(sb))
# <class 'str'>

dsb = json.loads(sb)

pprint.pprint(dsb, width=40)
# {'A': {'i': 1, 'j': 2},
#  'B': [{'X': 1, 'Y': 10},
#        {'X': 2, 'Y': 20}],
#  'C': 'あ'}

print(type(dsb))
# <class 'dict'>

sb_u = b.decode('unicode-escape')

print(sb_u)
# {"C": "あ", "A": {"i": 1, "j": 2}, "B": [{"X": 1, "Y": 10}, {"X": 2, "Y": 20}]}

print(type(sb_u))
# <class 'str'>

dsb_u = json.loads(sb_u)

pprint.pprint(dsb_u, width=40)
# {'A': {'i': 1, 'j': 2},
#  'B': [{'X': 1, 'Y': 10},
#        {'X': 2, 'Y': 20}],
#  'C': 'あ'}

print(type(dsb_u))
# <class 'dict'>

with open('data/src/test.json') as f:
    print(f.read())
# {"C": "\u3042", "A": {"i": 1, "j": 2}, "B": [{"X": 1, "Y": 10}, {"X": 2, "Y": 20}]}

with open('data/src/test.json') as f:
    df = json.load(f)

pprint.pprint(df, width=40)
# {'A': {'i': 1, 'j': 2},
#  'B': [{'X': 1, 'Y': 10},
#        {'X': 2, 'Y': 20}],
#  'C': 'あ'}

print(type(df))
# <class 'dict'>

pprint.pprint(d, width=40)
# {'A': {'i': 1, 'j': 2},
#  'B': [{'X': 1, 'Y': 10},
#        {'X': 2, 'Y': 20}],
#  'C': 'あ'}

print(d['A'])
# {'i': 1, 'j': 2}

print(d['A']['i'])
# 1

print(d['B'])
# [{'X': 1, 'Y': 10}, {'X': 2, 'Y': 20}]

print(d['B'][0])
# {'X': 1, 'Y': 10}

print(d['B'][0]['X'])
# 1

value = d['B'][1]['Y']
print(value)
# 20

# print(d['D'])
# KeyError: 'D'

print(d.get('D'))
# None

d['C'] = 'ん'
pprint.pprint(d, width=40)
# {'A': {'i': 1, 'j': 2},
#  'B': [{'X': 1, 'Y': 10},
#        {'X': 2, 'Y': 20}],
#  'C': 'ん'}

d.pop('C')
pprint.pprint(d, width=40)
# {'A': {'i': 1, 'j': 2},
#  'B': [{'X': 1, 'Y': 10},
#        {'X': 2, 'Y': 20}]}

d['C'] = 'あ'
pprint.pprint(d, width=40)
# {'A': {'i': 1, 'j': 2},
#  'B': [{'X': 1, 'Y': 10},
#        {'X': 2, 'Y': 20}],
#  'C': 'あ'}

sd = json.dumps(d)

print(sd)
# {"A": {"i": 1, "j": 2}, "B": [{"X": 1, "Y": 10}, {"X": 2, "Y": 20}], "C": "\u3042"}

print(type(sd))
# <class 'str'>

pprint.pprint(od)
# OrderedDict([('C', 'あ'),
#              ('A', OrderedDict([('i', 1), ('j', 2)])),
#              ('B',
#               [OrderedDict([('X', 1), ('Y', 10)]),
#                OrderedDict([('X', 2), ('Y', 20)])])])

sod = json.dumps(od)

print(sod)
# {"C": "\u3042", "A": {"i": 1, "j": 2}, "B": [{"X": 1, "Y": 10}, {"X": 2, "Y": 20}]}

print(type(sod))
# <class 'str'>

print(json.dumps(d, separators=(',', ':')))
# {"A":{"i":1,"j":2},"B":[{"X":1,"Y":10},{"X":2,"Y":20}],"C":"\u3042"}

print(json.dumps(d, separators=(' / ', '-> ')))
# {"A"-> {"i"-> 1 / "j"-> 2} / "B"-> [{"X"-> 1 / "Y"-> 10} / {"X"-> 2 / "Y"-> 20}] / "C"-> "\u3042"}

print(json.dumps(d, indent=4))
# {
#     "A": {
#         "i": 1,
#         "j": 2
#     },
#     "B": [
#         {
#             "X": 1,
#             "Y": 10
#         },
#         {
#             "X": 2,
#             "Y": 20
#         }
#     ],
#     "C": "\u3042"
# }

print(json.dumps(od))
# {"C": "\u3042", "A": {"i": 1, "j": 2}, "B": [{"X": 1, "Y": 10}, {"X": 2, "Y": 20}]}

print(json.dumps(od, sort_keys=True))
# {"A": {"i": 1, "j": 2}, "B": [{"X": 1, "Y": 10}, {"X": 2, "Y": 20}], "C": "\u3042"}

print(json.dumps(od, ensure_ascii=False))
# {"C": "あ", "A": {"i": 1, "j": 2}, "B": [{"X": 1, "Y": 10}, {"X": 2, "Y": 20}]}

with open('data/dst/test2.json', 'w') as f:
    json.dump(d, f, indent=4)

with open('data/dst/test2.json') as f:
    print(f.read())
# {
#     "A": {
#         "i": 1,
#         "j": 2
#     },
#     "B": [
#         {
#             "X": 1,
#             "Y": 10
#         },
#         {
#             "X": 2,
#             "Y": 20
#         }
#     ],
#     "C": "\u3042"
# }

d_new = {'A': 100, 'B': 'abc', 'C': 'あいうえお'}

with open('data/dst/test_new.json', 'w') as f:
    json.dump(d_new, f, indent=2, ensure_ascii=False)

with open('data/dst/test_new.json') as f:
    print(f.read())
# {
#   "A": 100,
#   "B": "abc",
#   "C": "あいうえお"
# }

with open('data/dst/test_new.json') as f:
    d_update = json.load(f, object_pairs_hook=OrderedDict)

print(d_update)
# OrderedDict([('A', 100), ('B', 'abc'), ('C', 'あいうえお')])

d_update['A'] = 200
d_update.pop('B')
d_update['D'] = 'new value'

print(d_update)
# OrderedDict([('A', 200), ('C', 'あいうえお'), ('D', 'new value')])

with open('data/dst/test_new_update.json', 'w') as f:
    json.dump(d_update, f, indent=2, ensure_ascii=False)

with open('data/dst/test_new_update.json') as f:
    print(f.read())
# {
#   "A": 200,
#   "C": "あいうえお",
#   "D": "new value"
# }

with open('data/src/test.json') as f:
    print(f.read())
# {"C": "\u3042", "A": {"i": 1, "j": 2}, "B": [{"X": 1, "Y": 10}, {"X": 2, "Y": 20}]}

with open('data/src/test.json', encoding='unicode-escape') as f:
    print(f.read())
# {"C": "あ", "A": {"i": 1, "j": 2}, "B": [{"X": 1, "Y": 10}, {"X": 2, "Y": 20}]}

print(b)
# b'{"C": "\\u3042", "A": {"i": 1, "j": 2}, "B": [{"X": 1, "Y": 10}, {"X": 2, "Y": 20}]}'

print(b.decode())
# {"C": "\u3042", "A": {"i": 1, "j": 2}, "B": [{"X": 1, "Y": 10}, {"X": 2, "Y": 20}]}

print(b.decode(encoding='unicode-escape'))
# {"C": "あ", "A": {"i": 1, "j": 2}, "B": [{"X": 1, "Y": 10}, {"X": 2, "Y": 20}]}

d = {"A": 100, "B": 'abc', "C": 'あいうえお'}

print(str(d))
# {'A': 100, 'B': 'abc', 'C': 'あいうえお'}

# print(json.loads(str(d)))
# JSONDecodeError: Expecting property name enclosed in double quotes: line 1 column 2 (char 1)

print(json.dumps(d))
# {"A": 100, "B": "abc", "C": "\u3042\u3044\u3046\u3048\u304a"}

print(json.loads(json.dumps(d)))
# {'A': 100, 'B': 'abc', 'C': 'あいうえお'}

print(type(json.loads(json.dumps(d))))
# <class 'dict'>
