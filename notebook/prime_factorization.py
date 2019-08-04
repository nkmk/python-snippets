import collections

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

print(prime_factorize(1))
# []

print(prime_factorize(36))
# [2, 2, 3, 3]

print(prime_factorize(840))
# [2, 2, 2, 3, 5, 7]

c = collections.Counter(prime_factorize(840))
print(c)
# Counter({2: 3, 3: 1, 5: 1, 7: 1})

print(c.keys())
# dict_keys([2, 3, 5, 7])

print(c.values())
# dict_values([3, 1, 1, 1])

print(c.items())
# dict_items([(2, 3), (3, 1), (5, 1), (7, 1)])

print(list(c.keys()))
# [2, 3, 5, 7]
