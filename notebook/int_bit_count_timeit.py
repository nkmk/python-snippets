def bit_count(self):
    return bin(self).count("1")

i = 255

%%timeit
i.bit_count()
# 22 ns ± 0.072 ns per loop (mean ± std. dev. of 7 runs, 10,000,000 loops each)

%%timeit
bit_count(i)
# 121 ns ± 0.275 ns per loop (mean ± std. dev. of 7 runs, 10,000,000 loops each)
