import pandas as pd

df = pd.read_csv('data/src/titanic_train.csv')

df.drop(labels=['Name', 'Ticket', 'Cabin'], axis=1, inplace=True)

df_single = df.set_index('PassengerId')

print(df_single.head())
#              Survived  Pclass     Sex   Age  SibSp  Parch     Fare Embarked
# PassengerId                                                                
# 1                   0       3    male  22.0      1      0   7.2500        S
# 2                   1       1  female  38.0      1      0  71.2833        C
# 3                   1       3  female  26.0      0      0   7.9250        S
# 4                   1       1  female  35.0      1      0  53.1000        S
# 5                   0       3    male  35.0      0      0   8.0500        S

df_multi = df.set_index(['Sex', 'Pclass', 'Embarked', 'PassengerId']).sort_index()

print(df_multi.head())
#                                     Survived   Age  SibSp  Parch      Fare
# Sex    Pclass Embarked PassengerId                                        
# female 1      C        2                   1  38.0      1      0   71.2833
#                        32                  1   NaN      1      0  146.5208
#                        53                  1  49.0      1      0   76.7292
#                        178                 0  50.0      0      0   28.7125
#                        195                 1  44.0      0      0   27.7208

print(df_multi.tail())
#                                   Survived   Age  SibSp  Parch    Fare
# Sex  Pclass Embarked PassengerId                                      
# male 3      S        877                 0  20.0      0      0  9.8458
#                      878                 0  19.0      0      0  7.8958
#                      879                 0   NaN      0      0  7.8958
#                      882                 0  33.0      0      0  7.8958
#                      885                 0  25.0      0      0  7.0500

print(df_multi.mean())
# Survived     0.383838
# Age         29.699118
# SibSp        0.523008
# Parch        0.381594
# Fare        32.204208
# dtype: float64

print(df_single.mean())
# Survived     0.383838
# Pclass       2.308642
# Age         29.699118
# SibSp        0.523008
# Parch        0.381594
# Fare        32.204208
# dtype: float64

print(df_multi.max())
# Survived      1.0000
# Age          80.0000
# SibSp         8.0000
# Parch         6.0000
# Fare        512.3292
# dtype: float64

print(df_single.max())
# Survived          1
# Pclass            3
# Sex            male
# Age              80
# SibSp             8
# Parch             6
# Fare        512.329
# dtype: object

print(df_multi.mean(level='Sex'))
#         Survived        Age     SibSp     Parch       Fare
# Sex                                                       
# female  0.742038  27.915709  0.694268  0.649682  44.479818
# male    0.188908  30.726645  0.429809  0.235702  25.523893

print(df_multi.mean(level=0))
#         Survived        Age     SibSp     Parch       Fare
# Sex                                                       
# female  0.742038  27.915709  0.694268  0.649682  44.479818
# male    0.188908  30.726645  0.429809  0.235702  25.523893

print(df_multi.mean(level=1))
#         Survived        Age     SibSp     Parch       Fare
# Pclass                                                    
# 1       0.629630  38.233441  0.416667  0.356481  84.154687
# 2       0.472826  29.877630  0.402174  0.380435  20.662183
# 3       0.242363  25.140620  0.615071  0.393075  13.675550

print(df_multi.mean(level=2))
#           Survived        Age     SibSp     Parch       Fare
# Embarked                                                    
# C         0.553571  30.814769  0.386905  0.363095  59.954144
# Q         0.389610  28.089286  0.428571  0.168831  13.276030
# S         0.336957  29.445397  0.571429  0.413043  27.079812

print(df_multi.mean(level=['Sex', 'Pclass']))
#                Survived        Age     SibSp     Parch        Fare
# Sex    Pclass                                                     
# female 1       0.968085  34.611765  0.553191  0.457447  106.125798
#        2       0.921053  28.722973  0.486842  0.605263   21.970121
#        3       0.500000  21.750000  0.895833  0.798611   16.118810
# male   1       0.368852  41.281386  0.311475  0.278689   67.226127
#        2       0.157407  30.740707  0.342593  0.222222   19.741782
#        3       0.135447  26.507589  0.498559  0.224784   12.661633

