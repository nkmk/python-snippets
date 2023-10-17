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

df = df.assign(point_ratio=df['point'] / 100)
df = df.drop(columns='state')
df = df.sort_values('age')
df = df.head(3)

print(df)
#          age  point  point_ratio
# name                            
# Charlie   18     70         0.70
# Alice     24     64         0.64
# Ellen     24     88         0.88

df_mc = pd.read_csv('data/src/sample_pandas_normal.csv', index_col=0).assign(point_ratio=df['point'] / 100).drop(columns='state').sort_values('age').head(3)

print(df_mc)
#          age  point  point_ratio
# name                            
# Charlie   18     70         0.70
# Alice     24     64         0.64
# Ellen     24     88         0.88

df_mc_break = pd.read_csv(
    'data/src/sample_pandas_normal.csv',
    index_col=0
).assign(
    point_ratio=df['point'] / 100
).drop(
    columns='state'
).sort_values(
    'age'
).head(
    3
)

print(df_mc_break)
#          age  point  point_ratio
# name                            
# Charlie   18     70         0.70
# Alice     24     64         0.64
# Ellen     24     88         0.88

# df_mc_break = pd.read_csv(
#     'data/src/sample_
#     pandas_normal.csv',
#     index_col=0
# ).assign(
#     point_ratio=df['point'] / 100
# ).drop(
#     columns='state'
# ).sort_values(
#     'age'
# ).head(
#     3
# )
# SyntaxError: unterminated string literal (detected at line 2)

df_mc_break = pd.read_csv(
    'data/src/sample_pandas_normal.csv', index_col=0
).assign(
    point_ratio=df['point'] / 100
).drop(columns='state').sort_values('age').head(3)

print(df_mc_break)
#          age  point  point_ratio
# name                            
# Charlie   18     70         0.70
# Alice     24     64         0.64
# Ellen     24     88         0.88

df_mc_backslash = pd.read_csv('data/src/sample_pandas_normal.csv', index_col=0) \
                    .assign(point_ratio=df['point'] / 100) \
                    .drop(columns='state') \
                    .sort_values('age') \
                    .head(3)

print(df_mc_backslash)
#          age  point  point_ratio
# name                            
# Charlie   18     70         0.70
# Alice     24     64         0.64
# Ellen     24     88         0.88

df_mc_parens = (
    pd.read_csv('data/src/sample_pandas_normal.csv', index_col=0)
    .assign(point_ratio=df['point'] / 100)
    .drop(columns='state')
    .sort_values('age')
    .head(3)
)

print(df_mc_parens)
#          age  point  point_ratio
# name                            
# Charlie   18     70         0.70
# Alice     24     64         0.64
# Ellen     24     88         0.88

df_mc_parens = (pd.read_csv('data/src/sample_pandas_normal.csv', index_col=0)
                .assign(point_ratio=df['point'] / 100)
                .drop(columns='state')
                .sort_values('age')
                .head(3))

print(df_mc_parens)
#          age  point  point_ratio
# name                            
# Charlie   18     70         0.70
# Alice     24     64         0.64
# Ellen     24     88         0.88

df_mc_parens = (
    pd.read_csv('data/src/sample_pandas_normal.csv', index_col=0).
    assign(point_ratio=df['point'] / 100).
    drop(columns='state').
    sort_values('age').
    head(3)
)

print(df_mc_parens)
#          age  point  point_ratio
# name                            
# Charlie   18     70         0.70
# Alice     24     64         0.64
# Ellen     24     88         0.88
