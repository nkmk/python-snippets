import pandas as pd

df = pd.DataFrame([[0, 10, 20], [30, 40, 50], [60, 70, 80]],
                  index=[2, 0, 1], columns=[1, 2, 0])
print(df)
#     1   2   0
# 2   0  10  20
# 0  30  40  50
# 1  60  70  80

print(df[0])
# 2    20
# 0    50
# 1    80
# Name: 0, dtype: int64

print(df[[0, 2]])
#     0   2
# 2  20  10
# 0  50  40
# 1  80  70

print(df[:2])
#     1   2   0
# 2   0  10  20
# 0  30  40  50

print(df[-2:])
#     1   2   0
# 0  30  40  50
# 1  60  70  80

print(df.loc[:2])
#    1   2   0
# 2  0  10  20

print(df.iloc[:2])
#     1   2   0
# 2   0  10  20
# 0  30  40  50

s = df[2]
print(s)
# 2    10
# 0    40
# 1    70
# Name: 2, dtype: int64

print(s[0])
# 40

print(s.at[0])
# 40

print(s.iat[0])
# 10

# print(s[-1])
# KeyError: -1

print(s.iat[-1])
# 70
