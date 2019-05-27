import builtins

print(len('abc'))
# 3

print(builtins.len('abc'))
# 3

print(len)
# <built-in function len>

print(builtins.len)
# <built-in function len>

print(builtins.len is len)
# True

print(__builtins__.len('abc'))
# 3

print(__builtins__.len is len)
# True

print(__builtins__ is builtins)
# True
