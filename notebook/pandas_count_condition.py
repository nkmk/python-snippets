import pandas as pd

df = pd.read_csv('data/src/sample_pandas_normal.csv')

print(df)
#       name  age state  point
# 0    Alice   24    NY     64
# 1      Bob   42    CA     92
# 2  Charlie   18    CA     70
# 3     Dave   68    TX     70
# 4    Ellen   24    CA     88
# 5    Frank   30    NY     57

df_bool = (df == 'CA')
print(df_bool)
#     name    age  state  point
# 0  False  False  False  False
# 1  False  False   True  False
# 2  False  False   True  False
# 3  False  False  False  False
# 4  False  False   True  False
# 5  False  False  False  False

print(df_bool.sum())
# name     0
# age      0
# state    3
# point    0
# dtype: int64

print(df_bool.sum(axis=1))
# 0    0
# 1    1
# 2    1
# 3    0
# 4    1
# 5    0
# dtype: int64

print(df_bool.values)
# [[False False False False]
#  [False False  True False]
#  [False False  True False]
#  [False False False False]
#  [False False  True False]
#  [False False False False]]

print(type(df_bool.values))
# <class 'numpy.ndarray'>

print(df_bool.values.sum())
# 3

s_bool = df['age'] < 25
print(s_bool)
# 0     True
# 1    False
# 2     True
# 3    False
# 4     True
# 5    False
# Name: age, dtype: bool

print(s_bool.sum())
# 3

df_bool_multi = ((df == 'CA') | (df == 70))
print(df_bool_multi)
#     name    age  state  point
# 0  False  False  False  False
# 1  False  False   True  False
# 2  False  False   True   True
# 3  False  False  False   True
# 4  False  False   True  False
# 5  False  False  False  False

print(df_bool_multi.sum())
# name     0
# age      0
# state    3
# point    2
# dtype: int64

print(df_bool_multi.sum(axis=1))
# 0    0
# 1    1
# 2    2
# 3    1
# 4    1
# 5    0
# dtype: int64

print(df_bool_multi.values.sum())
# 5

df_bool_multi_and = ((df['state'] == 'CA') & (df['age'] < 30))
print(df_bool_multi_and)
# 0    False
# 1    False
# 2     True
# 3    False
# 4     True
# 5    False
# dtype: bool

print(df_bool_multi_and.sum())
# 2

df_bool_multi_or = ((df['state'] == 'CA') | (df['age'] < 30))
print(df_bool_multi_or)
# 0     True
# 1     True
# 2     True
# 3    False
# 4     True
# 5    False
# dtype: bool

print(df_bool_multi_or.sum())
# 4

df_bool_not = ~(df == 'CA')
print(df_bool_not)
#    name   age  state  point
# 0  True  True   True   True
# 1  True  True  False   True
# 2  True  True  False   True
# 3  True  True   True   True
# 4  True  True  False   True
# 5  True  True   True   True

print(df_bool_not.sum())
# name     6
# age      6
# state    3
# point    6
# dtype: int64

print(df_bool_not.sum(axis=1))
# 0    4
# 1    3
# 2    3
# 3    4
# 4    3
# 5    4
# dtype: int64

print(df_bool_not.values.sum())
# 21

df_num = df[['age', 'point']]
print(df_num)
#    age  point
# 0   24     64
# 1   42     92
# 2   18     70
# 3   68     70
# 4   24     88
# 5   30     57

print((df_num <= 70).sum())
# age      6
# point    4
# dtype: int64

print(((df['age'] > 20) & (df['age'] < 40)).sum())
# 3

print((df_num % 2 == 1).sum())
# age      0
# point    1
# dtype: int64

df_str = df[['name', 'state']]
print(df_str)
#       name state
# 0    Alice    NY
# 1      Bob    CA
# 2  Charlie    CA
# 3     Dave    TX
# 4    Ellen    CA
# 5    Frank    NY

print((df_str == 'NY').sum())
# name     0
# state    2
# dtype: int64

print(df_str['name'].str.endswith('e'))
# 0     True
# 1    False
# 2     True
# 3     True
# 4    False
# 5    False
# Name: name, dtype: bool

print(df_str['name'].str.endswith('e').sum())
# 3

df = pd.read_csv('data/src/titanic_train.csv')

print(df.head())
#    PassengerId  Survived  Pclass  \
# 0            1         0       3   
# 1            2         1       1   
# 2            3         1       3   
# 3            4         1       1   
# 4            5         0       3   
#                                                 Name     Sex   Age  SibSp  \
# 0                            Braund, Mr. Owen Harris    male  22.0      1   
# 1  Cumings, Mrs. John Bradley (Florence Briggs Th...  female  38.0      1   
# 2                             Heikkinen, Miss. Laina  female  26.0      0   
# 3       Futrelle, Mrs. Jacques Heath (Lily May Peel)  female  35.0      1   
# 4                           Allen, Mr. William Henry    male  35.0      0   
#    Parch            Ticket     Fare Cabin Embarked  
# 0      0         A/5 21171   7.2500   NaN        S  
# 1      0          PC 17599  71.2833   C85        C  
# 2      0  STON/O2. 3101282   7.9250   NaN        S  
# 3      0            113803  53.1000  C123        S  
# 4      0            373450   8.0500   NaN        S  

df.info()
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 891 entries, 0 to 890
# Data columns (total 12 columns):
# PassengerId    891 non-null int64
# Survived       891 non-null int64
# Pclass         891 non-null int64
# Name           891 non-null object
# Sex            891 non-null object
# Age            714 non-null float64
# SibSp          891 non-null int64
# Parch          891 non-null int64
# Ticket         891 non-null object
# Fare           891 non-null float64
# Cabin          204 non-null object
# Embarked       889 non-null object
# dtypes: float64(2), int64(5), object(5)
# memory usage: 83.6+ KB

print(df.isnull().head())
#    PassengerId  Survived  Pclass   Name    Sex    Age  SibSp  Parch  Ticket  \
# 0        False     False   False  False  False  False  False  False   False   
# 1        False     False   False  False  False  False  False  False   False   
# 2        False     False   False  False  False  False  False  False   False   
# 3        False     False   False  False  False  False  False  False   False   
# 4        False     False   False  False  False  False  False  False   False   
#     Fare  Cabin  Embarked  
# 0  False   True     False  
# 1  False  False     False  
# 2  False   True     False  
# 3  False  False     False  
# 4  False   True     False  

print(df.isnull().sum())
# PassengerId      0
# Survived         0
# Pclass           0
# Name             0
# Sex              0
# Age            177
# SibSp            0
# Parch            0
# Ticket           0
# Fare             0
# Cabin          687
# Embarked         2
# dtype: int64

print(df.isnull().sum(axis=1).head())
# 0    1
# 1    0
# 2    1
# 3    0
# 4    1
# dtype: int64

print(df.isnull().values.sum())
# 866

print(df.count())
# PassengerId    891
# Survived       891
# Pclass         891
# Name           891
# Sex            891
# Age            714
# SibSp          891
# Parch          891
# Ticket         891
# Fare           891
# Cabin          204
# Embarked       889
# dtype: int64

print(df.count(axis=1).head())
# 0    11
# 1    12
# 2    11
# 3    12
# 4    11
# dtype: int64

print(df.count().sum())
# 9826
