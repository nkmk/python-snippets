import re

s = '111aaa222bbb333'

result = re.split('[a-z]+', s)
print(result)
# ['111', '222', '333']

result = re.split('[0-9]+', s)
print(result)
# ['', 'aaa', 'bbb', '']

result = re.split('[a-z]+', s, 1)
print(result)
# ['111', '222bbb333']
