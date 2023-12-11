l = [0, 1, 2]

print(len(l))
# 3

t = (0, 1, 2)

print(len(t))
# 3

s = {0, 1, 2}

print(len(s))
# 3

d = {'key_0': 0, 'key_1': 1, 'key_2': 2}

print(len(d))
# 3

s = 'abcde'

print(len(s))
# 5

s = 'あいうえお'

print(len(s))
# 5

l = [0, 1, 2]

print(l.__len__())
# 3

s = 'abcde'

print(s.__len__())
# 5

i = 100

print(hasattr(i, '__len__'))
# False

# print(len(i))
# TypeError: object of type 'int' has no len()

class MyClass:
    def __len__(self):
        return 100

mc = MyClass()

print(len(mc))
# 100
