import warnings
import pandas as pd

df = pd.DataFrame([[0, 1, 2], [3, 4, 5]])

df.ix[0, 0] = 0
# /usr/local/lib/python3.7/site-packages/ipykernel_launcher.py:1: FutureWarning: 
# .ix is deprecated. Please use
# .loc for label based indexing or
# .iloc for positional indexing
# 
# See the documentation here:
# http://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#ix-indexer-is-deprecated
#   """Entry point for launching an IPython kernel.

df.iloc[:1][0] = 0
# /usr/local/lib/python3.7/site-packages/ipykernel_launcher.py:1: SettingWithCopyWarning: 
# A value is trying to be set on a copy of a slice from a DataFrame.
# Try using .loc[row_indexer,col_indexer] = value instead
# 
# See the caveats in the documentation: http://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy
#   """Entry point for launching an IPython kernel.

warnings.simplefilter('ignore')

df.ix[0, 0] = 0

df.iloc[:1][0] = 0

warnings.resetwarnings()

warnings.simplefilter('ignore', FutureWarning)

df.ix[0, 0] = 0

df.iloc[:1][0] = 0
# /usr/local/lib/python3.7/site-packages/ipykernel_launcher.py:1: SettingWithCopyWarning: 
# A value is trying to be set on a copy of a slice from a DataFrame.
# Try using .loc[row_indexer,col_indexer] = value instead
# 
# See the caveats in the documentation: http://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy
#   """Entry point for launching an IPython kernel.

warnings.resetwarnings()

# warnings.simplefilter('ignore', SettingWithCopyWarning)
# NameError: name 'SettingWithCopyWarning' is not defined

warnings.simplefilter('ignore', pd.core.common.SettingWithCopyWarning)

df.ix[0, 0] = 0
# /usr/local/lib/python3.7/site-packages/ipykernel_launcher.py:1: FutureWarning: 
# .ix is deprecated. Please use
# .loc for label based indexing or
# .iloc for positional indexing
# 
# See the documentation here:
# http://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#ix-indexer-is-deprecated
#   """Entry point for launching an IPython kernel.

df.iloc[:1][0] = 0

warnings.resetwarnings()

warnings.simplefilter('error')

# df.ix[0, 0] = 0
# FutureWarning: ...

warnings.resetwarnings()

warnings.simplefilter('ignore', FutureWarning)
warnings.simplefilter('error', pd.core.common.SettingWithCopyWarning)

df.ix[0, 0] = 0

# df.iloc[:1][0] = 0
# SettingWithCopyWarning: ...

warnings.resetwarnings()

with warnings.catch_warnings():
    warnings.simplefilter('ignore')
    df.ix[0, 0] = 0

df.ix[0, 0] = 0
# /usr/local/lib/python3.7/site-packages/ipykernel_launcher.py:1: FutureWarning: 
# .ix is deprecated. Please use
# .loc for label based indexing or
# .iloc for positional indexing
# 
# See the documentation here:
# http://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#ix-indexer-is-deprecated
#   """Entry point for launching an IPython kernel.
