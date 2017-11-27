names = ['Alice', 'Bob', 'Charlie']
ages = [24, 50, 18]

for i, (name, age) in enumerate(zip(names, ages)):
    print(i, name, age)
# 0 Alice 24
# 1 Bob 50
# 2 Charlie 18

for i, t in enumerate(zip(names, ages)):
    print(i, t)
# 0 ('Alice', 24)
# 1 ('Bob', 50)
# 2 ('Charlie', 18)

for i, t in enumerate(zip(names, ages)):
    print(i, t[0], t[1])
# 0 Alice 24
# 1 Bob 50
# 2 Charlie 18
