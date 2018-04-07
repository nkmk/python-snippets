import numpy as np
import pandas as pd

df = pd.read_csv('data/src/titanic_train.csv', index_col=0).drop(['Name', 'Ticket', 'SibSp', 'Parch'], axis=1)

print(df.head())
#              Survived  Pclass     Sex   Age     Fare Cabin Embarked
# PassengerId                                                        
# 1                   0       3    male  22.0   7.2500   NaN        S
# 2                   1       1  female  38.0  71.2833   C85        C
# 3                   1       3  female  26.0   7.9250   NaN        S
# 4                   1       1  female  35.0  53.1000  C123        S
# 5                   0       3    male  35.0   8.0500   NaN        S

print(pd.pivot_table(df, index='Pclass', columns='Sex'))
#               Age                   Fare             Survived          
# Sex        female       male      female       male    female      male
# Pclass                                                                 
# 1       34.611765  41.281386  106.125798  67.226127  0.968085  0.368852
# 2       28.722973  30.740707   21.970121  19.741782  0.921053  0.157407
# 3       21.750000  26.507589   16.118810  12.661633  0.500000  0.135447

print(type(pd.pivot_table(df, index='Pclass', columns='Sex')))
# <class 'pandas.core.frame.DataFrame'>

print(pd.pivot_table(df, index='Pclass', columns='Sex', values='Age'))
# Sex        female       male
# Pclass                      
# 1       34.611765  41.281386
# 2       28.722973  30.740707
# 3       21.750000  26.507589

print(pd.pivot_table(df, index=['Sex', 'Pclass'], columns='Survived', values=['Age', 'Fare']))
#                      Age                   Fare            
# Survived               0          1           0           1
# Sex    Pclass                                              
# female 1       25.666667  34.939024  110.604167  105.978159
#        2       36.000000  28.080882   18.250000   22.288989
#        3       23.818182  19.329787   19.773093   12.464526
# male   1       44.581967  36.248000   62.894910   74.637320
#        2       33.369048  16.022000   19.488965   21.095100
#        3       27.255814  22.274211   12.204469   15.579696

print(pd.pivot_table(df, index='Sex', columns='Pclass', values='Age', margins=True))
# Pclass          1          2          3        All
# Sex                                               
# female  34.611765  28.722973  21.750000  27.915709
# male    41.281386  30.740707  26.507589  30.726645
# All     38.233441  29.877630  25.140620  29.699118

print(pd.pivot_table(df, index='Sex', columns='Pclass', values='Age',
                     margins=True, margins_name='Total'))
# Pclass          1          2          3      Total
# Sex                                               
# female  34.611765  28.722973  21.750000  27.915709
# male    41.281386  30.740707  26.507589  30.726645
# Total   38.233441  29.877630  25.140620  29.699118

print(pd.pivot_table(df, index='Sex', columns='Pclass', values='Age',
                     margins=True, aggfunc=np.min))
# Pclass     1     2     3   All
# Sex                           
# female  2.00  2.00  0.75  0.75
# male    0.92  0.67  0.42  0.42
# All     0.92  0.67  0.42  0.42

print(pd.pivot_table(df, index='Sex', columns='Pclass', values='Age',
                     margins=True, aggfunc=[np.min, np.max]))
#         amin                    amax                  
# Pclass     1     2     3   All     1     2     3   All
# Sex                                                   
# female  2.00  2.00  0.75  0.75  63.0  57.0  63.0  63.0
# male    0.92  0.67  0.42  0.42  80.0  70.0  74.0  80.0
# All     0.92  0.67  0.42  0.42  80.0  70.0  74.0  80.0

print(pd.pivot_table(df, index='Sex', columns='Pclass', values='Age',
                     margins=True, aggfunc=len))
# Pclass      1      2      3    All
# Sex                               
# female   94.0   76.0  144.0  261.0
# male    122.0  108.0  347.0  453.0
# All     186.0  173.0  355.0  714.0

print(len(df))
# 891

print(df.isnull().sum())
# Survived      0
# Pclass        0
# Sex           0
# Age         177
# Fare          0
# Cabin       687
# Embarked      2
# dtype: int64

print(pd.pivot_table(df, index='Sex', columns='Pclass', values='Age',
                     margins=True, aggfunc=len, dropna=False))
# Pclass      1      2      3    All
# Sex                               
# female   94.0   76.0  144.0  314.0
# male    122.0  108.0  347.0  577.0
# All     216.0  184.0  491.0  891.0
