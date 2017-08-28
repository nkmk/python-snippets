# https://docs.python.jp/3/library/functions.html?highlight=bool#bool
# https://docs.python.jp/3/library/stdtypes.html#truth

print(bool('True'))
print(bool('False'))
print(bool('foo'))
print(bool(''))
# True
# True
# True
# False

print(bool(1))
print(bool(2))
print(bool(1.23))
print(bool(-1))
print(bool(0))
# True
# True
# True
# True
# False

print(bool([1, 2, 3]))
print(bool([]))
# True
# False

print(bool(None))
# False
