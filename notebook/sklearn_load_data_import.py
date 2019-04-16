import sklearn.datasets

data_iris = sklearn.datasets.load_iris()

print(type(data_iris))
# <class 'sklearn.utils.Bunch'>

data_boston = sklearn.datasets.load_boston()

print(type(data_boston))
# <class 'sklearn.utils.Bunch'>
