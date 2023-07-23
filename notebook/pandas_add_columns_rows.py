import pandas as pd

print(pd.__version__)
# 2.0.3

df = pd.DataFrame()
for i in range(101):
    df[i] = 0
# PerformanceWarning: DataFrame is highly fragmented.
# This is usually the result of calling `frame.insert` many times, which has poor performance.
# Consider joining all columns at once using pd.concat(axis=1) instead.
# To get a de-fragmented frame, use `newframe = frame.copy()`
# /var/folders/rf/b7l8_vgj5mdgvghn_326rn_c0000gn/T/ipykernel_77347/2582768187.py:3: PerformanceWarning: DataFrame is highly fragmented.  This is usually the result of calling `frame.insert` many times, which has poor performance.  Consider joining all columns at once using pd.concat(axis=1) instead. To get a de-fragmented frame, use `newframe = frame.copy()`
#   df[i] = 0

df = pd.DataFrame({'col1': [1, 2, 3], 'col2': [10, 20, 30], 'col3': [100, 200, 300]},
                  index=['row1', 'row2', 'row3'])
print(df)
#       col1  col2  col3
# row1     1    10   100
# row2     2    20   200
# row3     3    30   300

l_data = []
l_label = []

for i in range(4, 7):
    l_data.append([i, i * 10, i * 100])
    l_label.append(f'row{i}')

print(l_data)
# [[4, 40, 400], [5, 50, 500], [6, 60, 600]]

print(l_label)
# ['row4', 'row5', 'row6']

df_append = pd.DataFrame(l_data, index=l_label, columns=df.columns)
print(df_append)
#       col1  col2  col3
# row4     4    40   400
# row5     5    50   500
# row6     6    60   600

df_result = pd.concat([df, df_append])
print(df_result)
#       col1  col2  col3
# row1     1    10   100
# row2     2    20   200
# row3     3    30   300
# row4     4    40   400
# row5     5    50   500
# row6     6    60   600

l_data = []
l_label = []

for i in range(3, 6):
    l_data.append([10**i, 2 * 10**i, 3 * 10**i])
    l_label.append(f'col{i + 1}')

print(l_data)
# [[1000, 2000, 3000], [10000, 20000, 30000], [100000, 200000, 300000]]

print(l_label)
# ['col4', 'col5', 'col6']

df_append = pd.DataFrame(zip(*l_data), index=df.index, columns=l_label)
print(df_append)
#       col4   col5    col6
# row1  1000  10000  100000
# row2  2000  20000  200000
# row3  3000  30000  300000

df_result = pd.concat([df, df_append], axis=1)
print(df_result)
#       col1  col2  col3  col4   col5    col6
# row1     1    10   100  1000  10000  100000
# row2     2    20   200  2000  20000  200000
# row3     3    30   300  3000  30000  300000

d = {}

for i in range(3, 6):
    d[f'col{i + 1}'] = [10**i, 2 * 10**i, 3 * 10**i]

print(d)
# {'col4': [1000, 2000, 3000], 'col5': [10000, 20000, 30000], 'col6': [100000, 200000, 300000]}

df_append = pd.DataFrame(d, index=df.index)
print(df_append)
#       col4   col5    col6
# row1  1000  10000  100000
# row2  2000  20000  200000
# row3  3000  30000  300000

df_result = pd.concat([df, df_append], axis=1)
print(df_result)
#       col1  col2  col3  col4   col5    col6
# row1     1    10   100  1000  10000  100000
# row2     2    20   200  2000  20000  200000
# row3     3    30   300  3000  30000  300000
