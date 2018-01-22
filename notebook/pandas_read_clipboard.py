import pandas as pd

df = pd.read_clipboard()
print(df)
#    バージョン    リリース日[16]
# 0    3.0   2008年12月3日
# 1    3.1   2009年6月27日
# 2    3.2   2011年2月20日
# 3    3.3   2012年9月29日
# 4    3.4   2014年3月16日
# 5    3.5   2015年9月13日
# 6    3.6  2016年12月23日

df.to_csv('data/dst/test.csv')
