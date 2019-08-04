def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a

print(prime_factorize(67280421310721))
# [67280421310721]

%%timeit
prime_factorize(67280421310721)
# 790 ms ± 14 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)

print(prime_factorize(67280421310722))
# [2, 3, 3, 109, 18401, 1863581]

%%timeit
prime_factorize(67280421310722)
# 1.74 ms ± 4.55 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)

print(prime_factorize(2147483647))
# [2147483647]

%%timeit
prime_factorize(2147483647)
# 4.53 ms ± 131 µs per loop (mean ± std. dev. of 7 runs, 100 loops each)
