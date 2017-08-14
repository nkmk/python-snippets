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
# 0.66

train_size = 5000
test_size = 1000
data_train, data_test, label_train, label_test = model_selection.train_test_split(mnist_data, mnist_label, test_size=test_size, train_size=train_size)

clf = svm.SVC()
clf.fit(data_train, label_train)
pre = clf.predict(data_test)

ac_score = metrics.accuracy_score(label_test, pre)
print(ac_score)
# 0.907
