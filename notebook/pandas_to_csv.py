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

df.to_csv('data/dst/to_csv_out.csv')

df.to_csv('data/dst/to_csv_out_columns.csv', columns=['age'])

df.to_csv('data/dst/to_csv_out_header_index.csv', header=False, index=False)

df.to_csv('data/dst/to_csv_out.tsv', sep='\t')

df.to_csv('data/dst/to_csv_out_a.csv')
df.to_csv('data/dst/to_csv_out_a.csv', mode='a', header=False)

df.to_csv('data/dst/to_csv_out_a_new_column.csv')

df = pd.read_csv('data/dst/to_csv_out_a_new_column.csv', index_col=0)

print(df)
#          age state  point
# name                     
# Alice     24    NY     64
# Bob       42    CA     92
# Charlie   18    CA     70
# Dave      68    TX     70
# Ellen     24    CA     88
# Frank     30    NY     57

df['new_col'] = 'new data'

print(df)
#          age state  point   new_col
# name                               
# Alice     24    NY     64  new data
# Bob       42    CA     92  new data
# Charlie   18    CA     70  new data
# Dave      68    TX     70  new data
# Ellen     24    CA     88  new data
# Frank     30    NY     57  new data

df.to_csv('data/dst/to_csv_out_a_new_column.csv')
