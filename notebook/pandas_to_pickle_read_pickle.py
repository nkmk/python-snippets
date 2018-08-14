import pandas as pd

df = pd.DataFrame({'list': [[0, 0], [0, 1], [1, 0], [1, 1]]},
                  index=pd.date_range('2018-01-01', '2018-01-04', freq='D'))

print(df)
#               list
# 2018-01-01  [0, 0]
# 2018-01-02  [0, 1]
# 2018-01-03  [1, 0]
# 2018-01-04  [1, 1]

print(df.index)
# DatetimeIndex(['2018-01-01', '2018-01-02', '2018-01-03', '2018-01-04'], dtype='datetime64[ns]', freq='D')

print(type(df['list'][0]))
# <class 'list'>

df.to_csv('data/dst/pandas_obj.csv')

df_from_csv = pd.read_csv('data/dst/pandas_obj.csv', index_col=0, parse_dates=True)

print(df_from_csv)
#               list
# 2018-01-01  [0, 0]
# 2018-01-02  [0, 1]
# 2018-01-03  [1, 0]
# 2018-01-04  [1, 1]

print(df_from_csv.index)
# DatetimeIndex(['2018-01-01', '2018-01-02', '2018-01-03', '2018-01-04'], dtype='datetime64[ns]', freq=None)

print(type(df_from_csv['list'][0]))
# <class 'str'>

df_from_csv['list'] = df_from_csv['list'].apply(eval)

print(df_from_csv)
#               list
# 2018-01-01  [0, 0]
# 2018-01-02  [0, 1]
# 2018-01-03  [1, 0]
# 2018-01-04  [1, 1]

print(type(df_from_csv['list'][0]))
# <class 'list'>

df.to_pickle('data/dst/pandas_obj.pkl')

df_from_pkl = pd.read_pickle('data/dst/pandas_obj.pkl')

print(df_from_pkl)
#               list
# 2018-01-01  [0, 0]
# 2018-01-02  [0, 1]
# 2018-01-03  [1, 0]
# 2018-01-04  [1, 1]

print(df_from_pkl.index)
# DatetimeIndex(['2018-01-01', '2018-01-02', '2018-01-03', '2018-01-04'], dtype='datetime64[ns]', freq='D')

print(type(df_from_pkl['list'][0]))
# <class 'list'>

df.to_pickle('data/dst/pandas_obj.zip')

df_from_pkl_zip = pd.read_pickle('data/dst/pandas_obj.zip')

print(df_from_pkl_zip)
#               list
# 2018-01-01  [0, 0]
# 2018-01-02  [0, 1]
# 2018-01-03  [1, 0]
# 2018-01-04  [1, 1]
