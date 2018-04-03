l = ['Alice', 'Bob', 'Charlie']

for name in l:
    print(name)
# Alice
# Bob
# Charlie

for name in l:
    if name == 'Bob':
        print('!!BREAK!!')
        break
    print(name)
# Alice
# !!BREAK!!

for name in l:
    print(name)
else:
    print('!!FINISH!!')
# Alice
# Bob
# Charlie
# !!FINISH!!

for name in l:
    if name == 'Bob':
        print('!!BREAK!!')
        break
    print(name)
else:
    print('!!FINISH!!')
# Alice
# !!BREAK!!
