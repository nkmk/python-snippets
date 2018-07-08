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
