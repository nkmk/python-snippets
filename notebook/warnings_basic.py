import warnings
import pandas as pd

df = pd.DataFrame([[0, 1, 2], [3, 4, 5]])

print(100 is 100)
# True
# 
# <>:1: SyntaxWarning: "is" with a literal. Did you mean "=="?
# <>:1: SyntaxWarning: "is" with a literal. Did you mean "=="?
# /var/folders/rf/b7l8_vgj5mdgvghn_326rn_c0000gn/T/ipykernel_60077/3973932639.py:1: SyntaxWarning: "is" with a literal. Did you mean "=="?
#   print(100 is 100)

df.iloc[:1][0] = 0
# /var/folders/rf/b7l8_vgj5mdgvghn_326rn_c0000gn/T/ipykernel_60077/1345802814.py:1: SettingWithCopyWarning: 
# A value is trying to be set on a copy of a slice from a DataFrame.
# Try using .loc[row_indexer,col_indexer] = value instead
# 
# See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy
#   df.iloc[:1][0] = 0

warnings.simplefilter('ignore')

print(100 is 100)
# True

df.iloc[:1][0] = 0

warnings.resetwarnings()

warnings.simplefilter('ignore', SyntaxWarning)

print(100 is 100)
# True

df.iloc[:1][0] = 0
# /var/folders/rf/b7l8_vgj5mdgvghn_326rn_c0000gn/T/ipykernel_60077/1345802814.py:1: SettingWithCopyWarning: 
# A value is trying to be set on a copy of a slice from a DataFrame.
# Try using .loc[row_indexer,col_indexer] = value instead
# 
# See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy
#   df.iloc[:1][0] = 0

warnings.resetwarnings()

# warnings.simplefilter('ignore', SettingWithCopyWarning)
# NameError: name 'SettingWithCopyWarning' is not defined

warnings.simplefilter('ignore', pd.errors.SettingWithCopyWarning)

print(100 is 100)
# True
# 
# <>:1: SyntaxWarning: "is" with a literal. Did you mean "=="?
# <>:1: SyntaxWarning: "is" with a literal. Did you mean "=="?
# /var/folders/rf/b7l8_vgj5mdgvghn_326rn_c0000gn/T/ipykernel_60077/3973932639.py:1: SyntaxWarning: "is" with a literal. Did you mean "=="?
#   print(100 is 100)

df.iloc[:1][0] = 0

warnings.resetwarnings()

warnings.simplefilter('error')

# print(100 is 100)
# SyntaxError: "is" with a literal. Did you mean "=="?

warnings.resetwarnings()

warnings.simplefilter('ignore', SyntaxWarning)
warnings.simplefilter('error', pd.errors.SettingWithCopyWarning)

print(100 is 100)
# True

# df.iloc[:1][0] = 0
# SettingWithCopyWarning: ...

warnings.resetwarnings()

with warnings.catch_warnings():
    warnings.simplefilter('ignore')
    df.iloc[:1][0] = 0

df.iloc[:1][0] = 0
# /var/folders/rf/b7l8_vgj5mdgvghn_326rn_c0000gn/T/ipykernel_60077/1345802814.py:1: SettingWithCopyWarning: 
# A value is trying to be set on a copy of a slice from a DataFrame.
# Try using .loc[row_indexer,col_indexer] = value instead
# 
# See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy
#   df.iloc[:1][0] = 0

with warnings.catch_warnings(action='ignore', category=pd.errors.SettingWithCopyWarning):
    df.iloc[:1][0] = 0