print(df_multi.mean(level=[0, 1, 2]))
#                         Survived        Age     SibSp     Parch        Fare
# Sex    Pclass Embarked                                                     
# female 1      C         0.976744  36.052632  0.511628  0.302326  115.640309
#               Q         1.000000  33.000000  1.000000  0.000000   90.000000
#               S         0.958333  32.704545  0.604167  0.625000   99.026910
#        2      C         1.000000  19.142857  0.714286  0.571429   25.268457
#               Q         1.000000  30.000000  0.000000  0.000000   12.350000
#               S         0.910448  29.719697  0.477612  0.626866   21.912687
#        3      C         0.652174  14.062500  0.565217  0.826087   14.694926
#               Q         0.727273  22.850000  0.212121  0.242424   10.307833
#               S         0.375000  23.223684  1.238636  1.000000   18.670077
# male   1      C         0.404762  40.111111  0.238095  0.333333   93.536707
#               Q         0.000000  44.000000  2.000000  0.000000   90.000000
#               S         0.354430  41.897188  0.329114  0.253165   52.949947
#        2      C         0.200000  25.937500  0.500000  0.500000   25.421250
#               Q         0.000000  57.000000  0.000000  0.000000   12.350000
#               S         0.154639  30.875889  0.329897  0.195876   19.232474
#        3      C         0.232558  25.016800  0.232558  0.139535    9.352237
#               Q         0.076923  28.142857  0.589744  0.128205   11.924251
#               S         0.128302  26.574766  0.528302  0.252830   13.307149

print(df_single.groupby(by='Sex').mean())
#         Survived    Pclass        Age     SibSp     Parch       Fare
# Sex                                                                 
# female  0.742038  2.159236  27.915709  0.694268  0.649682  44.479818
# male    0.188908  2.389948  30.726645  0.429809  0.235702  25.523893

print(df_single.groupby(by=['Sex', 'Pclass', 'Embarked']).mean())
#                         Survived        Age     SibSp     Parch        Fare
# Sex    Pclass Embarked                                                     
# female 1      C         0.976744  36.052632  0.511628  0.302326  115.640309
#               Q         1.000000  33.000000  1.000000  0.000000   90.000000
#               S         0.958333  32.704545  0.604167  0.625000   99.026910
#        2      C         1.000000  19.142857  0.714286  0.571429   25.268457
#               Q         1.000000  30.000000  0.000000  0.000000   12.350000
#               S         0.910448  29.719697  0.477612  0.626866   21.912687
#        3      C         0.652174  14.062500  0.565217  0.826087   14.694926
#               Q         0.727273  22.850000  0.212121  0.242424   10.307833
#               S         0.375000  23.223684  1.238636  1.000000   18.670077
# male   1      C         0.404762  40.111111  0.238095  0.333333   93.536707
#               Q         0.000000  44.000000  2.000000  0.000000   90.000000
#               S         0.354430  41.897188  0.329114  0.253165   52.949947
#        2      C         0.200000  25.937500  0.500000  0.500000   25.421250
#               Q         0.000000  57.000000  0.000000  0.000000   12.350000
#               S         0.154639  30.875889  0.329897  0.195876   19.232474
#        3      C         0.232558  25.016800  0.232558  0.139535    9.352237
#               Q         0.076923  28.142857  0.589744  0.128205   11.924251
#               S         0.128302  26.574766  0.528302  0.252830   13.307149

print(df_multi.groupby(level='Sex').size())
# Sex
# female    314
# male      577
# dtype: int64

print(df_multi.groupby(level=2).size())
# Embarked
# C    168
# Q     77
# S    644
# dtype: int64

print(df_multi.groupby(level=[0, 1, 2]).size())
# Sex     Pclass  Embarked
# female  1       C            43
#                 Q             1
#                 S            48
#         2       C             7
#                 Q             2
#                 S            67
#         3       C            23
#                 Q            33
#                 S            88
# male    1       C            42
#                 Q             1
#                 S            79
#         2       C            10
#                 Q             1
#                 S            97
#         3       C            43
#                 Q            39
#                 S           265
# dtype: int64

print(df_single.groupby(by=['Sex', 'Pclass', 'Embarked']).size())
# Sex     Pclass  Embarked
# female  1       C            43
#                 Q             1
#                 S            48
#         2       C             7
#                 Q             2
#                 S            67
#         3       C            23
#                 Q            33
#                 S            88
# male    1       C            42
#                 Q             1
#                 S            79
#         2       C            10
#                 Q             1
#                 S            97
#         3       C            43
#                 Q            39
#                 S           265
# dtype: int64
