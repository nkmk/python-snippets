import re

s = 'aaa-AAA-123'

print(re.search('aaa', s))
# <re.Match object; span=(0, 3), match='aaa'>

print(re.search('xxx', s))
# None

print(re.search('^aaa', s))
# <re.Match object; span=(0, 3), match='aaa'>

print(re.search('^123', s))
# None

print(re.search('aaa$', s))
# None

print(re.search('123$', s))
# <re.Match object; span=(8, 11), match='123'>

print(re.search('[A-Z]+', s))
# <re.Match object; span=(4, 7), match='AAA'>

s = '012-3456-7890'

print(re.fullmatch(r'\d{3}-\d{4}-\d{4}', s))
# <re.Match object; span=(0, 13), match='012-3456-7890'>

s = 'tel: 012-3456-7890'

print(re.fullmatch(r'\d{3}-\d{4}-\d{4}', s))
# None

s = '012-3456-7890'

print(re.search(r'^\d{3}-\d{4}-\d{4}$', s))
# <re.Match object; span=(0, 13), match='012-3456-7890'>

s = 'tel: 012-3456-7890'

print(re.search('^\d{3}-\d{4}-\d{4}$', s))
# None

s = 'ABC'

print(re.search('abc', s))
# None

print(re.search('abc', s, re.IGNORECASE))
# <re.Match object; span=(0, 3), match='ABC'>
