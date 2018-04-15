import pandas as pd

s = pd.Series(data=[x**2 for x in range(11)],
              index=list('abcdefghijk'))

print(s)
# a      0
# b      1
# c      4
# d      9
# e     16
# f     25
# g     36
# h     49
# i     64
# j     81
# k    100
# dtype: int64

s_cut = pd.cut(s, 4)
print(s_cut)
# a     (-0.1, 25.0]
# b     (-0.1, 25.0]
# c     (-0.1, 25.0]
# d     (-0.1, 25.0]
# e     (-0.1, 25.0]
# f     (-0.1, 25.0]
# g     (25.0, 50.0]
# h     (25.0, 50.0]
# i     (50.0, 75.0]
# j    (75.0, 100.0]
# k    (75.0, 100.0]
# dtype: category
# Categories (4, interval[float64]): [(-0.1, 25.0] < (25.0, 50.0] < (50.0, 75.0] < (75.0, 100.0]]

print(type(s_cut))
# <class 'pandas.core.series.Series'>

print(pd.cut(s, [0, 10, 50, 100]))
# a          NaN
# b      (0, 10]
# c      (0, 10]
# d      (0, 10]
# e     (10, 50]
# f     (10, 50]
# g     (10, 50]
# h     (10, 50]
# i    (50, 100]
# j    (50, 100]
# k    (50, 100]
# dtype: category
# Categories (3, interval[int64]): [(0, 10] < (10, 50] < (50, 100]]

s_cut, bins = pd.cut(s, 4, retbins=True)
print(s_cut)
# a     (-0.1, 25.0]
# b     (-0.1, 25.0]
# c     (-0.1, 25.0]
# d     (-0.1, 25.0]
# e     (-0.1, 25.0]
# f     (-0.1, 25.0]
# g     (25.0, 50.0]
# h     (25.0, 50.0]
# i     (50.0, 75.0]
# j    (75.0, 100.0]
# k    (75.0, 100.0]
# dtype: category
# Categories (4, interval[float64]): [(-0.1, 25.0] < (25.0, 50.0] < (50.0, 75.0] < (75.0, 100.0]]

print(bins)
print(type(bins))
# [ -0.1  25.   50.   75.  100. ]
# <class 'numpy.ndarray'>

print(pd.cut(s, 4, right=False))
# a      [0.0, 25.0)
# b      [0.0, 25.0)
# c      [0.0, 25.0)
# d      [0.0, 25.0)
# e      [0.0, 25.0)
# f     [25.0, 50.0)
# g     [25.0, 50.0)
# h     [25.0, 50.0)
# i     [50.0, 75.0)
# j    [75.0, 100.1)
# k    [75.0, 100.1)
# dtype: category
# Categories (4, interval[float64]): [[0.0, 25.0) < [25.0, 50.0) < [50.0, 75.0) < [75.0, 100.1)]

print(pd.cut(s, 4, labels=False))
# a    0
# b    0
# c    0
# d    0
# e    0
# f    0
# g    1
# h    1
# i    2
# j    3
# k    3
# dtype: int64

print(pd.cut(s, 4, labels=['small', 'medium', 'large', 'x-large']))
# a      small
# b      small
# c      small
# d      small
# e      small
# f      small
# g     medium
# h     medium
# i      large
# j    x-large
# k    x-large
# dtype: category
# Categories (4, object): [small < medium < large < x-large]

print(pd.cut(s, 3))
# a      (-0.1, 33.333]
# b      (-0.1, 33.333]
# c      (-0.1, 33.333]
# d      (-0.1, 33.333]
# e      (-0.1, 33.333]
# f      (-0.1, 33.333]
# g    (33.333, 66.667]
# h    (33.333, 66.667]
# i    (33.333, 66.667]
# j     (66.667, 100.0]
# k     (66.667, 100.0]
# dtype: category
# Categories (3, interval[float64]): [(-0.1, 33.333] < (33.333, 66.667] < (66.667, 100.0]]

print(pd.cut(s, 3, precision=1))
# a     (-0.1, 33.3]
# b     (-0.1, 33.3]
# c     (-0.1, 33.3]
# d     (-0.1, 33.3]
# e     (-0.1, 33.3]
# f     (-0.1, 33.3]
# g     (33.3, 66.7]
# h     (33.3, 66.7]
# i     (33.3, 66.7]
# j    (66.7, 100.0]
# k    (66.7, 100.0]
# dtype: category
# Categories (3, interval[float64]): [(-0.1, 33.3] < (33.3, 66.7] < (66.7, 100.0]]

print(pd.qcut(s, 2))
# a    (-0.001, 25.0]
# b    (-0.001, 25.0]
# c    (-0.001, 25.0]
# d    (-0.001, 25.0]
# e    (-0.001, 25.0]
# f    (-0.001, 25.0]
# g     (25.0, 100.0]
# h     (25.0, 100.0]
# i     (25.0, 100.0]
# j     (25.0, 100.0]
# k     (25.0, 100.0]
# dtype: category
# Categories (2, interval[float64]): [(-0.001, 25.0] < (25.0, 100.0]]

