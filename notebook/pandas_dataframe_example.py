import pandas as pd

df = pd.read_csv('data/src/sample_pandas_normal.csv', index_col=0)
df['sex'] = ['Female', 'Male', 'Male', 'Male', 'Female', 'Male']
print(df)
#          age state  point     sex
# name                             
# Alice     24    NY     64  Female
# Bob       42    CA     92    Male
# Charlie   18    CA     70    Male
# Dave      68    TX     70    Male
# Ellen     24    CA     88  Female
# Frank     30    NY     57    Male

print(df.mean(numeric_only=True))
# age      34.333333
# point    73.500000
# dtype: float64

print(df.pivot_table(index='state', columns='sex', aggfunc='mean'))
#          age        point      
# sex   Female  Male Female  Male
# state                          
# CA      24.0  30.0   88.0  81.0
# NY      24.0  30.0   64.0  57.0
# TX       NaN  68.0    NaN  70.0
