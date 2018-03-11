import numpy as np

a = np.array([1, 2, 3], dtype=np.int64)
print(a.dtype)
# int64

a = np.array([1, 2, 3], dtype='int64')
print(a.dtype)
# int64

a = np.array([1, 2, 3], dtype='i8')
print(a.dtype)
# int64

print(int is np.int)
# True

a = np.array([1, 2, 3], dtype=int)
print(a.dtype)
# int64

a = np.array([1, 2, 3], dtype='int')
print(a.dtype)
# int64

a_str = np.array([1, 2, 3], dtype=str)
print(a_str)
print(a_str.dtype)
# ['1' '2' '3']
# <U1

a_str[0] = 'abcde'
print(a_str)
# ['a' '2' '3']

a_str10 = np.array([1, 2, 3], dtype='U10')
print(a_str10.dtype)
# <U10

a_str10[0] = 'abcde'
print(a_str10)
# ['abcde' '2' '3']

a_object = np.array([1, 0.1, 'one'], dtype=object)
print(a_object)
print(a_object.dtype)
# [1 0.1 'one']
# object

print(type(a_object[0]))
print(type(a_object[1]))
print(type(a_object[2]))
# <class 'int'>
# <class 'float'>
# <class 'str'>

a_object[2] = 'oneONE'
print(a_object)
# [1 0.1 'oneONE']

l = [1, 0.1, 'oneONE']
print(type(l[0]))
print(type(l[1]))
print(type(l[2]))
# <class 'int'>
# <class 'float'>
# <class 'str'>

print(a_object * 2)
# [2 0.2 'oneONEoneONE']

print(l * 2)
# [1, 0.1, 'oneONE', 1, 0.1, 'oneONE']
