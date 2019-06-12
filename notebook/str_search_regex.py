import re

s = 'I am Sam'

print(re.search('Sam', s))
# <re.Match object; span=(5, 8), match='Sam'>

print(re.search('XXX', s))
# None

m = re.search('Sam', s)

print(m.group())
# Sam

print(m.start())
# 5

print(m.end())
# 8

print(m.span())
# (5, 8)

s = 'I am Sam'

print(re.search('am', s))
# <re.Match object; span=(2, 4), match='am'>

print(re.findall('am', s))
# ['am', 'am']

print(len(re.findall('am', s)))
# 2

print([m.span() for m in re.finditer('am', s)])
# [(2, 4), (6, 8)]

s = 'I am Sam Adams'

print(re.findall('Sam|Adams', s))
# ['Sam', 'Adams']

print([m.span() for m in re.finditer('Sam|Adams', s)])
# [(5, 8), (9, 14)]

s = 'I am Sam Adams'

print(re.findall('am', s))
# ['am', 'am', 'am']

print(re.findall('[a-zA-Z]+am[a-z]*', s))
# ['Sam', 'Adams']

s = 'I am Sam'

print(re.search('sam', s))
# None

print(re.search('sam', s, flags=re.IGNORECASE))
# <re.Match object; span=(5, 8), match='Sam'>
