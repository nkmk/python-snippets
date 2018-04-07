import pandas as pd

df = pd.read_csv('data/src/sample_pandas_normal.csv')
s = df['state']

%timeit s.map({'NY': 'NewYork', 'CA': 'California', 'TX': 'Texas'})
# 345 µs ± 14 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)

%timeit s.replace({'NY': 'NewYork', 'CA': 'California', 'TX': 'Texas'})
# 519 µs ± 15.9 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)

s_copy = s.copy()
%timeit s_copy.update(s_copy.map({'NY': 'NewYork'}))
# 643 µs ± 21.4 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)

s_copy = s.copy()
%timeit s_copy.replace({'NY': 'NewYork'}, inplace=True)
# 230 µs ± 10 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)

s_copy = s.copy()
%timeit s_copy.update(s_copy.map({'NY': 'NewYork', 'CA': 'California', 'TX': 'Texas'}))
# 627 µs ± 10.9 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)

s_copy = s.copy()
%timeit s_copy.replace({'NY': 'NewYork', 'CA': 'California', 'TX': 'Texas'}, inplace=True)
# 441 µs ± 22.1 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)

%timeit s.map({'NY': 'NewYork'})
# 335 µs ± 7.55 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)

%timeit s.replace({'NY': 'NewYork'})
# 261 µs ± 6.57 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)

df = pd.read_csv('data/src/titanic_train.csv')
s = df['Sex']

%timeit s.map({'male': 0, 'female': 1})
# 422 µs ± 30.6 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)

%timeit s.replace({'male': 0, 'female': 1})
# 634 µs ± 13.4 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)
