import pandas as pd
import seaborn as sns

df = sns.load_dataset("iris")
print(df.shape)
# (150, 5)

print(df.sample())
#      sepal_length  sepal_width  petal_length  petal_width    species
# 108           6.7          2.5           5.8          1.8  virginica

print(df.sample(n=3))
#     sepal_length  sepal_width  petal_length  petal_width     species
# 3            4.6          3.1           1.5          0.2      setosa
# 1            4.9          3.0           1.4          0.2      setosa
# 96           5.7          2.9           4.2          1.3  versicolor

print(df.sample(n=3, random_state=0))
#      sepal_length  sepal_width  petal_length  petal_width     species
# 114           5.8          2.8           5.1          2.4   virginica
# 62            6.0          2.2           4.0          1.0  versicolor
# 33            5.5          4.2           1.4          0.2      setosa

print(df.sample(frac=0.04))
#      sepal_length  sepal_width  petal_length  petal_width     species
# 119           6.0          2.2           5.0          1.5   virginica
# 97            6.2          2.9           4.3          1.3  versicolor
# 46            5.1          3.8           1.6          0.2      setosa
# 137           6.4          3.1           5.5          1.8   virginica
# 56            6.3          3.3           4.7          1.6  versicolor
# 62            6.0          2.2           4.0          1.0  versicolor

print(df.head(3).sample(n=3, replace=True))
#    sepal_length  sepal_width  petal_length  petal_width species
# 2           4.7          3.2           1.3          0.2  setosa
# 1           4.9          3.0           1.4          0.2  setosa
# 1           4.9          3.0           1.4          0.2  setosa

print(df.head(3).sample(n=5, replace=True))
#    sepal_length  sepal_width  petal_length  petal_width species
# 1           4.9          3.0           1.4          0.2  setosa
# 0           5.1          3.5           1.4          0.2  setosa
# 1           4.9          3.0           1.4          0.2  setosa
# 0           5.1          3.5           1.4          0.2  setosa
# 0           5.1          3.5           1.4          0.2  setosa

print(df.head().sample(n=2, axis=1))
#    sepal_width species
# 0          3.5  setosa
# 1          3.0  setosa
# 2          3.2  setosa
# 3          3.1  setosa
# 4          3.6  setosa
