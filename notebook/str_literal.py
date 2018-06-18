s = 'abc'
print(s)
# abc

print(type(s))
# <class 'str'>

s = "abc"
print(s)
# abc

print(type(s))
# <class 'str'>

s_sq = 'abc'
s_dq = "abc"

print(s_sq == s_dq)
# True

s_sq = 'a\'b"c'
print(s_sq)
# a'b"c

s_sq = 'a\'b\"c'
print(s_sq)
# a'b"c

s_dq = "a'b\"c"
print(s_dq)
# a'b"c

s_dq = "a\'b\"c"
print(s_dq)
# a'b"c

s_sq = 'a\'b"c'
s_dq = "a'b\"c"

print(s_sq == s_dq)
# True

# s = 'abc
# xyz'
# SyntaxError: EOL while scanning string literal

s = 'abc\nxyz'
print(s)
# abc
# xyz

s_tq = '''abc
xyz'''

print(s_tq)
# abc
# xyz

print(type(s_tq))
# <class 'str'>

s_tq = '''abc'''
print(s_tq)
# abc

s_tq_sq = '''\'abc\'
"xyz"'''

print(s_tq_sq)
# 'abc'
# "xyz"

s_tq_dq = """'abc'
\"xyz\""""

print(s_tq_dq)
# 'abc'
# "xyz"

print(s_tq_sq == s_tq_dq)
# True

s_tq = '''abc
          xyz'''

print(s_tq)
# abc
#           xyz

s_multi = ('abc\n'
           'xyz')

print(s_multi)
# abc
# xyz
