def test():
    return 'abc', 100

result = test()

print(result)
print(type(result))
# ('abc', 100)
# <class 'tuple'>

print(result[0])
print(type(result[0]))
# abc
# <class 'str'>

print(result[1])
print(type(result[1]))
# 100
# <class 'int'>

# print(result[2])
# IndexError: tuple index out of range

a, b = test()

print(a)
# abc

print(b)
# 100

def test2():
    return 'abc', 100, [0, 1, 2]

a, b, c = test2()

print(a)
# abc

print(b)
# 100

print(c)
# [0, 1, 2]

def test_list():
    return ['abc', 100]

result = test_list()

print(result)
print(type(result))
# ['abc', 100]
# <class 'list'>
