l = ['oneXXXaaa', 'twoXXXbbb', 'three999aaa', '000111222']

l_in = [s for s in l if 'XXX' in s]
print(l_in)
# ['oneXXXaaa', 'twoXXXbbb']

l_in_not = [s for s in l if 'XXX' not in s]
print(l_in_not)
# ['three999aaa', '000111222']

l_replace = [s.replace('XXX', 'ZZZ') for s in l]
print(l_replace)
# ['oneZZZaaa', 'twoZZZbbb', 'three999aaa', '000111222']

l_replace_all = ['ZZZ' if 'XXX' in s else s for s in l]
print(l_replace_all)
# ['ZZZ', 'ZZZ', 'three999aaa', '000111222']

l_start = [s for s in l if s.startswith('t')]
print(l_start)
# ['twoXXXbbb', 'three999aaa']

l_start_not = [s for s in l if not s.startswith('t')]
print(l_start_not)
# ['oneXXXaaa', '000111222']

l_end = [s for s in l if s.endswith('aaa')]
print(l_end)
# ['oneXXXaaa', 'three999aaa']

l_end_not = [s for s in l if not s.endswith('aaa')]
print(l_end_not)
# ['twoXXXbbb', '000111222']

l_lower = [s for s in l if s.islower()]
print(l_lower)
# ['three999aaa']

l_upper_all = [s.upper() for s in l]
print(l_upper_all)
# ['ONEXXXAAA', 'TWOXXXBBB', 'THREE999AAA', '000111222']

l_lower_to_upper = [s.upper() if s.islower() else s for s in l]
print(l_lower_to_upper)
# ['oneXXXaaa', 'twoXXXbbb', 'THREE999AAA', '000111222']

l_isalpha = [s for s in l if s.isalpha()]
print(l_isalpha)
# ['oneXXXaaa', 'twoXXXbbb']

l_isnumeric = [s for s in l if s.isnumeric()]
print(l_isnumeric)
# ['000111222']

l_multi = [s for s in l if s.isalpha() and not s.startswith('t')]
print(l_multi)
# ['oneXXXaaa']

l_multi_or = [s for s in l if (s.isalpha() and not s.startswith('t')) or ('bbb' in s)]
print(l_multi_or)
# ['oneXXXaaa', 'twoXXXbbb']
