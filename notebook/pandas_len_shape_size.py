import pandas as pd

df = pd.read_csv('data/src/titanic_train.csv')

print(df.head())
#    PassengerId  Survived  Pclass  \
# 0            1         0       3   
# 1            2         1       1   
# 2            3         1       3   
# 3            4         1       1   
# 4            5         0       3   
# 
#                                                 Name     Sex   Age  SibSp  \
# 0                            Braund, Mr. Owen Harris    male  22.0      1   
# 1  Cumings, Mrs. John Bradley (Florence Briggs Th...  female  38.0      1   
# 2                             Heikkinen, Miss. Laina  female  26.0      0   
# 3       Futrelle, Mrs. Jacques Heath (Lily May Peel)  female  35.0      1   
# 4                           Allen, Mr. William Henry    male  35.0      0   
# 
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

print(len(df))
# 891

print(len(df.columns))
# 12

print(df.shape)
# (891, 12)

print(df.shape[0])
# 891

print(df.shape[1])
# 12

row, col = df.shape
print(row)
# 891

print(col)
# 12

print(df.size)
# 10692

print(df.shape[0] * df.shape[1])
# 10692

s = df['PassengerId']
print(s.head())
# 0    1
# 1    2
# 2    3
# 3    4
# 4    5
# Name: PassengerId, dtype: int64

print(len(s))
# 891

print(s.size)
# 891

print(s.shape)
# (891,)

df_multiindex = df.set_index(['Sex', 'Pclass', 'Embarked', 'PassengerId'])

print(len(df_multiindex))
# 891

print(len(df_multiindex.columns))
# 8

print(df_multiindex.shape)
# (891, 8)

print(df_multiindex.size)
# 7128
