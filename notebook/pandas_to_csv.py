import pandas as pd

print(pd.__version__)
# 2.0.3

df = pd.read_csv('data/src/sample_pandas_normal.csv', index_col=0).head(3)
print(df)
#          age state  point
# name                     
# Alice     24    NY     64
# Bob       42    CA     92
# Charlie   18    CA     70

df.to_csv('data/dst/to_csv_out.csv')

df.to_csv('data/dst/to_csv_out_columns.csv', columns=['age', 'point'])

df.to_csv('data/dst/to_csv_out_header_index.csv', header=False, index=False)

df.to_csv('data/dst/to_csv_out.tsv', sep='\t')

# df.to_csv('data/dst/to_csv_out.csv', mode='x')
# FileExistsError: [Errno 17] File exists: 'data/dst/to_csv_out.csv'

df.to_csv('data/dst/to_csv_out_a.csv')
df.to_csv('data/dst/to_csv_out_a.csv', mode='a', header=False)

df.to_csv('data/dst/to_csv_out_a_new_column.csv')

df_new = pd.read_csv('data/dst/to_csv_out_a_new_column.csv', index_col=0)
print(df_new)
#          age state  point
# name                     
# Alice     24    NY     64
# Bob       42    CA     92
# Charlie   18    CA     70

df_new['new_col'] = 'new data'
print(df_new)
#          age state  point   new_col
# name                               
# Alice     24    NY     64  new data
# Bob       42    CA     92  new data
# Charlie   18    CA     70  new data

df_new.to_csv('data/dst/to_csv_out_a_new_column.csv')

df_nan = df.copy()
df_nan.iat[0, 1] = float('nan')
df_nan.iat[1, 2] = float('nan')

print(df_nan)
#          age state  point
# name                     
# Alice     24   NaN   64.0
# Bob       42    CA    NaN
# Charlie   18    CA   70.0

df_nan.to_csv('data/dst/to_csv_out_nan.csv')

df_nan.to_csv('data/dst/to_csv_out_nan_rep.csv', na_rep='NaN')
