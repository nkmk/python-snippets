import pandas as pd

df = pd.DataFrame({'s': ['X,Y,Z', 'X', 'XY,Y', 'Y,Z,XY']},
                  index=['a', 'b', 'c', 'd'])

print(df)
#         s
# a   X,Y,Z
# b       X
# c    XY,Y
# d  Y,Z,XY

df['l'] = df['s'].map(lambda x: x.split(','))
print(df)
#         s           l
# a   X,Y,Z   [X, Y, Z]
# b       X         [X]
# c    XY,Y     [XY, Y]
# d  Y,Z,XY  [Y, Z, XY]

print(df.dtypes)
# s    object
# l    object
# dtype: object

print(type(df.at['a', 's']))
# <class 'str'>

print(type(df.at['a', 'l']))
# <class 'list'>

print(df['s'].map(lambda x: [s.strip() for s in x.split(',')]))
# a     [X, Y, Z]
# b           [X]
# c       [XY, Y]
# d    [Y, Z, XY]
# Name: s, dtype: object

print(df['l'].map(len))
# a    3
# b    1
# c    2
# d    3
# Name: l, dtype: int64

print(df['l'].map(sorted))
# a     [X, Y, Z]
# b           [X]
# c       [XY, Y]
# d    [XY, Y, Z]
# Name: l, dtype: object

print(df['l'].map(lambda x: ','.join(x)))
# a     X,Y,Z
# b         X
# c      XY,Y
# d    Y,Z,XY
# Name: l, dtype: object

print(df['l'].map(','.join))
# a     X,Y,Z
# b         X
# c      XY,Y
# d    Y,Z,XY
# Name: l, dtype: object

print(df['l'].map(lambda x: ','.join(sorted(x))))
# a     X,Y,Z
# b         X
# c      XY,Y
# d    XY,Y,Z
# Name: l, dtype: object

df['l'].map(lambda x: x.append('A'))
print(df)
#         s              l
# a   X,Y,Z   [X, Y, Z, A]
# b       X         [X, A]
# c    XY,Y     [XY, Y, A]
# d  Y,Z,XY  [Y, Z, XY, A]

df['l'].map(lambda x: x.remove('Z') if 'Z' in x else x)
print(df)
#         s           l
# a   X,Y,Z   [X, Y, A]
# b       X      [X, A]
# c    XY,Y  [XY, Y, A]
# d  Y,Z,XY  [Y, XY, A]

print(df['l'].map(lambda x: 'X' in x))
# a     True
# b     True
# c    False
# d    False
# Name: l, dtype: bool

print(df[df['l'].map(lambda x: 'X' in x)])
#        s          l
# a  X,Y,Z  [X, Y, A]
# b      X     [X, A]

print(df['s'].str.contains('Z'))
# a     True
# b    False
# c    False
# d     True
# Name: s, dtype: bool

print(df[df['s'].str.contains('Z')])
#         s           l
# a   X,Y,Z   [X, Y, A]
# d  Y,Z,XY  [Y, XY, A]
