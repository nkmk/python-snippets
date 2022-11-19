s = 'abc_aabbcc_abc'
print(s.count('abc'))
# 2

print(s.count('a'))
# 4

print(s.count('xyz'))
# 0

print(s.count('a', 4, 10))
# 2

print(s[4:10])
# aabbcc

print(s[4:10].count('a'))
# 2

print(s.count('a', -9))
# 2

print(s[-9:])
# abbcc_abc

print(s[-9:].count('a'))
# 2

s = 'abc_abc_abc'
print(s.count('abc_abc'))
# 1

s = 'I am Sam'
print(s.count('am'))
# 2

l = s.split()
print(l)
# ['I', 'am', 'Sam']

print(l.count('am'))
# 1

import re

s = '123-456-789'
print(re.findall('[0-9]{3}', s))
# ['123', '456', '789']

print(len(re.findall('[0-9]{3}', s)))
# 3

s = 'abc_abc_abc'
print(re.findall('(?=(abc_abc))', s))
# ['abc_abc', 'abc_abc']

print(len(re.findall('(?=(abc_abc))', s)))
# 2

s = '12345'
print(re.findall('(?=([0-9]{3}))', s))
# ['123', '234', '345']

print(len(re.findall('(?=([0-9]{3}))', s)))
# 3

s = 'abc_ABC'
print(s.count('abc'))
# 1

print(s.lower())
# abc_abc

print(s.lower().count('abc'))
# 2

print(s.upper())
# ABC_ABC

print(s.upper().count('ABC'))
# 2

print(re.findall('abc', s, flags=re.IGNORECASE))
# ['abc', 'ABC']

print(re.findall('ABC', s, flags=re.IGNORECASE))
# ['abc', 'ABC']
