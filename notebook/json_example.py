import json

s = '{"A": {"X": 1, "Y": 1.0, "Z": "abc"}, "B": [true, false, null, NaN, Infinity]}'

d = json.loads(s)
print(d)
# {'A': {'X': 1, 'Y': 1.0, 'Z': 'abc'}, 'B': [True, False, None, nan, inf]}

print(type(d))
# <class 'dict'>

s = '{"A": True}'

# d = json.loads(s)
# JSONDecodeError: Expecting value: line 1 column 7 (char 6)

with open('data/src/test.json') as f:
    print(f.read())
# {"A": {"X": 1, "Y": 1.0, "Z": "abc"}, "B": [true, false, null, NaN, Infinity]}

with open('data/src/test.json') as f:
    d = json.load(f)

print(d)
# {'A': {'X': 1, 'Y': 1.0, 'Z': 'abc'}, 'B': [True, False, None, nan, inf]}

print(type(d))
# <class 'dict'>

d = {'A': {'X': 1, 'Y': 1.0, 'Z': 'abc'}, 'B': [True, False, None]}

s = json.dumps(d)
print(s)
# {"A": {"X": 1, "Y": 1.0, "Z": "abc"}, "B": [true, false, null]}

print(type(s))
# <class 'str'>

d = {'A': {'X': 1, 'Y': 1.0, 'Z': 'abc'}, 'B': [True, False, None]}
print(json.dumps(d, separators=(',', ':')))
# {"A":{"X":1,"Y":1.0,"Z":"abc"},"B":[true,false,null]}

print(json.dumps(d, separators=(' / ', '->')))
# {"A"->{"X"->1 / "Y"->1.0 / "Z"->"abc"} / "B"->[true / false / null]}

d = {'A': {'X': 1, 'Y': 1.0, 'Z': 'abc'}, 'B': [True, False, None]}
print(json.dumps(d, indent=4))
# {
#     "A": {
#         "X": 1,
#         "Y": 1.0,
#         "Z": "abc"
#     },
#     "B": [
#         true,
#         false,
#         null
#     ]
# }

d = {'B': {'Y': 2, 'X': 1}, 'A': [3, 1, 2]}
print(json.dumps(d))
# {"B": {"Y": 2, "X": 1}, "A": [3, 1, 2]}

print(json.dumps(d, sort_keys=True))
# {"A": [3, 1, 2], "B": {"X": 1, "Y": 2}}

d = {'A': [float('nan'), float('inf')]}
print(json.dumps(d))
# {"A": [NaN, Infinity]}

# print(json.dumps(d, allow_nan=False))
# ValueError: Out of range float values are not JSON compliant

d = {'A': 'あいうえお', 'B': 'abc'}
print(json.dumps(d))
# {"A": "\u3042\u3044\u3046\u3048\u304a", "B": "abc"}

print(json.dumps(d, ensure_ascii=False))
# {"A": "あいうえお", "B": "abc"}

d = {
    'A': {'X': 1, 'Y': 1.0, 'Z': 'abc'},
    'B': [True, False, None, float('nan'), float('inf')]
}

with open('data/temp/test.json', 'w') as f:
    json.dump(d, f, indent=2)

with open('data/temp/test.json') as f:
    print(f.read())
# {
#   "A": {
#     "X": 1,
#     "Y": 1.0,
#     "Z": "abc"
#   },
#   "B": [
#     true,
#     false,
#     null,
#     NaN,
#     Infinity
#   ]
# }

d_new = {'A': 100, 'B': 'abc', 'C': [True, False]}

with open('data/temp/test_new.json', 'w') as f:
    json.dump(d_new, f, indent=2)

with open('data/temp/test_new.json') as f:
    print(f.read())
# {
#   "A": 100,
#   "B": "abc",
#   "C": [
#     true,
#     false
#   ]
# }

with open('data/temp/test_new.json') as f:
    d_update = json.load(f)

print(d_update)
# {'A': 100, 'B': 'abc', 'C': [True, False]}

d_update['A'] = 200
d_update.pop('B')
d_update['D'] = 'new value'

print(d_update)
# {'A': 200, 'C': [True, False], 'D': 'new value'}

with open('data/temp/test_new_update.json', 'w') as f:
    json.dump(d_update, f, indent=2)

with open('data/temp/test_new_update.json') as f:
    print(f.read())
# {
#   "A": 200,
#   "C": [
#     true,
#     false
#   ],
#   "D": "new value"
# }

d = {'A': 100, 'B': 'abc', 'C': [True, False]}

s = str(d)
print(str(d))
# {'A': 100, 'B': 'abc', 'C': [True, False]}

# print(json.loads(s))
# JSONDecodeError: Expecting property name enclosed in double quotes: line 1 column 2 (char 1)

s = json.dumps(d)
print(s)
# {"A": 100, "B": "abc", "C": [true, false]}

print(json.dumps(d))
# {"A": 100, "B": "abc", "C": [true, false]}

with open('data/src/test_u.json') as f:
    print(f.read())
# {"A": "\u3042\u3044\u3046\u3048\u304a", "B": "abc"}

with open('data/src/test_u.json', encoding='unicode-escape') as f:
    print(f.read())
# {"A": "あいうえお", "B": "abc"}

with open('data/src/test_u.json') as f:
    print(json.load(f))
# {'A': 'あいうえお', 'B': 'abc'}

s = r'{"A": "\u3042\u3044\u3046\u3048\u304a", "B": "abc"}'
b = s.encode()
print(b)
# b'{"A": "\\u3042\\u3044\\u3046\\u3048\\u304a", "B": "abc"}'

print(b.decode())
# {"A": "\u3042\u3044\u3046\u3048\u304a", "B": "abc"}

print(b.decode(encoding='unicode-escape'))
# {"A": "あいうえお", "B": "abc"}

print(json.loads(b))
# {'A': 'あいうえお', 'B': 'abc'}
