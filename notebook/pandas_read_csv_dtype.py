import pandas as pd

df = pd.read_csv('data/src/sample_pandas_normal.csv', index_col=0)
print(df)
#          age state  point
# name                     
# Alice     24    NY     64
# Bob       42    CA     92
# Charlie   18    CA     70
# Dave      68    TX     70
# Ellen     24    CA     88
# Frank     30    NY     57

print(df.dtypes)
# age       int64
# state    object
# point     int64
# dtype: object

df_str = pd.read_csv('data/src/sample_pandas_normal.csv', index_col=0, dtype=str)
print(df_str.dtypes)
print(type(df_str['age'][0]))
print(type(df_str['state'][0]))
print(type(df_str['point'][0]))
# age      object
# state    object
# point    object
# dtype: object
# <class 'str'>
# <class 'str'>
# <class 'str'>

df_object = pd.read_csv('data/src/sample_pandas_normal.csv', index_col=0, dtype=object)
print(df_object.dtypes)
print(type(df_object['age'][0]))
print(type(df_object['state'][0]))
print(type(df_object['point'][0]))
# age      object
# state    object
# point    object
# dtype: object
# <class 'str'>
# <class 'str'>
# <class 'str'>

df_col = pd.read_csv('data/src/sample_pandas_normal.csv', index_col=0, dtype={'age': float, 'point': 'float32'})
print(df_col.dtypes)
# age      float64
# state     object
# point    float32
# dtype: object

df_col = pd.read_csv('data/src/sample_pandas_normal.csv', index_col=0, dtype={1: float, 3: 'float32'})
print(df_col.dtypes)
# age      float64
# state     object
# point    float32
# dtype: object
