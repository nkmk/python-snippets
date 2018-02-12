import pandas as pd
import seaborn as sns

df = sns.load_dataset("iris")
print(df.shape)
# (150, 5)

print(df.head())
#    sepal_length  sepal_width  petal_length  petal_width species
# 0           5.1          3.5           1.4          0.2  setosa
# 1           4.9          3.0           1.4          0.2  setosa
# 2           4.7          3.2           1.3          0.2  setosa
# 3           4.6          3.1           1.5          0.2  setosa
# 4           5.0          3.6           1.4          0.2  setosa

print(df.head(3))
#    sepal_length  sepal_width  petal_length  petal_width species
# 0           5.1          3.5           1.4          0.2  setosa
# 1           4.9          3.0           1.4          0.2  setosa
# 2           4.7          3.2           1.3          0.2  setosa

print(df.tail())
#      sepal_length  sepal_width  petal_length  petal_width    species
# 145           6.7          3.0           5.2          2.3  virginica
# 146           6.3          2.5           5.0          1.9  virginica
# 147           6.5          3.0           5.2          2.0  virginica
# 148           6.2          3.4           5.4          2.3  virginica
# 149           5.9          3.0           5.1          1.8  virginica

print(df.tail(3))
#      sepal_length  sepal_width  petal_length  petal_width    species
# 147           6.5          3.0           5.2          2.0  virginica
# 148           6.2          3.4           5.4          2.3  virginica
# 149           5.9          3.0           5.1          1.8  virginica

print(df[50:55])
#     sepal_length  sepal_width  petal_length  petal_width     species
# 50           7.0          3.2           4.7          1.4  versicolor
# 51           6.4          3.2           4.5          1.5  versicolor
# 52           6.9          3.1           4.9          1.5  versicolor
# 53           5.5          2.3           4.0          1.3  versicolor
# 54           6.5          2.8           4.6          1.5  versicolor

print(df[:5])
#    sepal_length  sepal_width  petal_length  petal_width species
# 0           5.1          3.5           1.4          0.2  setosa
# 1           4.9          3.0           1.4          0.2  setosa
# 2           4.7          3.2           1.3          0.2  setosa
# 3           4.6          3.1           1.5          0.2  setosa
# 4           5.0          3.6           1.4          0.2  setosa

print(df[-5:])
#      sepal_length  sepal_width  petal_length  petal_width    species
# 145           6.7          3.0           5.2          2.3  virginica
# 146           6.3          2.5           5.0          1.9  virginica
# 147           6.5          3.0           5.2          2.0  virginica
# 148           6.2          3.4           5.4          2.3  virginica
# 149           5.9          3.0           5.1          1.8  virginica

print(df.head(1))
print(type(df.head(1)))
#    sepal_length  sepal_width  petal_length  petal_width species
# 0           5.1          3.5           1.4          0.2  setosa
# <class 'pandas.core.frame.DataFrame'>

print(df.iloc[0])
print(type(df.iloc[0]))
# sepal_length       5.1
# sepal_width        3.5
# petal_length       1.4
# petal_width        0.2
# species         setosa
# Name: 0, dtype: object
# <class 'pandas.core.series.Series'>

print(df.iloc[0]['sepal_length'])
# 5.1

print(df.iloc[-1])
print(type(df.iloc[-1]))
# sepal_length          5.9
# sepal_width             3
# petal_length          5.1
# petal_width           1.8
# species         virginica
# Name: 149, dtype: object
# <class 'pandas.core.series.Series'>

print(df.iloc[-1]['sepal_length'])
# 5.9

print(df['sepal_length'][0])
# 5.1

# print(df['sepal_length'][-1])
# KeyError

print(df['sepal_length'].iat[-1])
# 5.9

print(df['sepal_length'].values[0])
# 5.1

print(df['sepal_length'].values[-1])
# 5.9
