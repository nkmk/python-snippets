import pandas as pd

df = pd.DataFrame({'a': [0, 1, 2], 'b': [3, 4, 5]})
print(df)
#    a  b
# 0  0  3
# 1  1  4
# 2  2  5

df.to_clipboard()

# 	a	b
# 0	0	3
# 1	1	4
# 2	2	5

df.to_clipboard(excel=False)

#    a  b
# 0  0  3
# 1  1  4
# 2  2  5

df.to_clipboard(sep=',')

# ,a,b
# 0,0,3
# 1,1,4
# 2,2,5
