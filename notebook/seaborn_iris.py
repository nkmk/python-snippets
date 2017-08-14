import seaborn as sns

sns.set(style="ticks")

df = sns.load_dataset("iris")

# http://seaborn.pydata.org/generated/seaborn.pairplot.html
sns.pairplot(df, hue='species', markers=["o", "s", "+"]).savefig('data/dst/seaborn_iris.png')

# ![seaborn_iris](data/dst/seaborn_iris.png)
