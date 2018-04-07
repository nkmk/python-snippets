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

print(pd.crosstab(df['Sex'], df['Pclass']))
# Pclass    1    2    3
# Sex                  
# female   94   76  144
# male    122  108  347

print(type(pd.crosstab(df['Sex'], df['Pclass'])))
# <class 'pandas.core.frame.DataFrame'>

print(pd.crosstab([df['Sex'], df['Survived']], [df['Pclass'], df['Embarked']]))
# Pclass            1         2          3         
# Embarked          C  Q   S  C  Q   S   C   Q    S
# Sex    Survived                                  
# female 0          1  0   2  0  0   6   8   9   55
#        1         42  1  46  7  2  61  15  24   33
# male   0         25  1  51  8  1  82  33  36  231
#        1         17  0  28  2  0  15  10   3   34

print(pd.crosstab([df['Sex'], df['Survived']], [df['Pclass'], df['Embarked']],
                  margins=True))
# Pclass            1           2           3           All
# Embarked          C  Q    S   C  Q    S   C   Q    S     
# Sex    Survived                                          
# female 0          1  0    2   0  0    6   8   9   55   81
#        1         42  1   46   7  2   61  15  24   33  231
# male   0         25  1   51   8  1   82  33  36  231  468
#        1         17  0   28   2  0   15  10   3   34  109
# All              85  2  127  17  3  164  66  72  353  889

print(pd.crosstab([df['Sex'], df['Survived']], [df['Pclass'], df['Embarked']],
                  margins=True, margins_name='Total'))
# Pclass            1           2           3          Total
# Embarked          C  Q    S   C  Q    S   C   Q    S      
# Sex    Survived                                           
# female 0          1  0    2   0  0    6   8   9   55    81
#        1         42  1   46   7  2   61  15  24   33   231
# male   0         25  1   51   8  1   82  33  36  231   468
#        1         17  0   28   2  0   15  10   3   34   109
# Total            85  2  127  17  3  164  66  72  353   889

print(pd.crosstab(df['Sex'], df['Pclass'], margins=True, normalize=True))
# Pclass         1         2         3       All
# Sex                                           
# female  0.105499  0.085297  0.161616  0.352413
# male    0.136925  0.121212  0.389450  0.647587
# All     0.242424  0.206510  0.551066  1.000000

print(pd.crosstab(df['Sex'], df['Pclass'], margins=True, normalize='index'))
# Pclass         1         2         3
# Sex                                 
# female  0.299363  0.242038  0.458599
# male    0.211438  0.187175  0.601386
# All     0.242424  0.206510  0.551066

print(pd.crosstab(df['Sex'], df['Pclass'], margins=True, normalize='columns'))
# Pclass         1         2         3       All
# Sex                                           
# female  0.435185  0.413043  0.293279  0.352413
# male    0.564815  0.586957  0.706721  0.647587

# print(pd.crosstab(df['Sex'], [df['Pclass'], df['Embarked']],
#                   margins=True, normalize=True))
# TypeError: Expected tuple, got str

print(pd.crosstab(df['Sex'], [df['Pclass'], df['Embarked']],
                  margins=True, normalize='index'))
# Pclass           1                             2                      \
# Embarked         C         Q         S         C         Q         S   
# Sex                                                                    
# female    0.137821  0.003205  0.153846  0.022436  0.006410  0.214744   
# male      0.072790  0.001733  0.136915  0.017331  0.001733  0.168111   
# All       0.095613  0.002250  0.142857  0.019123  0.003375  0.184477   
# Pclass           3                      
# Embarked         C         Q         S  
# Sex                                     
# female    0.073718  0.105769  0.282051  
# male      0.074523  0.067591  0.459272  
# All       0.074241  0.080990  0.397075  

# print(pd.crosstab(df['Sex'], [df['Pclass'], df['Embarked']],
#                   margins=True, normalize='columns'))
# ValueError: Length of new names must be 1, got 2

print(pd.crosstab(df['Sex'], [df['Pclass'], df['Embarked']], normalize=True))
# Pclass           1                             2                      \
# Embarked         C         Q         S         C         Q         S   
# Sex                                                                    
# female    0.048369  0.001125  0.053993  0.007874  0.002250  0.075366   
# male      0.047244  0.001125  0.088864  0.011249  0.001125  0.109111   
# Pclass           3                     
# Embarked         C        Q         S  
# Sex                                    
# female    0.025872  0.03712  0.098988  
# male      0.048369  0.04387  0.298088  

print(pd.crosstab(df['Sex'], [df['Pclass'], df['Embarked']], normalize='index'))
# Pclass           1                             2                      \
# Embarked         C         Q         S         C         Q         S   
# Sex                                                                    
# female    0.137821  0.003205  0.153846  0.022436  0.006410  0.214744   
# male      0.072790  0.001733  0.136915  0.017331  0.001733  0.168111   
# Pclass           3                      
# Embarked         C         Q         S  
# Sex                                     
# female    0.073718  0.105769  0.282051  
# male      0.074523  0.067591  0.459272  

print(pd.crosstab(df['Sex'], [df['Pclass'], df['Embarked']], normalize='columns'))
# Pclass           1                        2                             3  \
# Embarked         C    Q         S         C         Q         S         C   
# Sex                                                                         
# female    0.505882  0.5  0.377953  0.411765  0.666667  0.408537  0.348485   
# male      0.494118  0.5  0.622047  0.588235  0.333333  0.591463  0.651515   
# Pclass                        
# Embarked         Q         S  
# Sex                           
# female    0.458333  0.249292  
# male      0.541667  0.750708  
