import re

l = ['oneXXXaaa', 'twoXXXbbb', 'three999aaa', '000111222']

l_re_match = [s for s in l if re.match('.*XXX.*', s)]
print(l_re_match)
# ['oneXXXaaa', 'twoXXXbbb']

l_re_sub_all = [re.sub('(.*)XXX(.*)', r'\2---\1', s) for s in l]
print(l_re_sub_all)
# ['aaa---one', 'bbb---two', 'three999aaa', '000111222']

l_re_sub = [re.sub('(.*)XXX(.*)', r'\2---\1', s) for s in l if re.match('.*XXX.*', s)]
print(l_re_sub)
# ['aaa---one', 'bbb---two']
