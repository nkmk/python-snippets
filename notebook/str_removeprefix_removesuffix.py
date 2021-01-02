s = 'abc-abcxyz'

print(s.removeprefix('abc-'))
# abcxyz

print(s.removeprefix('aabc-'))
# abc-abcxyz

print(s.lstrip('abc-'))
# xyz

def my_removeprefix(s, prefix):
    if s.startswith(prefix):
        return s[len(prefix):]
    else:
        return s

print(my_removeprefix(s, 'abc-'))
# abcxyz

s = 'abcxyz-xyz'

print(s.removesuffix('-xyz'))
# abcxyz

print(s.removesuffix('-xyzz'))
# abcxyz-xyz

def my_removesuffix(s, suffix):
    return s[:-len(suffix)] if s.endswith(suffix) else s

print(my_removesuffix(s, '-xyz'))
# abcxyz

s = 'abc-abcxyz-xyz'

print(s.removeprefix('abc-').removesuffix('-xyz'))
# abcxyz

print(my_removeprefix(my_removesuffix(s, '-xyz'), 'abc-'))
# abcxyz
