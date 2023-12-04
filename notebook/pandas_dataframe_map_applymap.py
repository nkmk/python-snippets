import pandas as pd

print(pd.__version__)
# 2.1.2

df = pd.DataFrame([[1, 10, 100], [2, 20, 200]])
print(df)
#    0   1    2
# 0  1  10  100
# 1  2  20  200

print(df.map(hex))
#      0     1     2
# 0  0x1   0xa  0x64
# 1  0x2  0x14  0xc8

print(df.applymap(hex))
#      0     1     2
# 0  0x1   0xa  0x64
# 1  0x2  0x14  0xc8
# 
# /var/folders/rf/b7l8_vgj5mdgvghn_326rn_c0000gn/T/ipykernel_36685/2076800564.py:1: FutureWarning: DataFrame.applymap has been deprecated. Use DataFrame.map instead.
#   print(df.applymap(hex))

df_nan = pd.DataFrame([[1, float('nan'), 100], [2, 20, 200]])
print(df_nan)
#    0     1    2
# 0  1   NaN  100
# 1  2  20.0  200

# print(df_nan.map(lambda x: hex(int(x))))
# ValueError: cannot convert float NaN to integer

print(df_nan.map(lambda x: hex(int(x)), na_action='ignore'))
#      0     1     2
# 0  0x1   NaN  0x64
# 1  0x2  0x14  0xc8

df = pd.DataFrame([['1', 'A', 'F'], ['11', 'AA', 'FF']])
print(df)
#     0   1   2
# 0   1   A   F
# 1  11  AA  FF

print(df.map(int, base=16))
#     0    1    2
# 0   1   10   15
# 1  17  170  255
