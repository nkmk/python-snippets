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

print(df.query('index.str.contains("li")', engine='python'))
#          age state  point
# name                     
# Alice     24    NY     64
# Charlie   18    CA     70

print(df.query('name.str.endswith("e")', engine='python'))
#          age state  point
# name                     
# Alice     24    NY     64
# Charlie   18    CA     70
# Dave      68    TX     70
