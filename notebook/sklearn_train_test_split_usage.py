import numpy as np
from sklearn.model_selection import train_test_split

a = np.arange(10)
print(a)
# [0 1 2 3 4 5 6 7 8 9]

print(train_test_split(a))
# [array([8, 4, 9, 0, 6, 7, 2]), array([1, 5, 3])]

print(type(train_test_split(a)))
# <class 'list'>

print(len(train_test_split(a)))
# 2

a_train, a_test = train_test_split(a)

print(a_train)
# [1 5 7 4 6 9 3]

print(a_test)
# [2 8 0]

a_train, a_test = train_test_split(a, test_size=0.6)

print(a_train)
# [1 0 5 2]

print(a_test)
# [7 3 4 6 9 8]

a_train, a_test = train_test_split(a, test_size=6)

print(a_train)
# [7 0 5 3]

print(a_test)
# [4 8 9 2 1 6]

a_train, a_test = train_test_split(a, test_size=0.3, train_size=0.4)

print(a_train)
# [2 8 1 5]

print(a_test)
# [7 6 0]

a_train, a_test = train_test_split(a, test_size=3, train_size=4)

print(a_train)
# [3 7 1 6]

print(a_test)
# [8 0 4]

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
# [[ 6 16]
#  [ 5 15]
#  [ 4 14]
#  [ 2 12]
#  [ 3 13]
#  [ 8 18]
#  [ 1 11]]

print(X_test)
# [[ 7 17]
#  [ 0 10]
#  [ 9 19]]

print(y_train)
# [6 5 4 2 3 8 1]

print(y_test)
# [7 0 9]

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
