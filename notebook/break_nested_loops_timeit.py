import itertools

n = 100
l1 = range(n)
l2 = range(n)
l3 = range(n)

x = n - 1

%%timeit
for i in l1:
    for j in l2:
        for k in l3:
            if i == x and j == x and k == x:
                break
        else:
            continue
        break
    else:
        continue
    break
# 43 ms ± 1.33 ms per loop (mean ± std. dev. of 7 runs, 10 loops each)

%%timeit
flag = False
for i in l1:
    for j in l2:
        for k in l3:
            if i == x and j == x and k == x:
                flag = True
                break
        if flag:
            break
    if flag:
        break
# 45.2 ms ± 3.42 ms per loop (mean ± std. dev. of 7 runs, 10 loops each)

%%timeit
for i, j, k in itertools.product(l1, l2, l3):
    if i == x and j == x and k == x:
        break
# 55.8 ms ± 458 µs per loop (mean ± std. dev. of 7 runs, 10 loops each)
