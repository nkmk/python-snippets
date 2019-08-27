import pandas as pd

df = pd.read_csv('data/src/sample_pandas_normal.csv', index_col=0)
df_A, df_B = df[:3].copy(), df[3:].copy()

print(df_A)
#          age state  point
# name                     
# Alice     24    NY     64
# Bob       42    CA     92
# Charlie   18    CA     70

print(df_B)
#        age state  point
# name                   
# Dave    68    TX     70
# Ellen   24    CA     88
# Frank   30    NY     57

print(pd.get_dummies(df_A))
#          age  point  state_CA  state_NY
# name                                   
# Alice     24     64         0         1
# Bob       42     92         1         0
# Charlie   18     70         1         0

print(pd.get_dummies(df_B))
#        age  point  state_CA  state_NY  state_TX
# name                                           
# Dave    68     70         0         0         1
# Ellen   24     88         1         0         0
# Frank   30     57         0         1         0

categories = set(df_A['state'].unique().tolist() + df_B['state'].unique().tolist())
print(categories)
# {'NY', 'TX', 'CA'}

df_A['state'] = pd.Categorical(df_A['state'], categories=categories)
df_B['state'] = pd.Categorical(df_B['state'], categories=categories)

print(df_A['state'].dtypes)
# category

print(pd.get_dummies(df_A))
#          age  point  state_NY  state_TX  state_CA
# name                                             
# Alice     24     64         1         0         0
# Bob       42     92         0         0         1
# Charlie   18     70         0         0         1

print(pd.get_dummies(df_B))
#        age  point  state_NY  state_TX  state_CA
# name                                           
# Dave    68     70         0         1         0
# Ellen   24     88         0         0         1
# Frank   30     57         1         0         0

df = pd.read_csv('data/src/sample_pandas_normal.csv', index_col=0)
df_train, df_test = df[:3].copy(), df[3:].copy()

categories = df_train['state'].unique()

df_train['state'] = pd.Categorical(df_train['state'], categories=categories)
df_test['state'] = pd.Categorical(df_test['state'], categories=categories)

print(df_test)
#        age state  point
# name                   
# Dave    68   NaN     70
# Ellen   24    CA     88
# Frank   30    NY     57

print(pd.get_dummies(df_train))
#          age  point  state_NY  state_CA
# name                                   
# Alice     24     64         1         0
# Bob       42     92         0         1
# Charlie   18     70         0         1

print(pd.get_dummies(df_test))
#        age  point  state_NY  state_CA
# name                                 
# Dave    68     70         0         0
# Ellen   24     88         0         1
# Frank   30     57         1         0

df = pd.read_csv('data/src/sample_pandas_normal.csv', index_col=0)
df_train, df_test = df[:3].copy(), df[3:].copy()

cols = df_train.select_dtypes('object').columns

for col in cols:
    categories = df_train[col].unique()
    df_train[col] = pd.Categorical(df_train[col], categories=categories)
    df_test[col] = pd.Categorical(df_test[col], categories=categories)

df_train = pd.get_dummies(df_train)
df_test = pd.get_dummies(df_test)

print(df_train)
#          age  point  state_NY  state_CA
# name                                   
# Alice     24     64         1         0
# Bob       42     92         0         1
# Charlie   18     70         0         1

print(df_test)
#        age  point  state_NY  state_CA
# name                                 
# Dave    68     70         0         0
# Ellen   24     88         0         1
# Frank   30     57         1         0
