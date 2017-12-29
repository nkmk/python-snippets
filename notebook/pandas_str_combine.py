import pandas as pd

df = pd.read_csv('data/src/sample_pandas_normal.csv').head(3)
print(df)
#       name  age state  point
# 0    Alice   24    NY     64
# 1      Bob   42    CA     92
# 2  Charlie   18    CA     70

df['name-state'] = df['name'].str.cat(df['state'], sep=' in ')
print(df)
#       name  age state  point     name-state
# 0    Alice   24    NY     64    Alice in NY
# 1      Bob   42    CA     92      Bob in CA
# 2  Charlie   18    CA     70  Charlie in CA

df['name-state2'] = df['name'] + ' in ' + df['state']
print(df)
#       name  age state  point     name-state    name-state2
# 0    Alice   24    NY     64    Alice in NY    Alice in NY
# 1      Bob   42    CA     92      Bob in CA      Bob in CA
# 2  Charlie   18    CA     70  Charlie in CA  Charlie in CA

df.drop(['name-state2', 'state'], axis=1, inplace=True)
print(df)
#       name  age  point     name-state
# 0    Alice   24     64    Alice in NY
# 1      Bob   42     92      Bob in CA
# 2  Charlie   18     70  Charlie in CA

df['name-age'] = df['name'] + '(' + df['age'].astype(str) + ')'
print(df)
#       name  age  point     name-state     name-age
# 0    Alice   24     64    Alice in NY    Alice(24)
# 1      Bob   42     92      Bob in CA      Bob(42)
# 2  Charlie   18     70  Charlie in CA  Charlie(18)
