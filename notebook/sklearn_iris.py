import pandas as pd
from sklearn import datasets, model_selection, svm, metrics

# http://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_iris.html
# http://scikit-learn.org/stable/auto_examples/datasets/plot_iris_dataset.html
iris = datasets.load_iris()

print(type(iris))
print(iris.keys())
# <class 'sklearn.datasets.base.Bunch'>
# dict_keys(['data', 'target', 'target_names', 'DESCR', 'feature_names'])

iris_data = pd.DataFrame(data=iris.data, columns=iris.feature_names)
print(iris_data.head())
#    sepal length (cm)  sepal width (cm)  petal length (cm)  petal width (cm)
# 0                5.1               3.5                1.4               0.2
# 1                4.9               3.0                1.4               0.2
# 2                4.7               3.2                1.3               0.2
# 3                4.6               3.1                1.5               0.2
# 4                5.0               3.6                1.4               0.2

iris_label = pd.Series(data=iris.target)
print(iris_label.head())
# 0    0
# 1    0
# 2    0
# 3    0
# 4    0
# dtype: int64

print(len(iris_data))
# 150

# http://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html
data_train, data_test, label_train, label_test = model_selection.train_test_split(iris_data, iris_label)

print(data_train.head())
#      sepal length (cm)  sepal width (cm)  petal length (cm)  petal width (cm)
# 55                 5.7               2.8                4.5               1.3
# 128                6.4               2.8                5.6               2.1
# 142                5.8               2.7                5.1               1.9
# 97                 6.2               2.9                4.3               1.3
# 130                7.4               2.8                6.1               1.9

print(label_train.head())
# 55     1
# 128    2
# 142    2
# 97     1
# 130    2
# dtype: int64

# default value of test_size = 0.25
print(len(data_train), len(data_test))
# 112 38

clf = svm.SVC()
clf.fit(data_train, label_train)
pre = clf.predict(data_test)

print(type(pre))
print(pre)
# <class 'numpy.ndarray'>
# [0 0 1 1 0 0 0 0 0 2 1 0 0 0 2 1 1 2 2 2 2 1 0 1 1 1 2 0 2 2 0 2 0 2 0 1 0
#  0]

# http://scikit-learn.org/stable/modules/generated/sklearn.metrics.accuracy_score.html
ac_score = metrics.accuracy_score(label_test, pre)

print(ac_score)
# 0.973684210526
