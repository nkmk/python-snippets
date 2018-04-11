import pandas as pd
import numpy as np

df = pd.read_csv('data/src/sample_pandas_normal.csv', index_col=0)

df['sex'] = ['female', np.nan, 'male', 'male', 'female', 'male']
df['rank'] = [2, 1, 1, 0, 2, 0]

print(df)
#          age state  point     sex  rank
# name                                   
# Alice     24    NY     64  female     2
# Bob       42    CA     92     NaN     1
# Charlie   18    CA     70    male     1
# Dave      68    TX     70    male     0
# Ellen     24    CA     88  female     2
# Frank     30    NY     57    male     0

print(pd.get_dummies(df['sex']))
#          female  male
# name                 
# Alice         1     0
# Bob           0     0
# Charlie       0     1
# Dave          0     1
# Ellen         1     0
# Frank         0     1

print(pd.get_dummies(['male', 1, 1, 2]))
#    1  2  male
# 0  0  0     1
# 1  1  0     0
# 2  1  0     0
# 3  0  1     0

print(pd.get_dummies(np.arange(6)))
#    0  1  2  3  4  5
# 0  1  0  0  0  0  0
# 1  0  1  0  0  0  0
# 2  0  0  1  0  0  0
# 3  0  0  0  1  0  0
# 4  0  0  0  0  1  0
# 5  0  0  0  0  0  1

# print(pd.get_dummies(np.arange(6).reshape((2, 3))))
# Exception: Data must be 1-dimensional

print(pd.get_dummies(df))
#          age  point  rank  state_CA  state_NY  state_TX  sex_female  sex_male
# name                                                                         
# Alice     24     64     2         0         1         0           1         0
# Bob       42     92     1         1         0         0           0         0
# Charlie   18     70     1         1         0         0           0         1
# Dave      68     70     0         0         0         1           0         1
# Ellen     24     88     2         1         0         0           1         0
# Frank     30     57     0         0         1         0           0         1

print(pd.get_dummies(df, drop_first=True))
#          age  point  rank  state_NY  state_TX  sex_male
# name                                                   
# Alice     24     64     2         1         0         0
# Bob       42     92     1         0         0         0
# Charlie   18     70     1         0         0         1
# Dave      68     70     0         0         1         1
# Ellen     24     88     2         0         0         0
# Frank     30     57     0         1         0         1

print(pd.get_dummies(df, drop_first=True, dummy_na=True))
#          age  point  rank  state_NY  state_TX  state_nan  sex_male  sex_nan
# name                                                                       
# Alice     24     64     2         1         0          0         0        0
# Bob       42     92     1         0         0          0         0        1
# Charlie   18     70     1         0         0          0         1        0
# Dave      68     70     0         0         1          0         1        0
# Ellen     24     88     2         0         0          0         0        0
# Frank     30     57     0         1         0          0         1        0

print(pd.get_dummies(df, drop_first=True, prefix='', prefix_sep=''))
#          age  point  rank  NY  TX  male
# name                                   
# Alice     24     64     2   1   0     0
# Bob       42     92     1   0   0     0
# Charlie   18     70     1   0   0     1
# Dave      68     70     0   0   1     1
# Ellen     24     88     2   0   0     0
# Frank     30     57     0   1   0     1

print(pd.get_dummies(df, drop_first=True, prefix=['ST', 'sex'], prefix_sep='-'))
#          age  point  rank  ST-NY  ST-TX  sex-male
# name                                             
# Alice     24     64     2      1      0         0
# Bob       42     92     1      0      0         0
# Charlie   18     70     1      0      0         1
# Dave      68     70     0      0      1         1
# Ellen     24     88     2      0      0         0
# Frank     30     57     0      1      0         1

print(pd.get_dummies(df, drop_first=True, prefix={'state': 'ST', 'sex': 'sex'}, prefix_sep='-'))
#          age  point  rank  ST-NY  ST-TX  sex-male
# name                                             
# Alice     24     64     2      1      0         0
# Bob       42     92     1      0      0         0
# Charlie   18     70     1      0      0         1
# Dave      68     70     0      0      1         1
# Ellen     24     88     2      0      0         0
# Frank     30     57     0      1      0         1

print(pd.get_dummies(df, drop_first=True, columns=['sex', 'rank']))
#          age state  point  sex_male  rank_1  rank_2
# name                                               
# Alice     24    NY     64         0       0       1
# Bob       42    CA     92         0       1       0
# Charlie   18    CA     70         1       1       0
# Dave      68    TX     70         1       0       0
# Ellen     24    CA     88         0       0       1
# Frank     30    NY     57         1       0       0

df['rank'] = df['rank'].astype(object)
print(pd.get_dummies(df, drop_first=True))
#          age  point  state_NY  state_TX  sex_male  rank_1  rank_2
# name                                                             
# Alice     24     64         1         0         0       0       1
# Bob       42     92         0         0         0       1       0
# Charlie   18     70         0         0         1       1       0
# Dave      68     70         0         1         1       0       0
# Ellen     24     88         0         0         0       0       1
# Frank     30     57         1         0         1       0       0

print(df['state'].map({'CA': 0, 'NY': 1, 'TX': 2}))
# name
# Alice      1
# Bob        0
# Charlie    0
# Dave       2
# Ellen      0
# Frank      1
# Name: state, dtype: int64

df['state'] = df['state'].map({'CA': 0, 'NY': 1, 'TX': 2})
print(df)
#          age  state  point     sex rank
# name                                   
# Alice     24      1     64  female    2
# Bob       42      0     92     NaN    1
# Charlie   18      0     70    male    1
# Dave      68      2     70    male    0
# Ellen     24      0     88  female    2
# Frank     30      1     57    male    0
