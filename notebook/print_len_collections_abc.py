import collections

def print_len_abc_sized(x):
    if isinstance(x, collections.abc.Sized):
        print(len(x))
    else:
        print('x is not Sized')

print_len_abc_sized([0, 1, 2])
# 3

print_len_abc_sized('abc')
# 3

print_len_abc_sized({0, 1, 2})
# 3

print_len_abc_sized(100)
# x is not Sized

def print_len_abc_sequence(x):
    if isinstance(x, collections.abc.Sequence):
        print(len(x))
    else:
        print('x is not Sequence')

print_len_abc_sequence([0, 1, 2])
# 3

print_len_abc_sequence('abc')
# 3

print_len_abc_sequence({0, 1, 2})
# x is not Sequence

print_len_abc_sequence({'k1': 1, 'k2': 2, 'k3': 3})
# x is not Sequence

def print_len_abc_mutablesequence(x):
    if isinstance(x, collections.abc.MutableSequence):
        print(len(x))
    else:
        print('x is not MutableSequence')

print_len_abc_mutablesequence([0, 1, 2])
# 3

print_len_abc_mutablesequence('abc')
# x is not MutableSequence

print_len_abc_mutablesequence((0, 1, 2))
# x is not MutableSequence

class MySequence(collections.abc.Sequence):
    def __len__(self):
        return 10

# ms = MySequence()
# TypeError: Can't instantiate abstract class MySequence with abstract methods __getitem__

class MySequence(collections.abc.Sequence):
    def __len__(self):
        return 10

    def __getitem__(self, i):
        return i

ms = MySequence()

print(len(ms))
# 10

print(ms[3])
# 3

print(ms.index(5))
# 5

print(list(reversed(ms)))
# [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

print(isinstance(ms, collections.abc.Sequence))
# True

print(hasattr(ms, '__len__'))
# True

class MySequence_bare():
    def __len__(self):
        return 10

    def __getitem__(self, i):
        return i

msb = MySequence_bare()

print(len(msb))
# 10

print(msb[3])
# 3

# print(msb.index(5))
# AttributeError: 'MySequence_bare' object has no attribute 'index'

print(isinstance(msb, collections.abc.Sequence))
# False

print(hasattr(msb, '__len__'))
# True
