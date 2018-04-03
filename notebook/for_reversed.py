l = ['Alice', 'Bob', 'Charlie']

for name in reversed(l):
    print(name)
# Charlie
# Bob
# Alice

for i in reversed(range(3)):
    print(i)
# 2
# 1
# 0

for i in range(2, -1, -1):
    print(i)
# 2
# 1
# 0

# for i, name in reversed(enumerate(l)):
#     print(i, name)
# TypeError: 'enumerate' object is not reversible

for i, name in reversed(list(enumerate(l))):
    print(i, name)
# 2 Charlie
# 1 Bob
# 0 Alice

for i, name in enumerate(reversed(l)):
    print(i, name)
# 0 Charlie
# 1 Bob
# 2 Alice

l2 = [24, 50, 18]

# for name, age in reversed(zip(l, l2)):
#     print(name, age)
# TypeError: 'zip' object is not reversible

for name, age in reversed(list(zip(l, l2))):
    print(name, age)
# Charlie 18
# Bob 50
# Alice 24
