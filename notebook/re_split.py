import re

s = '111aaa222bbb333'

print(re.split('[a-z]+', s))
# ['111', '222', '333']

print(re.split('[0-9]+', s))
# ['', 'aaa', 'bbb', '']

print(re.split('[a-z]+', s, 1))
# ['111', '222bbb333']
