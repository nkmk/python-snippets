import pandas as pd
from sklearn.datasets import load_iris

data = load_iris()

print(type(data))
# <class 'sklearn.utils.Bunch'>

print(issubclass(type(data), dict))
# True

print(data.keys())
# dict_keys(['data', 'target', 'target_names', 'DESCR', 'feature_names', 'filename'])

print(data['feature_names'])
# ['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)']

print(data.feature_names)
# ['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)']

print(data.filename)
# /usr/local/lib/python3.7/site-packages/sklearn/datasets/data/iris.csv

print(data.DESCR)
# .. _iris_dataset:
# 
# Iris plants dataset
# --------------------
# 
# **Data Set Characteristics:**
# 
#     :Number of Instances: 150 (50 in each of three classes)
#     :Number of Attributes: 4 numeric, predictive attributes and the class
#     :Attribute Information:
#         - sepal length in cm
#         - sepal width in cm
#         - petal length in cm
#         - petal width in cm
#         - class:
#                 - Iris-Setosa
#                 - Iris-Versicolour
#                 - Iris-Virginica
#                 
#     :Summary Statistics:
# 
#     ============== ==== ==== ======= ===== ====================
#                     Min  Max   Mean    SD   Class Correlation
#     ============== ==== ==== ======= ===== ====================
#     sepal length:   4.3  7.9   5.84   0.83    0.7826
#     sepal width:    2.0  4.4   3.05   0.43   -0.4194
#     petal length:   1.0  6.9   3.76   1.76    0.9490  (high!)
#     petal width:    0.1  2.5   1.20   0.76    0.9565  (high!)
#     ============== ==== ==== ======= ===== ====================
# 
#     :Missing Attribute Values: None
#     :Class Distribution: 33.3% for each of 3 classes.
#     :Creator: R.A. Fisher
#     :Donor: Michael Marshall (MARSHALL%PLU@io.arc.nasa.gov)
#     :Date: July, 1988
# 
# The famous Iris database, first used by Sir R.A. Fisher. The dataset is taken
# from Fisher's paper. Note that it's the same as in R, but not as in the UCI
# Machine Learning Repository, which has two wrong data points.
# 
# This is perhaps the best known database to be found in the
# pattern recognition literature.  Fisher's paper is a classic in the field and
# is referenced frequently to this day.  (See Duda & Hart, for example.)  The
# data set contains 3 classes of 50 instances each, where each class refers to a
# type of iris plant.  One class is linearly separable from the other 2; the
# latter are NOT linearly separable from each other.
# 
# .. topic:: References
# 
#    - Fisher, R.A. "The use of multiple measurements in taxonomic problems"
#      Annual Eugenics, 7, Part II, 179-188 (1936); also in "Contributions to
#      Mathematical Statistics" (John Wiley, NY, 1950).
#    - Duda, R.O., & Hart, P.E. (1973) Pattern Classification and Scene Analysis.
#      (Q327.D83) John Wiley & Sons.  ISBN 0-471-22361-1.  See page 218.
#    - Dasarathy, B.V. (1980) "Nosing Around the Neighborhood: A New System
#      Structure and Classification Rule for Recognition in Partially Exposed
#      Environments".  IEEE Transactions on Pattern Analysis and Machine
#      Intelligence, Vol. PAMI-2, No. 1, 67-71.
#    - Gates, G.W. (1972) "The Reduced Nearest Neighbor Rule".  IEEE Transactions
#      on Information Theory, May 1972, 431-433.
#    - See also: 1988 MLC Proceedings, 54-64.  Cheeseman et al"s AUTOCLASS II
#      conceptual clustering system finds 3 classes in the data.
#    - Many, many more ...

X = data.data
y = data.target

print(type(X))
# <class 'numpy.ndarray'>

print(X.shape)
# (150, 4)

print(X[:5])
# [[5.1 3.5 1.4 0.2]
#  [4.9 3.  1.4 0.2]
#  [4.7 3.2 1.3 0.2]
#  [4.6 3.1 1.5 0.2]
#  [5.  3.6 1.4 0.2]]

print(type(y))
# <class 'numpy.ndarray'>

print(y.shape)
# (150,)

print(y)
# [0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
#  0 0 0 0 0 0 0 0 0 0 0 0 0 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
#  1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 2 2 2 2 2 2 2 2 2 2 2
#  2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2
#  2 2]

df_X = pd.DataFrame(data.data, columns=data.feature_names)

print(df_X.head())
#    sepal length (cm)  sepal width (cm)  petal length (cm)  petal width (cm)
# 0                5.1               3.5                1.4               0.2
# 1                4.9               3.0                1.4               0.2
# 2                4.7               3.2                1.3               0.2
# 3                4.6               3.1                1.5               0.2
# 4                5.0               3.6                1.4               0.2

s_y = pd.Series(data.target)

print(s_y.head())
# 0    0
# 1    0
# 2    0
# 3    0
# 4    0
# dtype: int64

print(df_X.describe())
#        sepal length (cm)  sepal width (cm)  petal length (cm)  \
# count         150.000000        150.000000         150.000000   
# mean            5.843333          3.057333           3.758000   
# std             0.828066          0.435866           1.765298   
# min             4.300000          2.000000           1.000000   
# 25%             5.100000          2.800000           1.600000   
# 50%             5.800000          3.000000           4.350000   
# 75%             6.400000          3.300000           5.100000   
# max             7.900000          4.400000           6.900000   
# 
#        petal width (cm)  
# count        150.000000  
# mean           1.199333  
# std            0.762238  
# min            0.100000  
# 25%            0.300000  
# 50%            1.300000  
# 75%            1.800000  
# max            2.500000  

print(s_y.value_counts())
# 2    50
# 1    50
# 0    50
# dtype: int64

X, y = load_iris(return_X_y=True)

print(type(X))
# <class 'numpy.ndarray'>

print(X.shape)
# (150, 4)

print(type(y))
# <class 'numpy.ndarray'>

print(y.shape)
# (150,)
