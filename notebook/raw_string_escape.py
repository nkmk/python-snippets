s = 'a\tb\nA\tB'
print(s)
# a	b
# A	B

rs = r'a\tb\nA\tB'
print(rs)
# a\tb\nA\tB

print(type(rs))
# <class 'str'>

print(rs == 'a\\tb\\nA\\tB')
# True

print(len(s))
# 7

print(list(s))
# ['a', '\t', 'b', '\n', 'A', '\t', 'B']

print(len(rs))
# 10

print(list(rs))
# ['a', '\\', 't', 'b', '\\', 'n', 'A', '\\', 't', 'B']

path = 'C:\\Windows\\system32\\cmd.exe'
rpath = r'C:\Windows\system32\cmd.exe'
print(path == rpath)
# True

path2 = 'C:\\Windows\\system32\\'
# rpath2 = r'C:\Windows\system32\'
# SyntaxError: EOL while scanning string literal
rpath2 = r'C:\Windows\system32' + '\\'
print(path2 == rpath2)
# True

s_r = repr(s)
print(s_r)
# 'a\tb\nA\tB'

print(list(s_r))
# ["'", 'a', '\\', 't', 'b', '\\', 'n', 'A', '\\', 't', 'B', "'"]

s_r2 = repr(s)[1:-1]
print(s_r2)
# a\tb\nA\tB

print(s_r2 == rs)
# True

print(r'\t' == repr('\t')[1:-1])
# True

# print(r'\')
# SyntaxError: EOL while scanning string literal

print(r'\\')
# \\

# print(r'\\\')
# SyntaxError: EOL while scanning string literal
