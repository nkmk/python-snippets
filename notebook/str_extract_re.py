import re

s = '012-3456-7890'

print(re.search(r'\d+', s))
# <re.Match object; span=(0, 3), match='012'>

m = re.search(r'\d+', s)

print(m.group())
# 012

print(type(m.group()))
# <class 'str'>

print(re.findall(r'\d+', s))
# ['012', '3456', '7890']

print(re.findall('a.*b', 'axyzb'))
# ['axyzb']

print(re.findall('a.*b', 'a---b'))
# ['a---b']

print(re.findall('a.*b', 'aあいうえおb'))
# ['aあいうえおb']

print(re.findall('a.*b', 'ab'))
# ['ab']

print(re.findall('a.+b', 'ab'))
# []

print(re.findall('a.+b', 'axb'))
# ['axb']

print(re.findall('a.+b', 'axxxxxxb'))
# ['axxxxxxb']

print(re.findall('a.?b', 'ab'))
# ['ab']

print(re.findall('a.?b', 'axb'))
# ['axb']

print(re.findall('a.?b', 'axxb'))
# []

print(re.findall('a(.*)b', 'axyzb'))
# ['xyz']

print(re.findall(r'\(.+\)', 'abc(def)ghi'))
# ['(def)']

print(re.findall(r'\((.+)\)', 'abc(def)ghi'))
# ['def']

s = 'axb-axxxxxxb'

print(re.findall('a.*b', s))
# ['axb-axxxxxxb']

print(re.findall('a.*?b', s))
# ['axb', 'axxxxxxb']

print(re.findall('a.+b', s))
# ['axb-axxxxxxb']

print(re.findall('a.+?b', s))
# ['axb', 'axxxxxxb']

print(re.findall('[abc]x', 'ax-bx-cx'))
# ['ax', 'bx', 'cx']

print(re.findall('[abc]+', 'abc-aaa-cba'))
# ['abc', 'aaa', 'cba']

print(re.findall('[a-z]+', 'abc-xyz'))
# ['abc', 'xyz']

s = 'abc-012-あいうえお'

print(re.findall('[0-9]+', s))
# ['012']

print(re.findall('[a-z]+', s))
# ['abc']

print(re.findall('[ぁ-ゟ]+', s))
# ['あいうえお']

s = 'abc-def-ghi'

print(re.findall('[a-z]+', s))
# ['abc', 'def', 'ghi']

print(re.findall('^[a-z]+', s))
# ['abc']

print(re.findall('[a-z]+$', s))
# ['ghi']

s = 'axxxb-012'

print(re.findall('a.*b', s))
# ['axxxb']

print(re.findall(r'\d+', s))
# ['012']

print(re.findall(r'a.*b|\d+', s))
# ['axxxb', '012']

s = 'abc-Abc-ABC'

print(re.findall('[a-z]+', s))
# ['abc', 'bc']

print(re.findall('[A-Z]+', s))
# ['A', 'ABC']

print(re.findall('[a-z]+', s, flags=re.IGNORECASE))
# ['abc', 'Abc', 'ABC']
