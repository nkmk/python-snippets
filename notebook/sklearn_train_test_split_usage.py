import numpy as np
from sklearn.model_selection import train_test_split

a = np.arange(10)
print(a)
# [0 1 2 3 4 5 6 7 8 9]

print(train_test_split(a))
# [array([3, 9, 6, 1, 5, 0, 7]), array([2, 8, 4])]

print(type(train_test_split(a)))
# <class 'list'>

print(len(train_test_split(a)))
# 2

a_train, a_test = train_test_split(a)

print(a_train)
# [3 4 0 5 7 8 2]

print(a_test)
# [6 1 9]

a_train, a_test = train_test_split(a, test_size=0.6)

print(a_train)
# [9 1 2 6]

print(a_test)
# [5 7 4 3 0 8]

a_train, a_test = train_test_split(a, test_size=6)

print(a_train)
# [4 2 1 0]

print(a_test)
# [7 6 3 9 8 5]

a_train, a_test = train_test_split(a, train_size=0.6)

print(a_train)
# [2 9 6 0 4 3]

print(a_test)
# [7 8 5 1]

a_train, a_test = train_test_split(a, train_size=6)

print(a_train)
# [9 3 0 8 7 1]

print(a_test)
# [5 6 4 2]

a_train, a_test = train_test_split(a, train_size=0.25)

print(a_train)
# [1 2]

print(a_test)
# [0 8 4 7 5 6 3 9]

a_train, a_test = train_test_split(a, test_size=0.3, train_size=0.4)

print(a_train)
# [3 0 4 9]

print(a_test)
# [7 2 8]

a_train, a_test = train_test_split(a, test_size=3, train_size=4)

print(a_train)
# [9 7 0 4]

print(a_test)
# [3 8 5]

# a_train, a_test = train_test_split(a, test_size=0.8, train_size=0.7)
# ValueError: The sum of test_size and train_size = 1.500000, should be smaller than 1.0. Reduce test_size and/or train_size.

# a_train, a_test = train_test_split(a, test_size=8, train_size=7)
# ValueError: The sum of train_size and test_size = 15, should be smaller than the number of samples 10. Reduce test_size and/or train_size.

a_train, a_test = train_test_split(a, shuffle=False)

print(a_train)
# [0 1 2 3 4 5 6]

print(a_test)
# [7 8 9]

a_train, a_test = train_test_split(a, random_state=0)

print(a_train)
# [9 1 6 7 3 0 5]

print(a_test)
# [2 8 4]

X = np.arange(20).reshape(2, 10).T
print(X)
# [[ 0 10]
#  [ 1 11]
#  [ 2 12]
#  [ 3 13]
#  [ 4 14]
#  [ 5 15]
#  [ 6 16]
#  [ 7 17]
#  [ 8 18]
#  [ 9 19]]

y = np.arange(10)
print(y)
# [0 1 2 3 4 5 6 7 8 9]

X_train, X_test, y_train, y_test = train_test_split(X, y)

print(X_train)
# [[ 7 17]
#  [ 3 13]
#  [ 0 10]
#  [ 8 18]
#  [ 6 16]
#  [ 4 14]
#  [ 2 12]]

print(X_test)
# [[ 5 15]
#  [ 1 11]
#  [ 9 19]]

print(y_train)
# [7 3 0 8 6 4 2]

print(y_test)
# [5 1 9]

z = np.arange(10) * 10
print(z)
# [ 0 10 20 30 40 50 60 70 80 90]

X_train, X_test, y_train, y_test, z_train, z_test = train_test_split(X, y, z)

print(X_train)
# [[ 6 16]
#  [ 9 19]
#  [ 1 11]
#  [ 2 12]
#  [ 7 17]
#  [ 0 10]
#  [ 3 13]]

print(X_test)
# [[ 8 18]
#  [ 4 14]
#  [ 5 15]]

print(y_train)
# [6 9 1 2 7 0 3]

print(y_test)
# [8 4 5]

print(z_train)
# [60 90 10 20 70  0 30]

print(z_test)
# [80 40 50]

y_mismatch = np.arange(8)
print(y_mismatch)
# [0 1 2 3 4 5 6 7]

# X_train, X_test, y_train, y_test = train_test_split(X, y_mismatch)
# ValueError: Found input variables with inconsistent numbers of samples: [10, 8]

y = np.array([0] * 5 + [1] * 5)
print(y)
# [0 0 0 0 0 1 1 1 1 1]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=100)

print(y_train)
# [0 1 0 0 0 0 1 1]

print(y_test)
# [1 1]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=100,
                                                    stratify=y)

print(y_train)
# [1 1 0 0 0 1 1 0]

print(y_test)
# [1 0]
