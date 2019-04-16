from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris

data = load_iris()

X = data['data']
y = data['target']

print(X.shape)
# (150, 4)

print(X[:5])
# [[5.1 3.5 1.4 0.2]
#  [4.9 3.  1.4 0.2]
#  [4.7 3.2 1.3 0.2]
#  [4.6 3.1 1.5 0.2]
#  [5.  3.6 1.4 0.2]]

print(y.shape)
# (150,)

print(y)
# [0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
#  0 0 0 0 0 0 0 0 0 0 0 0 0 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
#  1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 2 2 2 2 2 2 2 2 2 2 2
#  2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2
#  2 2]

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

print(X_train.shape)
# (112, 4)

print(X_test.shape)
# (38, 4)

print(y_train.shape)
# (112,)

print(y_test.shape)
# (38,)

print(y_test)
# [2 1 0 2 0 2 0 1 1 1 2 1 1 1 1 0 1 1 0 0 2 1 0 0 2 0 0 1 1 0 2 1 0 2 2 1 0
#  1]

print((y_test == 0).sum())
# 13

print((y_test == 1).sum())
# 16

print((y_test == 2).sum())
# 9

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0, stratify=y)

print(y_test)
# [0 0 0 0 1 1 1 0 1 2 2 2 1 2 1 0 0 2 0 1 2 1 1 0 2 0 0 1 2 1 0 1 2 2 0 1 2
#  2]

print((y_test == 0).sum())
# 13

print((y_test == 1).sum())
# 13

print((y_test == 2).sum())
# 12
