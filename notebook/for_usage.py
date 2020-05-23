l = ['Alice', 'Bob', 'Charlie']

for name in l:
    print(name)
# Alice
# Bob
# Charlie

l = ['Alice', 'Bob', 'Charlie']

for name in l:
    if name == 'Bob':
        print('!!BREAK!!')
        break
    print(name)
# Alice
# !!BREAK!!

l = ['Alice', 'Bob', 'Charlie']

for name in l:
    if name == 'Bob':
        print('!!SKIP!!')
        continue
    print(name)
# Alice
# !!SKIP!!
# Charlie

l = ['Alice', 'Bob', 'Charlie']

for name in l:
    print(name)
else:
    print('!!FINISH!!')
# Alice
# Bob
# Charlie
# !!FINISH!!

l = ['Alice', 'Bob', 'Charlie']

for name in l:
    if name == 'Bob':
        print('!!BREAK!!')
        break
    print(name)
else:
    print('!!FINISH!!')
# Alice
# !!BREAK!!

l = ['Alice', 'Bob', 'Charlie']

for name in l:
    if name == 'Bob':
        print('!!SKIP!!')
        continue
    print(name)
else:
    print('!!FINISH!!')
# Alice
# !!SKIP!!
# Charlie
# !!FINISH!!

l = ['A', 'B', 'C', 'D', 'E', 'F', 'G']

for c in l[2:5]:
    print(c)
# C
# D
# E

for c in l[::2]:
    print(c)
# A
# C
# E
# G

for c in l[1::2]:
    print(c)
# B
# D
# F
