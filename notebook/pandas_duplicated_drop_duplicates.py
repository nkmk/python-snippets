import pandas as pd

print(pd.__version__)
# 2.1.4

df = pd.read_csv('data/src/sample_pandas_normal.csv')
df.loc[6] = ['Dave', 68, 'TX', 70]
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

print(df.duplicated().sum())
# 1

print(~df.duplicated())
# 0     True
# 1     True
# 2     True
# 3     True
# 4     True
# 5     True
# 6    False
# dtype: bool

print((~df.duplicated()).sum())
# 6

print(df.duplicated().value_counts())
# False    6
# True     1
# Name: count, dtype: int64

print(df.duplicated(keep=False).value_counts())
# False    5
# True     2
# Name: count, dtype: int64

print(df.drop_duplicates())
#       name  age state  point
# 0    Alice   24    NY     64
# 1      Bob   42    CA     92
# 2  Charlie   18    CA     70
# 3     Dave   68    TX     70
# 4    Ellen   24    CA     88
# 5    Frank   30    NY     57

print(df.drop_duplicates(keep='last'))
#       name  age state  point
# 0    Alice   24    NY     64
# 1      Bob   42    CA     92
# 2  Charlie   18    CA     70
# 4    Ellen   24    CA     88
# 5    Frank   30    NY     57
# 6     Dave   68    TX     70

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

print(df.drop_duplicates(subset=['state', 'point']))
#       name  age state  point
# 0    Alice   24    NY     64
# 1      Bob   42    CA     92
# 2  Charlie   18    CA     70
# 3     Dave   68    TX     70
# 4    Ellen   24    CA     88
# 5    Frank   30    NY     57

print(df.drop_duplicates(subset='state', keep='last'))
#     name  age state  point
# 4  Ellen   24    CA     88
# 5  Frank   30    NY     57
# 6   Dave   68    TX     70

print(df.drop_duplicates(subset='state', keep='last', ignore_index=True))
#     name  age state  point
# 0  Ellen   24    CA     88
# 1  Frank   30    NY     57
# 2   Dave   68    TX     70

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

print(df.groupby('state').mean(numeric_only=True))
#         age      point
# state                 
# CA     28.0  83.333333
# NY     27.0  60.500000
# TX     68.0  70.000000

print(
    df.groupby('state').agg(
        {'name': lambda x: ','.join(x), 'age': 'mean', 'point': 'sum'}
    )
)
#                     name   age  point
# state                                
# CA     Bob,Charlie,Ellen  28.0    250
# NY           Alice,Frank  27.0    121
# TX                  Dave  68.0     70

print(df.groupby('state').agg({'name': list, 'age': 'mean', 'point': 'sum'}))
#                         name   age  point
# state                                    
# CA     [Bob, Charlie, Ellen]  28.0    250
# NY            [Alice, Frank]  27.0    121
# TX                    [Dave]  68.0     70
