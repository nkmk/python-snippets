import pandas as pd

df = pd.DataFrame({'a': [0.123456789], 'b': [0.987654321]})

df
#           a         b
# 0  0.123457  0.987654

print(pd.options.display.precision)
# 6

%precision 3
# '%.3f'

print(pd.options.display.precision)
# 6

df
#           a         b
# 0  0.123457  0.987654

pd.options.display.precision = 3

df
#        a      b
# 0  0.123  0.988

print(df)
#        a      b
# 0  0.123  0.988
