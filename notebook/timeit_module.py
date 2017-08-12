import timeit

def test(n):
    return sum(range(n))

n = 10000
loop = 1000

result = timeit.timeit('test(n)', globals=globals(), number=loop)
print(result / loop)
# 0.0002666301020071842

result = timeit.timeit(lambda: test(n), number=loop)
print(result / loop)
# 0.00027574066299712287

print(timeit.timeit(lambda: test(n), number=1))
print(timeit.timeit(lambda: test(n), number=10))
print(timeit.timeit(lambda: test(n), number=100))
# 0.0003999490290880203
# 0.0038685189792886376
# 0.03517670702422038

# magic command
# It works only on Jupyter / IPython.
get_ipython().magic('timeit test(n)')
# 243 µs ± 6.53 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)

get_ipython().magic('timeit -r 3 -n 10000 test(n)')
# 237 µs ± 6.44 µs per loop (mean ± std. dev. of 3 runs, 10000 loops each)

get_ipython().run_cell_magic('timeit', '-r 3 -n 10000', 'import numpy as np\na = np.arange(n)\nnp.sum(a)')
# 19.7 µs ± 9.57 µs per loop (mean ± std. dev. of 3 runs, 10000 loops each)
