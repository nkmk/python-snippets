import pandas as pd

df = pd.DataFrame({'col1': [0.123456789, 1000000000.0],
                   'col2': [123456789.0, 0.0],
                   'col3': [123456789, 0]})
print(df)
#            col1         col2       col3
# 0  1.234568e-01  123456789.0  123456789
# 1  1.000000e+09          0.0          0

print(df.dtypes)
# col1    float64
# col2    float64
# col3      int64
# dtype: object

print(df.iat[0, 0])
# 0.123456789

print(df.iat[1, 0])
# 1000000000.0

df.to_csv('data/dst/to_csv_out_float_default.csv')

print('%.3f' % 0.123456789)
# 0.123

print('%.3f' % 123456789)
# 123456789.000

df.to_csv('data/dst/to_csv_out_float_format_3f.csv', float_format='%.3f')

print('%.3e' % 0.123456789)
# 1.235e-01

print('%.3e' % 123456789)
# 1.235e+08

df.to_csv('data/dst/to_csv_out_float_format_3e.csv', float_format='%.3e')

df['col1'] = df['col1'].map('{:.3f}'.format)
df['col2'] = df['col2'].map('{:.3e}'.format)
df['col3'] = df['col3'].map('{:#010x}'.format)

print(df)
#              col1       col2        col3
# 0           0.123  1.235e+08  0x075bcd15
# 1  1000000000.000  0.000e+00  0x00000000

print(df.dtypes)
# col1    object
# col2    object
# col3    object
# dtype: object

df.to_csv('data/dst/to_csv_out_float_format_str.csv')

df = pd.read_csv('data/dst/to_csv_out_float_format_str.csv', index_col=0)
print(df)
#            col1         col2        col3
# 0  1.230000e-01  123500000.0  0x075bcd15
# 1  1.000000e+09          0.0  0x00000000

print(df.dtypes)
# col1    float64
# col2    float64
# col3     object
# dtype: object

df['col3'] = df['col3'].map(lambda x: int(x, 16))
print(df)
#            col1         col2       col3
# 0  1.230000e-01  123500000.0  123456789
# 1  1.000000e+09          0.0          0

print(df.dtypes)
# col1    float64
# col2    float64
# col3      int64
# dtype: object
