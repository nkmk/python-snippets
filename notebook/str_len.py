s = 'abcde'

print(len(s))
# 5

s_length = len(s)

print(s_length)
# 5

print(type(s_length))
# <class 'int'>

s = 'あいうえお'

print(len(s))
# 5

s = 'abcdeあいうえお'

print(len(s))
# 10

s = 'a\tb\\c'
print(s)
# a	b\c

print(len(s))
# 5

s = r'a\tb\\c'
print(s)
# a\tb\\c

print(len(s))
# 7

s = '\u3042\u3044\u3046'
print(s)
# あいう

print(len(s))
# 3

s = r'\u3042\u3044\u3046'
print(s)
# \u3042\u3044\u3046

print(len(s))
# 18

s = 'a\nb'
print(s)
# a
# b

print(len(s))
# 3

s = 'a\r\nb'
print(s)
# a
# b

print(len(s))
# 4

s = 'abc\nabcd\r\nab'
print(s)
# abc
# abcd
# ab

print(len(s))
# 12

print(s.splitlines())
# ['abc', 'abcd', 'ab']

print(len(s.splitlines()))
# 3

print([len(line) for line in s.splitlines()])
# [3, 4, 2]

print(sum(len(line) for line in s.splitlines()))
# 9
