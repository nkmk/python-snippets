# %matplotlib inline

import pandas as pd
import seaborn as sns

df = pd.read_csv('data/src/iris.csv', index_col=0)
# df = sns.load_dataset("iris")

print(df.head())
#    sepal_length  sepal_width  petal_length  petal_width species
# 0           5.1          3.5           1.4          0.2  setosa
# 1           4.9          3.0           1.4          0.2  setosa
# 2           4.7          3.2           1.3          0.2  setosa
# 3           4.6          3.1           1.5          0.2  setosa
# 4           5.0          3.6           1.4          0.2  setosa

print(df.dtypes)
# sepal_length    float64
# sepal_width     float64
# petal_length    float64
# petal_width     float64
# species          object
# dtype: object

print(df['species'].value_counts())
# versicolor    50
# setosa        50
# virginica     50
# Name: species, dtype: int64

pg = sns.pairplot(df)
print(type(pg))
# <class 'seaborn.axisgrid.PairGrid'>

pg.savefig('data/dst/seaborn_pairplot_default.png')

sns.pairplot(df).savefig('data/dst/seaborn_pairplot_default.png')

sns.pairplot(df, hue='species').savefig('data/dst/seaborn_pairplot_hue.png')

sns.pairplot(df, hue='species',
             hue_order=['virginica', 'versicolor', 'setosa']).savefig('data/dst/seaborn_pairplot_hue_order.png')

sns.pairplot(df, hue='species', palette='Blues').savefig('data/dst/seaborn_pairplot_palette.png')

sns.pairplot(df, hue='species',
             palette={'setosa': 'red',
                      'versicolor': '#00ff00',
                      'virginica': 'blue'}).savefig('data/dst/seaborn_pairplot_palette_dict.png')

sns.pairplot(df, hue='species',
             vars=['sepal_length', 'sepal_width']).savefig('data/dst/seaborn_pairplot_vars.png')

sns.pairplot(df, hue='species',
             x_vars=['sepal_length', 'sepal_width'],
             y_vars=['petal_length', 'petal_width']).savefig('data/dst/seaborn_pairplot_xy_vars.png')

sns.pairplot(df, hue='species', markers='+').savefig('data/dst/seaborn_pairplot_markers.png')

sns.pairplot(df, hue='species', markers=['+', 's', 'd']).savefig('data/dst/seaborn_pairplot_markers_multi.png')

sns.pairplot(df, hue='species', kind='reg').savefig('data/dst/seaborn_pairplot_kind_reg.png')

sns.pairplot(df, hue='species', diag_kind='kde').savefig('data/dst/seaborn_pairplot_diag_kind_kde.png')

sns.pairplot(df, hue='species', size=2).savefig('data/dst/seaborn_pairplot_size.png')

sns.pairplot(df, hue='species',
             plot_kws={'alpha': 0.2},
             diag_kws={'bins': 20, 'histtype': 'step'}).savefig('data/dst/seaborn_pairplot_kws.png')

sns.pairplot(df, hue='species', kind='reg',
             plot_kws={'ci': None,
                       'marker': '+',
                       'scatter_kws': {'alpha': 0.4},
                       'line_kws': {'linestyle': '--'}}).savefig('data/dst/seaborn_pairplot_kind_reg_kws.png')
