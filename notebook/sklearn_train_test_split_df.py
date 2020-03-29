import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris

data = load_iris()

X_df = pd.DataFrame(data['data'], columns=data['feature_names'])
y_s = pd.Series(data['target'])

print(X_df)
#      sepal length (cm)  sepal width (cm)  petal length (cm)  petal width (cm)
# 0                  5.1               3.5                1.4               0.2
# 1                  4.9               3.0                1.4               0.2
# 2                  4.7               3.2                1.3               0.2
# 3                  4.6               3.1                1.5               0.2
# 4                  5.0               3.6                1.4               0.2
# ..                 ...               ...                ...               ...
# 145                6.7               3.0                5.2               2.3
# 146                6.3               2.5                5.0               1.9
# 147                6.5               3.0                5.2               2.0
# 148                6.2               3.4                5.4               2.3
# 149                5.9               3.0                5.1               1.8
# 
# [150 rows x 4 columns]

print(type(X_df))
# <class 'pandas.core.frame.DataFrame'>

print(X_df.shape)
# (150, 4)

print(y_s)
# 0      0
# 1      0
# 2      0
# 3      0
# 4      0
#       ..
# 145    2
# 146    2
# 147    2
# 148    2
# 149    2
# Length: 150, dtype: int64

print(type(y_s))
# <class 'pandas.core.series.Series'>

print(y_s.shape)
# (150,)

X_train_df, X_test_df, y_train_s, y_test_s = train_test_split(
    X_df, y_s, test_size=0.2, random_state=0, stratify=y_s
)

print(type(X_train_df))
# <class 'pandas.core.frame.DataFrame'>

print(X_train_df.shape)
# (120, 4)

print(type(X_test_df))
# <class 'pandas.core.frame.DataFrame'>

print(X_test_df.shape)
# (30, 4)

print(type(y_train_s))
# <class 'pandas.core.series.Series'>

print(y_train_s.shape)
# (120,)

print(type(y_test_s))
# <class 'pandas.core.series.Series'>

print(y_test_s.shape)
# (30,)

print(y_train_s.value_counts())
# 2    40
# 1    40
# 0    40
# dtype: int64

print(y_test_s.value_counts())
# 2    10
# 1    10
# 0    10
# dtype: int64
