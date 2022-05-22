import pandas as pd
import seaborn as sns

df = sns.load_dataset("iris")
print(df.shape)
# (150, 5)

print(df.sample())
#      sepal_length  sepal_width  petal_length  petal_width    species
# 133           6.3          2.8           5.1          1.5  virginica

print(df.sample(axis=1))
#      petal_width
# 0            0.2
# 1            0.2
# 2            0.2
# 3            0.2
# 4            0.2
# ..           ...
# 145          2.3
# 146          1.9
# 147          2.0
# 148          2.3
# 149          1.8
# 
# [150 rows x 1 columns]

print(df.sample(n=3))
#     sepal_length  sepal_width  petal_length  petal_width     species
# 29           4.7          3.2           1.6          0.2      setosa
# 67           5.8          2.7           4.1          1.0  versicolor
# 18           5.7          3.8           1.7          0.3      setosa

print(df.sample(frac=0.04))
#      sepal_length  sepal_width  petal_length  petal_width     species
# 15            5.7          4.4           1.5          0.4      setosa
# 66            5.6          3.0           4.5          1.5  versicolor
# 131           7.9          3.8           6.4          2.0   virginica
# 64            5.6          2.9           3.6          1.3  versicolor
# 81            5.5          2.4           3.7          1.0  versicolor
# 137           6.4          3.1           5.5          1.8   virginica

# print(df.sample(n=3, frac=0.04))
# ValueError: Please enter a value for `frac` OR `n`, not both

print(df.sample(n=3, random_state=0))
#      sepal_length  sepal_width  petal_length  petal_width     species
# 114           5.8          2.8           5.1          2.4   virginica
# 62            6.0          2.2           4.0          1.0  versicolor
# 33            5.5          4.2           1.4          0.2      setosa

print(df.sample(n=3, random_state=0))
#      sepal_length  sepal_width  petal_length  petal_width     species
# 114           5.8          2.8           5.1          2.4   virginica
# 62            6.0          2.2           4.0          1.0  versicolor
# 33            5.5          4.2           1.4          0.2      setosa

print(df.head(3))
#    sepal_length  sepal_width  petal_length  petal_width species
# 0           5.1          3.5           1.4          0.2  setosa
# 1           4.9          3.0           1.4          0.2  setosa
# 2           4.7          3.2           1.3          0.2  setosa

print(df.head(3).sample(n=3, replace=True))
#    sepal_length  sepal_width  petal_length  petal_width species
# 0           5.1          3.5           1.4          0.2  setosa
# 0           5.1          3.5           1.4          0.2  setosa
# 2           4.7          3.2           1.3          0.2  setosa

print(df.head(3).sample(n=5, replace=True))
#    sepal_length  sepal_width  petal_length  petal_width species
# 1           4.9          3.0           1.4          0.2  setosa
# 2           4.7          3.2           1.3          0.2  setosa
# 0           5.1          3.5           1.4          0.2  setosa
# 0           5.1          3.5           1.4          0.2  setosa
# 1           4.9          3.0           1.4          0.2  setosa

print(df.head(3).sample(frac=2, replace=True))
#    sepal_length  sepal_width  petal_length  petal_width species
# 2           4.7          3.2           1.3          0.2  setosa
# 1           4.9          3.0           1.4          0.2  setosa
# 2           4.7          3.2           1.3          0.2  setosa
# 2           4.7          3.2           1.3          0.2  setosa
# 0           5.1          3.5           1.4          0.2  setosa
# 2           4.7          3.2           1.3          0.2  setosa

print(df.sample(n=3, ignore_index=True))
#    sepal_length  sepal_width  petal_length  petal_width     species
# 0           5.2          2.7           3.9          1.4  versicolor
# 1           6.3          2.5           4.9          1.5  versicolor
# 2           5.7          3.0           4.2          1.2  versicolor

print(df.sample(n=3).reset_index(drop=True))
#    sepal_length  sepal_width  petal_length  petal_width    species
# 0           4.9          3.1           1.5          0.2     setosa
# 1           7.9          3.8           6.4          2.0  virginica
# 2           6.3          2.8           5.1          1.5  virginica
