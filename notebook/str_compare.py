print('abc' == 'abc')
# True

print('abc' == 'xyz')
# False

print('abc' == 'ABC')
# False

print('abc' != 'xyz')
# True

print('abc' != 'abc')
# False

print('bbb' in 'aaa-bbb-ccc')
# True

print('xxx' in 'aaa-bbb-ccc')
# False

print('abc' in 'aaa-bbb-ccc')
# False

print('xxx' not in 'aaa-bbb-ccc')
# True

print('bbb' not in 'aaa-bbb-ccc')
# False

s = 'aaa-bbb-ccc'

print(s.startswith('aaa'))
# True

print(s.startswith('bbb'))
# False

print(s.startswith(('aaa', 'bbb', 'ccc')))
# True

print(s.startswith(('xxx', 'yyy', 'zzz')))
# False

# print(s.startswith(['a', 'b', 'c']))
# TypeError: startswith first arg must be str or a tuple of str, not list

print(s.endswith('ccc'))
# True

print(s.endswith('bbb'))
# False

print(s.endswith(('aaa', 'bbb', 'ccc')))
# True

print('a' < 'b')
# True

print('aa' < 'ab')
# True

print('abc' < 'abcd')
# True

print(ord('a'))
# 97

print(ord('b'))
# 98

print('Z' < 'a')
# True

print(ord('Z'))
# 90

print('あ' < 'い')
# True

print(ord('あ'))
# 12354

print(ord('い'))
# 12356

print('ん' < 'ア')
# True

print(ord('ん'))
# 12435

print(ord('ア'))
# 12450

print('乙' < '亜')
# True

print(ord('乙'))
# 20057

print(ord('亜'))
# 20124

print('七' < '三')
# True

print(ord('七'))
# 19971

print(ord('三'))
# 19977

print(sorted(['aaa', 'abc', 'Abc', 'ABC']))
# ['ABC', 'Abc', 'aaa', 'abc']

print(sorted('一二三四五六七八九十'))
# ['一', '七', '三', '九', '二', '五', '八', '六', '十', '四']

s1 = 'abc'
s2 = 'ABC'

print(s1 == s2)
# False

print(s1.lower() == s2.lower())
# True

s = 'Abcあいうえお'

print(s.lower())
# abcあいうえお

print(s.upper())
# ABCあいうえお
