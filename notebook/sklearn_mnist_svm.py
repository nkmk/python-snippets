import pandas as pd
from sklearn import datasets, model_selection, svm, metrics

mnist = datasets.fetch_mldata('MNIST original', data_home='data/src/download/')

print(type(mnist))
print(mnist.keys())
# <class 'sklearn.datasets.base.Bunch'>
# dict_keys(['DESCR', 'COL_NAMES', 'target', 'data'])

mnist_data = pd.DataFrame(mnist.data / 255)
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
# 0.71

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
# 0.35409306720248424
# 0.77

clf = svm.LinearSVC()
print(timeit.timeit(lambda: clf.fit(data_train, label_train), number=num) / num)
pre = clf.predict(data_test)
ac_score = metrics.accuracy_score(label_test, pre)
print(ac_score)
# 0.11930906050256454
# 0.77

train_size = 10000
test_size = 2000
data_train, data_test, label_train, label_test = model_selection.train_test_split(mnist_data, mnist_label, test_size=test_size, train_size=train_size)

clf = svm.LinearSVC()
clf.fit(data_train, label_train)
pre = clf.predict(data_test)

ac_score = metrics.accuracy_score(label_test, pre)
print(ac_score)
# 0.8965

co_mat = metrics.confusion_matrix(label_test, pre)
print(co_mat)
# [[162   0   0   2   0   0   0   1   1   0]
#  [  0 249   3   0   0   1   1   1   3   0]
#  [  2   2 183   7   3   1   2   3   4   0]
#  [  1   1  10 178   2   4   0   4   5   2]
#  [  1   2   2   0 158   2   2   0   6   6]
#  [  4   1   2   8   1 160   5   2   2   5]
#  [  3   0   3   1   2   1 176   1   2   0]
#  [  2   0   1   1   3   0   0 187   1  10]
#  [  4   5   2   5   3   3   4   0 167   4]
#  [  0   1   2   1  11   2   0   8   4 173]]
