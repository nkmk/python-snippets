import warnings
import pandas as pd

print(pd.__version__)
# 2.0.3

warnings.simplefilter('ignore')

%%timeit
df_loc = pd.DataFrame([[0, 0, 0], [1, 1, 1], [2, 2, 2]])

for i in range(3, 1003):
    df_loc.loc[i] = [i] * 3
# 150 ms ± 4.67 ms per loop (mean ± std. dev. of 7 runs, 10 loops each)

%%timeit
df = pd.DataFrame([[0, 0, 0], [1, 1, 1], [2, 2, 2]])
l_data = []
l_label = []

for i in range(3, 1003):
    l_data.append([i] * 3)
    l_label.append(i)

df_concat = pd.concat([df, pd.DataFrame(l_data, index=l_label, columns=df.columns)])
# 487 µs ± 12.5 µs per loop (mean ± std. dev. of 7 runs, 1,000 loops each)

df_loc = pd.DataFrame([[0, 0, 0], [1, 1, 1], [2, 2, 2]])
for i in range(3, 1003):
    df_loc.loc[i] = [i] * 3

df = pd.DataFrame([[0, 0, 0], [1, 1, 1], [2, 2, 2]])
l_data = []
l_label = []

for i in range(3, 1003):
    l_data.append([i] * 3)
    l_label.append(i)

df_concat = pd.concat([df, pd.DataFrame(l_data, index=l_label, columns=df.columns)])

print(df_loc.equals(df_concat))
# True

%%timeit
df_index = pd.DataFrame([[0, 0, 0], [1, 1, 1], [2, 2, 2]])

for i in range(3, 1003):
    df_index[i] = [0, 1, 2]
# 31.2 ms ± 578 µs per loop (mean ± std. dev. of 7 runs, 10 loops each)

%%timeit
df = pd.DataFrame([[0, 0, 0], [1, 1, 1], [2, 2, 2]])
l_data = []
l_label = []

for i in range(3, 1003):
    l_data.append([0, 1, 2])
    l_label.append(i)

df_concat = pd.concat([df, pd.DataFrame(zip(*l_data), index=df.index, columns=l_label)], axis=1)
# 3.56 ms ± 54.7 µs per loop (mean ± std. dev. of 7 runs, 100 loops each)

%%timeit
df = pd.DataFrame([[0, 0, 0], [1, 1, 1], [2, 2, 2]])
d = {}

for i in range(3, 1003):
    d[i] = [0, 1, 2]

df_concat_d = pd.concat([df, pd.DataFrame(d, index=df.index)], axis=1)
# 4.16 ms ± 126 µs per loop (mean ± std. dev. of 7 runs, 100 loops each)

df_index = pd.DataFrame([[0, 0, 0], [1, 1, 1], [2, 2, 2]])

for i in range(3, 1003):
    df_index[i] = [0, 1, 2]

df = pd.DataFrame([[0, 0, 0], [1, 1, 1], [2, 2, 2]])
l_data = []
l_label = []

for i in range(3, 1003):
    l_data.append([0, 1, 2])
    l_label.append(i)

df_concat = pd.concat([df, pd.DataFrame(zip(*l_data), index=df.index, columns=l_label)], axis=1)

df = pd.DataFrame([[0, 0, 0], [1, 1, 1], [2, 2, 2]])
d = {}

for i in range(3, 1003):
    d[i] = [0, 1, 2]

df_concat_d = pd.concat([df, pd.DataFrame(d, index=df.index)], axis=1)

print(df_index.equals(df_concat))
# True

print(df_index.equals(df_concat_d))
# True

import numpy as np

l_v = np.zeros((1000, 3)).tolist()

%%timeit
pd.DataFrame(l_v)
# 93.1 µs ± 2.07 µs per loop (mean ± std. dev. of 7 runs, 10,000 loops each)

l_h = np.zeros((3, 1000)).tolist()

%%timeit
pd.DataFrame(l_h)
# 3.12 ms ± 4.19 µs per loop (mean ± std. dev. of 7 runs, 100 loops each)
