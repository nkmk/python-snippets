from sklearn import datasets, model_selection, svm, metrics

mnist = datasets.fetch_mldata('MNIST original', data_home='data/src/download/')

print(type(mnist))
print(mnist.keys())
# <class 'sklearn.datasets.base.Bunch'>
# dict_keys(['DESCR', 'COL_NAMES', 'target', 'data'])

mnist_data = mnist.data / 255
mnist_label = mnist.target

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
# 0.77

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
# 0.3631532890023664
# 0.73

clf = svm.LinearSVC()
print(timeit.timeit(lambda: clf.fit(data_train, label_train), number=num) / num)
pre = clf.predict(data_test)
ac_score = metrics.accuracy_score(label_test, pre)
print(ac_score)
# 0.10481857029953971
# 0.76

train_size = 10000
test_size = 2000
data_train, data_test, label_train, label_test = model_selection.train_test_split(mnist_data, mnist_label, test_size=test_size, train_size=train_size)

clf = svm.LinearSVC()
print(timeit.timeit(lambda: clf.fit(data_train, label_train), number=num) / num)
pre = clf.predict(data_test)

ac_score = metrics.accuracy_score(label_test, pre)
print(ac_score)
# 5.980748841702007
# 0.8945

co_mat = metrics.confusion_matrix(label_test, pre)
print(co_mat)
# [[186   0   0   2   1   1   0   1   2   0]
#  [  0 210   1   0   1   2   2   1   3   0]
#  [  1   3 192   8   2   6   2   3   5   3]
#  [  1   1   7 163   0   6   1   1   7   2]
#  [  1   0   1   0 166   1   2   2   1   6]
#  [  5   3   1   6   5 168   7   3   6   3]
#  [  1   0   4   0   1   4 170   0   3   0]
#  [  1   1   3   2   2   0   0 196   0   6]
#  [  0   4   3   3   3  13   1   1 162   6]
#  [  2   1   0   2   5   2   0   6   2 176]]
