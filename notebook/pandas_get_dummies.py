import pandas as pd

print(pd.__version__)
# 2.1.2

df = pd.read_csv('data/src/sample_pandas_normal.csv', index_col=0)

df['sex'] = ['female', float('nan'), 'male', 'male', 'female', 'male']
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
#          female   male
# name                  
# Alice      True  False
# Bob       False  False
# Charlie   False   True
# Dave      False   True
# Ellen      True  False
# Frank     False   True

print(pd.get_dummies(['female', float('nan'), 'male', 'male', 'female', 'male']))
#    female   male
# 0    True  False
# 1   False  False
# 2   False   True
# 3   False   True
# 4    True  False
# 5   False   True

print(pd.get_dummies(df))
#          age  point  rank  state_CA  state_NY  state_TX  sex_female  sex_male
# name                                                                         
# Alice     24     64     2     False      True     False        True     False
# Bob       42     92     1      True     False     False       False     False
# Charlie   18     70     1      True     False     False       False      True
# Dave      68     70     0     False     False      True       False      True
# Ellen     24     88     2      True     False     False        True     False
# Frank     30     57     0     False      True     False       False      True

print(pd.get_dummies(df, dtype=int))
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
# Alice     24     64     2      True     False     False
# Bob       42     92     1     False     False     False
# Charlie   18     70     1     False     False      True
# Dave      68     70     0     False      True      True
# Ellen     24     88     2     False     False     False
# Frank     30     57     0      True     False      True

print(pd.get_dummies(df, drop_first=True, dummy_na=True))
#          age  point  rank  state_NY  state_TX  state_nan  sex_male  sex_nan
# name                                                                       
# Alice     24     64     2      True     False      False     False    False
# Bob       42     92     1     False     False      False     False     True
# Charlie   18     70     1     False     False      False      True    False
# Dave      68     70     0     False      True      False      True    False
# Ellen     24     88     2     False     False      False     False    False
# Frank     30     57     0      True     False      False      True    False

print(pd.get_dummies(df, prefix='', prefix_sep=''))
#          age  point  rank     CA     NY     TX  female   male
# name                                                         
# Alice     24     64     2  False   True  False    True  False
# Bob       42     92     1   True  False  False   False  False
# Charlie   18     70     1   True  False  False   False   True
# Dave      68     70     0  False  False   True   False   True
# Ellen     24     88     2   True  False  False    True  False
# Frank     30     57     0  False   True  False   False   True

print(pd.get_dummies(df, prefix=['ST', 'sex'], prefix_sep='-'))
#          age  point  rank  ST-CA  ST-NY  ST-TX  sex-female  sex-male
# name                                                                
# Alice     24     64     2  False   True  False        True     False
# Bob       42     92     1   True  False  False       False     False
# Charlie   18     70     1   True  False  False       False      True
# Dave      68     70     0  False  False   True       False      True
# Ellen     24     88     2   True  False  False        True     False
# Frank     30     57     0  False   True  False       False      True

print(pd.get_dummies(df, prefix={'state': 'ST', 'sex': 'sex'}, prefix_sep='-'))
#          age  point  rank  ST-CA  ST-NY  ST-TX  sex-female  sex-male
# name                                                                
# Alice     24     64     2  False   True  False        True     False
# Bob       42     92     1   True  False  False       False     False
# Charlie   18     70     1   True  False  False       False      True
# Dave      68     70     0  False  False   True       False      True
# Ellen     24     88     2   True  False  False        True     False
# Frank     30     57     0  False   True  False       False      True

print(pd.get_dummies(df, columns=['sex', 'rank']))
#          age state  point  sex_female  sex_male  rank_0  rank_1  rank_2
# name                                                                   
# Alice     24    NY     64        True     False   False   False    True
# Bob       42    CA     92       False     False   False    True   False
# Charlie   18    CA     70       False      True   False    True   False
# Dave      68    TX     70       False      True    True   False   False
# Ellen     24    CA     88        True     False   False   False    True
# Frank     30    NY     57       False      True    True   False   False

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
# Alice     24     64     False      True
# Bob       42     92      True     False
# Charlie   18     70      True     False

print(pd.get_dummies(df_B))
#        age  point  state_CA  state_NY  state_TX
# name                                           
# Dave    68     70     False     False      True
# Ellen   24     88      True     False     False
# Frank   30     57     False      True     False

categories = set(df_A['state'].tolist() + df_B['state'].tolist())
print(categories)
# {'NY', 'TX', 'CA'}

df_A['state'] = pd.Categorical(df_A['state'], categories)
df_B['state'] = pd.Categorical(df_B['state'], categories)

print(df_A['state'].dtypes)
# category

print(pd.get_dummies(df_A))
#          age  point  state_NY  state_TX  state_CA
# name                                             
# Alice     24     64      True     False     False
# Bob       42     92     False     False      True
# Charlie   18     70     False     False      True

print(pd.get_dummies(df_B))
#        age  point  state_NY  state_TX  state_CA
# name                                           
# Dave    68     70     False      True     False
# Ellen   24     88     False     False      True
# Frank   30     57      True     False     False

categories = ['CA', 'NY']

df_A['state'] = pd.Categorical(df_A['state'], categories)
df_B['state'] = pd.Categorical(df_B['state'], categories)

print(df_A)
#          age state  point
# name                     
# Alice     24    NY     64
# Bob       42    CA     92
# Charlie   18    CA     70

print(df_B)
#        age state  point
# name                   
# Dave    68   NaN     70
# Ellen   24    CA     88
# Frank   30    NY     57

print(pd.get_dummies(df_A))
#          age  point  state_CA  state_NY
# name                                   
# Alice     24     64     False      True
# Bob       42     92      True     False
# Charlie   18     70      True     False

print(pd.get_dummies(df_B))
#        age  point  state_CA  state_NY
# name                                 
# Dave    68     70     False     False
# Ellen   24     88      True     False
# Frank   30     57     False      True
