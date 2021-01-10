import joblib

print(joblib.__version__)
# 1.0.0

def func(i):
    return i

result = joblib.Parallel(n_jobs=-1)(joblib.delayed(func)(i) for i in range(5))
print(result)
# [0, 1, 2, 3, 4]

result = joblib.Parallel(n_jobs=-1, verbose=1)(joblib.delayed(func)(i) for i in range(5))
# [Parallel(n_jobs=-1)]: Using backend LokyBackend with 4 concurrent workers.
# [Parallel(n_jobs=-1)]: Done   5 out of   5 | elapsed:    0.0s finished

result = joblib.Parallel(n_jobs=-1, verbose=11)(joblib.delayed(func)(i) for i in range(5))
# [Parallel(n_jobs=-1)]: Using backend LokyBackend with 4 concurrent workers.
# [Parallel(n_jobs=-1)]: Done   1 tasks      | elapsed:    0.0s
# [Parallel(n_jobs=-1)]: Batch computation too fast (0.0055s.) Setting batch_size=2.
# [Parallel(n_jobs=-1)]: Done   2 out of   5 | elapsed:    0.0s remaining:    0.0s
# [Parallel(n_jobs=-1)]: Done   3 out of   5 | elapsed:    0.0s remaining:    0.0s
# [Parallel(n_jobs=-1)]: Done   5 out of   5 | elapsed:    0.0s remaining:    0.0s
# [Parallel(n_jobs=-1)]: Done   5 out of   5 | elapsed:    0.0s finished

result = joblib.Parallel(n_jobs=2, verbose=1)(joblib.delayed(func)(i) for i in range(5))
# [Parallel(n_jobs=2)]: Using backend LokyBackend with 2 concurrent workers.
# [Parallel(n_jobs=2)]: Done   5 out of   5 | elapsed:    0.3s finished

result = joblib.Parallel(n_jobs=-2, verbose=1)(joblib.delayed(func)(i) for i in range(5))
# [Parallel(n_jobs=-2)]: Using backend LokyBackend with 3 concurrent workers.
# [Parallel(n_jobs=-2)]: Done   5 out of   5 | elapsed:    0.4s finished

def func_multi(i):
    return i, i**2, i**3

results = joblib.Parallel(n_jobs=-1)(joblib.delayed(func_multi)(i) for i in range(5))
print(results)
# [(0, 0, 0), (1, 1, 1), (2, 4, 8), (3, 9, 27), (4, 16, 64)]

a, b, c = zip(*results)
print(a)
# (0, 1, 2, 3, 4)

print(b)
# (0, 1, 4, 9, 16)

print(c)
# (0, 1, 8, 27, 64)

def func_multi2(i, j, k):
    return i, j, k

results = joblib.Parallel(n_jobs=-1)(
    joblib.delayed(func_multi2)(i, j, k) for i, j, k in zip(range(5), range(5, 10), range(10, 15))
)
print(results)
# [(0, 5, 10), (1, 6, 11), (2, 7, 12), (3, 8, 13), (4, 9, 14)]

def func_none():
    # do something
    pass

results = joblib.Parallel(n_jobs=-1)(joblib.delayed(func_none)() for i in range(5))
print(results)
# [None, None, None, None, None]

joblib.Parallel(n_jobs=-1)(joblib.delayed(func_none)() for i in range(5))
# [None, None, None, None, None]

_ = joblib.Parallel(n_jobs=-1)(joblib.delayed(func_none)() for i in range(5))
