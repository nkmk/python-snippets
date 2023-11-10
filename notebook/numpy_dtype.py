import numpy as np

print(np.__version__)
# 1.26.1

a = np.array([1, 2, 3], dtype=np.int64)
print(a.dtype)
# int64

a = np.array([1, 2, 3], dtype='int64')
print(a.dtype)
# int64

a = np.array([1, 2, 3], dtype='i8')
print(a.dtype)
# int64

a = np.array([1, 2, 3], dtype=int)
print(a.dtype)
# int64

a = np.array([1, 2, 3], dtype='int')
print(a.dtype)
# int64

a_str = np.array([1, 22, 333], dtype=str)
print(a_str)
# ['1' '22' '333']

print(a_str.dtype)
# <U3

a_str[0] = 'abcde'
print(a_str)
# ['abc' '22' '333']

a_str10 = np.array([1, 22, 333], dtype='U10')
print(a_str10.dtype)
# <U10

a_str10[0] = 'abcde'
print(a_str10)
# ['abcde' '22' '333']

a_object = np.array([1, 0.1, 'abc'], dtype=object)
print(a_object)
# [1 0.1 'abc']

print(a_object.dtype)
# object

print(type(a_object[0]))
print(type(a_object[1]))
print(type(a_object[2]))
# <class 'int'>
# <class 'float'>
# <class 'str'>

a_object[2] = 'abcXYZ'
print(a_object)
# [1 0.1 'abcXYZ']

l = [1, 0.1, 'abcXYZ']

print(type(l))
# <class 'list'>

print(type(l[0]))
print(type(l[1]))
print(type(l[2]))
# <class 'int'>
# <class 'float'>
# <class 'str'>

print(a_object * 2)
# [2 0.2 'abcXYZabcXYZ']

print(l * 2)
# [1, 0.1, 'abcXYZ', 1, 0.1, 'abcXYZ']
