import pandas as pd

df = pd.read_csv('data/src/sample_pandas_normal.csv', index_col=0)
df['f_data'] = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6]
print(df)
#          age state  point  f_data
# name                             
# Alice     24    NY     64     0.1
# Bob       42    CA     92     0.2
# Charlie   18    CA     70     0.3
# Dave      68    TX     70     0.4
# Ellen     24    CA     88     0.5
# Frank     30    NY     57     0.6

print(df.dtypes)
# age         int64
# state      object
# point       int64
# f_data    float64
# dtype: object

print(type(df.dtypes))
print(type(df.dtypes[0]))
# <class 'pandas.core.series.Series'>
# <class 'numpy.dtype'>

print(df.dtypes == 'int64')
# age        True
# state     False
# point      True
# f_data    False
# dtype: bool

print(df.loc[:, df.dtypes == 'int64'])
#          age  point
# name               
# Alice     24     64
# Bob       42     92
# Charlie   18     70
# Dave      68     70
# Ellen     24     88
# Frank     30     57

print(df.dtypes != 'object')
# age        True
# state     False
# point      True
# f_data     True
# dtype: bool

print(df.loc[:, df.dtypes != 'object'])
#          age  point  f_data
# name                       
# Alice     24     64     0.1
# Bob       42     92     0.2
# Charlie   18     70     0.3
# Dave      68     70     0.4
# Ellen     24     88     0.5
# Frank     30     57     0.6

print(df.dtypes == 'int')
# age        True
# state     False
# point      True
# f_data    False
# dtype: bool

print(df.loc[:, df.dtypes == 'int'])
#          age  point
# name               
# Alice     24     64
# Bob       42     92
# Charlie   18     70
# Dave      68     70
# Ellen     24     88
# Frank     30     57

df = df.astype({'age': 'int8'})

print(df.dtypes)
# age          int8
# state      object
# point       int64
# f_data    float64
# dtype: object

print(df.dtypes == 'int')
# age       False
# state     False
# point      True
# f_data    False
# dtype: bool

print(df.dtypes.isin(['int8', 'int64']))
# age       False
# state     False
# point      True
# f_data    False
# dtype: bool

print((df.dtypes == 'int8') | (df.dtypes == 'int64'))
# age        True
# state     False
# point      True
# f_data    False
# dtype: bool

print(df.loc[:, (df.dtypes == 'int8') | (df.dtypes == 'int64')])
#          age  point
# name               
# Alice     24     64
# Bob       42     92
# Charlie   18     70
# Dave      68     70
# Ellen     24     88
# Frank     30     57

print(df.dtypes.astype('str').str.contains('int'))
# age        True
# state     False
# point      True
# f_data    False
# dtype: bool

print(df.loc[:, df.dtypes.astype('str').str.contains('int')])
#          age  point
# name               
# Alice     24     64
# Bob       42     92
# Charlie   18     70
# Dave      68     70
# Ellen     24     88
# Frank     30     57

print(df.loc[:, df.dtypes != 'object'])
#          age  point  f_data
# name                       
# Alice     24     64     0.1
# Bob       42     92     0.2
# Charlie   18     70     0.3
# Dave      68     70     0.4
# Ellen     24     88     0.5
# Frank     30     57     0.6
