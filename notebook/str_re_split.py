import re

s_nums = 'one1two22three333four'

print(re.split('\d+', s_nums))
# ['one', 'two', 'three', 'four']

print(re.split('\d+', s_nums, 2))
# ['one', 'two', 'three333four']

s_marks = 'one-two+three#four'

print(re.split('[-+#]', s_marks))
# ['one', 'two', 'three', 'four']

s_strs = 'oneXXXtwoYYYthreeZZZfour'

print(re.split('XXX|YYY|ZZZ', s_strs))
# ['one', 'two', 'three', 'four']
