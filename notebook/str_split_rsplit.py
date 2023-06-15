s_blank = 'one two   three\nfour\tfive'
print(s_blank)
# one two   three
# four	five

print(s_blank.split())
# ['one', 'two', 'three', 'four', 'five']

print(type(s_blank.split()))
# <class 'list'>

s_comma = 'one,two,three,four,five'
print(s_comma.split(','))
# ['one', 'two', 'three', 'four', 'five']

print(s_comma.split('three'))
# ['one,two,', ',four,five']

s_hyphen = '-one--two-'
print(s_hyphen.split('-'))
# ['', 'one', '', 'two', '']

print([s for s in s_hyphen.split('-') if s])
# ['one', 'two']

s_blank = ' one two  three '
print(s_blank.split())
# ['one', 'two', 'three']

print(s_blank.split(' '))
# ['', 'one', 'two', '', 'three', '']

s_comma = 'one,two,three,four,five'
print(s_comma.split(',', 2))
# ['one', 'two', 'three,four,five']

print(s_comma.split(',', 10))
# ['one', 'two', 'three', 'four', 'five']

s_comma = 'one,two,three,four,five'
print(s_comma.rsplit(','))
# ['one', 'two', 'three', 'four', 'five']

print(s_comma.rsplit(',', 2))
# ['one,two,three', 'four', 'five']

print(s_comma.rsplit(',', 10))
# ['one', 'two', 'three', 'four', 'five']

s_lines_multi = '1 one\n2 two\r\n3 three\n'
print(s_lines_multi)
# 1 one
# 2 two
# 3 three
# 

print(s_lines_multi.split())
# ['1', 'one', '2', 'two', '3', 'three']

print(s_lines_multi.split('\n'))
# ['1 one', '2 two\r', '3 three', '']

print(s_lines_multi.splitlines())
# ['1 one', '2 two', '3 three']

print(s_lines_multi.splitlines(True))
# ['1 one\n', '2 two\r\n', '3 three\n']

s = 'abcdefghij'
print(s[:5])
# abcde

print(s[5:])
# fghij

s_tuple = s[:5], s[5:]
print(s_tuple)
# ('abcde', 'fghij')

print(type(s_tuple))
# <class 'tuple'>

s_first, s_last = s[:5], s[5:]
print(s_first)
# abcde

print(s_last)
# fghij

s_first, s_second, s_last = s[:3], s[3:6], s[6:]
print(s_first)
# abc

print(s_second)
# def

print(s_last)
# ghij

half = len(s) // 2
print(half)
# 5

s_first, s_last = s[:half], s[half:]
print(s_first)
# abcde

print(s_last)
# fghij

print(s_first + s_last)
# abcdefghij
