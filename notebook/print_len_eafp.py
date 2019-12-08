import numpy as np

def print_len_eafp(x):
    try:
        print(len(x))
    except TypeError as e:
        print(e)

print_len_eafp([0, 1, 2])
# 3

print_len_eafp(100)
# object of type 'int' has no len()

print_len_eafp((0, 1, 2))
# 3

print_len_eafp('abc')
# 3

a = np.arange(3)
print(a)
# [0 1 2]

print_len_eafp(a)
# 3
