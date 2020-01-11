import numpy as np

a = np.arange(16).reshape(4, 4)
print(a)
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]
#  [12 13 14 15]]

print(np.tril(a))
# [[ 0  0  0  0]
#  [ 4  5  0  0]
#  [ 8  9 10  0]
#  [12 13 14 15]]

print(np.triu(a))
# [[ 0  1  2  3]
#  [ 0  5  6  7]
#  [ 0  0 10 11]
#  [ 0  0  0 15]]

print(np.tril(a).T)
# [[ 0  4  8 12]
#  [ 0  5  9 13]
#  [ 0  0 10 14]
#  [ 0  0  0 15]]

print(np.tril(a) + np.tril(a).T)
# [[ 0  4  8 12]
#  [ 4 10  9 13]
#  [ 8  9 20 14]
#  [12 13 14 30]]

print(a.diagonal())
# [ 0  5 10 15]

print(np.diag(a.diagonal()))
# [[ 0  0  0  0]
#  [ 0  5  0  0]
#  [ 0  0 10  0]
#  [ 0  0  0 15]]

print(np.tril(a) + np.tril(a).T - np.diag(a.diagonal()))
# [[ 0  4  8 12]
#  [ 4  5  9 13]
#  [ 8  9 10 14]
#  [12 13 14 15]]

def get_symmetric(a, use_tril=True):
    if use_tril:
        a = np.tril(a)
    else:
        a = np.triu(a)
    return a + a.T - np.diag(a.diagonal())

print(get_symmetric(a))
# [[ 0  4  8 12]
#  [ 4  5  9 13]
#  [ 8  9 10 14]
#  [12 13 14 15]]

print(get_symmetric(a, False))
# [[ 0  1  2  3]
#  [ 1  5  6  7]
#  [ 2  6 10 11]
#  [ 3  7 11 15]]

def is_symmetric(a):
    return np.array_equal(a, a.T)

a_sym = get_symmetric(a)
print(a_sym)
# [[ 0  4  8 12]
#  [ 4  5  9 13]
#  [ 8  9 10 14]
#  [12 13 14 15]]

print(is_symmetric(a_sym))
# True

print(is_symmetric(a))
# False

def get_skew_symmetric(a, use_tril=True):
    if use_tril:
        a = np.tril(a)
    else:
        a = np.triu(a)
    return a - a.T

print(get_skew_symmetric(a))
# [[  0  -4  -8 -12]
#  [  4   0  -9 -13]
#  [  8   9   0 -14]
#  [ 12  13  14   0]]

print(get_skew_symmetric(a, False))
# [[  0   1   2   3]
#  [ -1   0   6   7]
#  [ -2  -6   0  11]
#  [ -3  -7 -11   0]]

def is_skew_symmetric(a):
    return np.array_equal(a, -a.T)

a_sk_sym = get_skew_symmetric(a)
print(a_sk_sym)
# [[  0  -4  -8 -12]
#  [  4   0  -9 -13]
#  [  8   9   0 -14]
#  [ 12  13  14   0]]

print(is_skew_symmetric(a_sk_sym))
# True

print(is_skew_symmetric(a))
# False