s_qcut, bins = pd.qcut(s, 4, labels=['Q1', 'Q2', 'Q3', 'Q4'], retbins=True)
print(s_qcut)
# a    Q1
# b    Q1
# c    Q1
# d    Q2
# e    Q2
# f    Q2
# g    Q3
# h    Q3
# i    Q4
# j    Q4
# k    Q4
# dtype: category
# Categories (4, object): [Q1 < Q2 < Q3 < Q4]

print(bins)
# [  0.    6.5  25.   56.5 100. ]

s_duplicate = pd.Series(data=[0, 0, 0, 0, 0, 1, 2, 3, 4, 5, 6],
                        index=list('abcdefghijk'))

print(s_duplicate)
# a    0
# b    0
# c    0
# d    0
# e    0
# f    1
# g    2
# h    3
# i    4
# j    5
# k    6
# dtype: int64

print(pd.qcut(s_duplicate, 2))
# a    (-0.001, 1.0]
# b    (-0.001, 1.0]
# c    (-0.001, 1.0]
# d    (-0.001, 1.0]
# e    (-0.001, 1.0]
# f    (-0.001, 1.0]
# g       (1.0, 6.0]
# h       (1.0, 6.0]
# i       (1.0, 6.0]
# j       (1.0, 6.0]
# k       (1.0, 6.0]
# dtype: category
# Categories (2, interval[float64]): [(-0.001, 1.0] < (1.0, 6.0]]

# print(pd.qcut(s_duplicate, 4))
# ValueError: Bin edges must be unique: array([0. , 0. , 1. , 3.5, 6. ]).
# You can drop duplicate edges by setting the 'duplicates' kwarg

print(pd.qcut(s_duplicate, 4, duplicates='drop'))
# a    (-0.001, 1.0]
# b    (-0.001, 1.0]
# c    (-0.001, 1.0]
# d    (-0.001, 1.0]
# e    (-0.001, 1.0]
# f    (-0.001, 1.0]
# g       (1.0, 3.5]
# h       (1.0, 3.5]
# i       (3.5, 6.0]
# j       (3.5, 6.0]
# k       (3.5, 6.0]
# dtype: category
# Categories (3, interval[float64]): [(-0.001, 1.0] < (1.0, 3.5] < (3.5, 6.0]]

counts = pd.cut(s, 3, labels=['S', 'M', 'L']).value_counts()
print(counts)
# S    6
# M    3
# L    2
# dtype: int64

print(type(counts))
# <class 'pandas.core.series.Series'>

print(counts['M'])
# 3

print(pd.value_counts(pd.cut(s, 3, labels=['S', 'M', 'L'])))
# S    6
# M    3
# L    2
# dtype: int64

l = [x**2 for x in range(11)]
print(l)
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

l_cut = pd.cut(l, 3, labels=['S', 'M', 'L'])
print(l_cut)
# [S, S, S, S, S, ..., M, M, M, L, L]
# Length: 11
# Categories (3, object): [S < M < L]

print(type(l_cut))
# <class 'pandas.core.categorical.Categorical'>

print(l_cut[0])
# S

print(list(l_cut))
# ['S', 'S', 'S', 'S', 'S', 'S', 'M', 'M', 'M', 'L', 'L']

print(pd.value_counts(l_cut))
# S    6
# M    3
# L    2
# dtype: int64

df_titanic = pd.read_csv('data/src/titanic_train.csv').drop(['Name', 'Ticket', 'Cabin', 'Embarked'], axis=1)

print(df_titanic.head())
#    PassengerId  Survived  Pclass     Sex   Age  SibSp  Parch     Fare
# 0            1         0       3    male  22.0      1      0   7.2500
# 1            2         1       1  female  38.0      1      0  71.2833
# 2            3         1       3  female  26.0      0      0   7.9250
# 3            4         1       1  female  35.0      1      0  53.1000
# 4            5         0       3    male  35.0      0      0   8.0500

print(df_titanic['Age'].describe())
# count    714.000000
# mean      29.699118
# std       14.526497
# min        0.420000
# 25%       20.125000
# 50%       28.000000
# 75%       38.000000
# max       80.000000
# Name: Age, dtype: float64

print(pd.cut(df_titanic['Age'], 5, precision=0).value_counts(sort=False, dropna=False))
# (0.0, 16.0]     100
# (16.0, 32.0]    346
# (32.0, 48.0]    188
# (48.0, 64.0]     69
# (64.0, 80.0]     11
# NaN             177
# Name: Age, dtype: int64

df_titanic['Age_bin'] = pd.cut(df_titanic['Age'], 5, labels=False)

print(df_titanic.head())
#    PassengerId  Survived  Pclass     Sex   Age  SibSp  Parch     Fare  Age_bin
# 0            1         0       3    male  22.0      1      0   7.2500      1.0
# 1            2         1       1  female  38.0      1      0  71.2833      2.0
# 2            3         1       3  female  26.0      0      0   7.9250      1.0
# 3            4         1       1  female  35.0      1      0  53.1000      2.0
# 4            5         0       3    male  35.0      0      0   8.0500      2.0
