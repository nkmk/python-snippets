import unicodedata

s = '１２３ａｂｃｱｲｳｴｵ'
print(unicodedata.is_normalized('NFKC', s))
# False

%%timeit
unicodedata.is_normalized('NFKC', s)
# 42.5 ns ± 0.0538 ns per loop (mean ± std. dev. of 7 runs, 10,000,000 loops each)

%%timeit
unicodedata.normalize('NFKC', s)
# 988 ns ± 5.71 ns per loop (mean ± std. dev. of 7 runs, 1,000,000 loops each)

s = '123abcアイウエオ'
print(unicodedata.is_normalized('NFKC', s))
# True

%%timeit
unicodedata.is_normalized('NFKC', s)
# 54.3 ns ± 0.0637 ns per loop (mean ± std. dev. of 7 runs, 10,000,000 loops each)

%%timeit
unicodedata.normalize('NFKC', s)
# 51 ns ± 0.163 ns per loop (mean ± std. dev. of 7 runs, 10,000,000 loops each)

s = '123abcアイウエオ' * 1000
print(unicodedata.is_normalized('NFKC', s))
# True

%%timeit
unicodedata.is_normalized('NFKC', s)
# 13 µs ± 7.05 ns per loop (mean ± std. dev. of 7 runs, 100,000 loops each)

%%timeit
unicodedata.normalize('NFKC', s)
# 11.8 µs ± 117 ns per loop (mean ± std. dev. of 7 runs, 100,000 loops each)

s = '123abcアイウエオ' * 1000 + '１２３'
print(unicodedata.is_normalized('NFKC', s))
# False

%%timeit
unicodedata.is_normalized('NFKC', s)
# 13 µs ± 27.4 ns per loop (mean ± std. dev. of 7 runs, 100,000 loops each)

%%timeit
unicodedata.normalize('NFKC', s)
# 879 µs ± 3.31 µs per loop (mean ± std. dev. of 7 runs, 1,000 loops each)

s = '１２３' + '123abcアイウエオ' * 1000
print(unicodedata.is_normalized('NFKC', s))
# False

%%timeit
unicodedata.is_normalized('NFKC', s)
# 42.7 ns ± 0.339 ns per loop (mean ± std. dev. of 7 runs, 10,000,000 loops each)

%%timeit
unicodedata.normalize('NFKC', s)
# 866 µs ± 1.01 µs per loop (mean ± std. dev. of 7 runs, 1,000 loops each)
