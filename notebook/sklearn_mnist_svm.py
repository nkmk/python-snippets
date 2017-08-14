import pandas as pd
from sklearn import datasets, model_selection, svm, metrics

mnist = datasets.fetch_mldata('MNIST original', data_home='data/src/download/')

print(type(mnist))
print(mnist.keys())
# <class 'sklearn.datasets.base.Bunch'>
# dict_keys(['DESCR', 'COL_NAMES', 'target', 'data'])

mnist_data = pd.DataFrame(mnist.data / 256)
mnist_label = pd.Series(mnist.target)

print(mnist_data.shape)
print(mnist_label.shape)
# (70000, 784)
# (70000,)

train_size = 500
test_size = 100
data_train, data_test, label_train, label_test = model_selection.train_test_split(mnist_data, mnist_label, test_size=test_size, train_size=train_size)

clf = svm.SVC()
clf.fit(data_train, label_train)
pre = clf.predict(data_test)

ac_score = metrics.accuracy_score(label_test, pre)
print(ac_score)
# 0.73

import timeit

num = 10

train_size = 500
test_size = 100
data_train, data_test, label_train, label_test = model_selection.train_test_split(mnist_data, mnist_label, test_size=test_size, train_size=train_size)

clf = svm.SVC()
print(timeit.timeit(lambda: clf.fit(data_train, label_train), number=num) / num)
pre = clf.predict(data_test)
ac_score = metrics.accuracy_score(label_test, pre)
print(ac_score)
# 0.35348284359788523
# 0.79

clf = svm.LinearSVC()
print(timeit.timeit(lambda: clf.fit(data_train, label_train), number=num) / num)
pre = clf.predict(data_test)
ac_score = metrics.accuracy_score(label_test, pre)
print(ac_score)
# 0.10056947720004246
# 0.77

train_size = 10000
test_size = 2000
data_train, data_test, label_train, label_test = model_selection.train_test_split(mnist_data, mnist_label, test_size=test_size, train_size=train_size)

clf = svm.LinearSVC()
clf.fit(data_train, label_train)
pre = clf.predict(data_test)

ac_score = metrics.accuracy_score(label_test, pre)
print(ac_score)
# 0.8805

co_mat = metrics.confusion_matrix(label_test, pre)
print(co_mat)
# [[187   0   4   1   0   2   1   1   2   0]
#  [  0 229   3   4   0   1   1   0   2   0]
#  [  1   3 152   5   1   1   1   3   8   2]
#  [  2   4  11 178   0   4   0   1   6   7]
#  [  3   2   5   1 182   0   2   1   0  10]
#  [  2   2   0   8   3 150   6   1   8   3]
#  [  3   2   1   0   1   1 192   0   5   0]
#  [  0   3   4   0   1   5   0 192   0   8]
#  [  0   2   3   5   2   6   2   0 140   6]
#  [  6   1   0   3  13   5   0  11   1 159]]
