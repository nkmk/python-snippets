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

df = df.append({'name': 'Dave', 'age': 68, 'state': 'TX', 'point': 70}, ignore_index=True)
print(df)
#       name  age state  point
# 0    Alice   24    NY     64
# 1      Bob   42    CA     92
# 2  Charlie   18    CA     70
# 3     Dave   68    TX     70
# 4    Ellen   24    CA     88
# 5    Frank   30    NY     57
# 6     Dave   68    TX     70

print(df.duplicated())
# 0    False
# 1    False
# 2    False
# 3    False
# 4    False
# 5    False
# 6     True
# dtype: bool

print(df[df.duplicated()])
#    name  age state  point
# 6  Dave   68    TX     70

print(df.duplicated(keep='last'))
# 0    False
# 1    False
# 2    False
# 3     True
# 4    False
# 5    False
# 6    False
# dtype: bool

print(df.duplicated(keep=False))
# 0    False
# 1    False
# 2    False
# 3     True
# 4    False
# 5    False
# 6     True
# dtype: bool

print(df.duplicated(subset='state'))
# 0    False
# 1    False
# 2     True
# 3    False
# 4     True
# 5     True
# 6     True
# dtype: bool

print(df.duplicated(subset=['state', 'point']))
# 0    False
# 1    False
# 2    False
# 3    False
# 4    False
# 5    False
# 6     True
# dtype: bool

print(df.duplicated().value_counts())
# False    6
# True     1
# dtype: int64

print(df.duplicated().value_counts()[True])
# 1

print(df.duplicated(keep=False).value_counts()[True])
# 2

print(df[~df.duplicated()])
#       name  age state  point
# 0    Alice   24    NY     64
# 1      Bob   42    CA     92
# 2  Charlie   18    CA     70
# 3     Dave   68    TX     70
# 4    Ellen   24    CA     88
# 5    Frank   30    NY     57

print(df.drop_duplicates())
#       name  age state  point
# 0    Alice   24    NY     64
# 1      Bob   42    CA     92
# 2  Charlie   18    CA     70
# 3     Dave   68    TX     70
# 4    Ellen   24    CA     88
# 5    Frank   30    NY     57

print(df.drop_duplicates(keep=False))
#       name  age state  point
# 0    Alice   24    NY     64
# 1      Bob   42    CA     92
# 2  Charlie   18    CA     70
# 4    Ellen   24    CA     88
# 5    Frank   30    NY     57

print(df.drop_duplicates(subset='state'))
#     name  age state  point
# 0  Alice   24    NY     64
# 1    Bob   42    CA     92
# 3   Dave   68    TX     70

df.drop_duplicates(subset='state', keep='last', inplace=True)
print(df)
#     name  age state  point
# 4  Ellen   24    CA     88
# 5  Frank   30    NY     57
# 6   Dave   68    TX     70

df = pd.read_csv('data/src/sample_pandas_normal.csv')
print(df)
#       name  age state  point
# 0    Alice   24    NY     64
# 1      Bob   42    CA     92
# 2  Charlie   18    CA     70
# 3     Dave   68    TX     70
# 4    Ellen   24    CA     88
# 5    Frank   30    NY     57

print(df.groupby('state').mean())
#         age      point
# state                 
# CA     28.0  83.333333
# NY     27.0  60.500000
# TX     68.0  70.000000

print(df.groupby('state').agg(
    {'name': lambda x: ','.join(x),
     'age': 'mean',
     'point': 'mean'}))
#                     name  age      point
# state                                   
# CA     Bob,Charlie,Ellen   28  83.333333
# NY           Alice,Frank   27  60.500000
# TX                  Dave   68  70.000000

print(df.groupby('state').agg(
    {'name': list,
     'age': 'mean',
     'point': 'mean'}))
#                         name  age      point
# state                                       
# CA     [Bob, Charlie, Ellen]   28  83.333333
# NY            [Alice, Frank]   27  60.500000
# TX                    [Dave]   68  70.000000
