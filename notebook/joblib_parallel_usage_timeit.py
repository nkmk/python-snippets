import joblib

def func(i):
    return i

%%timeit
for i in range(100):
    func(i)
# 9.87 µs ± 251 ns per loop (mean ± std. dev. of 7 runs, 100000 loops each)

%%timeit
joblib.Parallel(n_jobs=-1)(joblib.delayed(func)(i) for i in range(100))
# 21.6 ms ± 2.12 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)

import time

def func_sleep(i):
    time.sleep(0.1)
    return i

%%timeit
for i in range(8):
    func_sleep(i)
# 824 ms ± 5.63 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)

%%timeit
joblib.Parallel(n_jobs=-1)(joblib.delayed(func_sleep)(i) for i in range(8))
# 221 ms ± 5.06 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)

%%timeit
joblib.Parallel(n_jobs=2)(joblib.delayed(func_sleep)(i) for i in range(8))
# 423 ms ± 7.93 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)
