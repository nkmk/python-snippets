from itertools import zip_longest

names = ['Alice', 'Bob', 'Charlie', 'Dave']
ages = [24, 50, 18]

for name, age in zip_longest(names, ages):
    print(name, age)
# Alice 24
# Bob 50
# Charlie 18
# Dave None

for name, age in zip_longest(names, ages, fillvalue=20):
    print(name, age)
# Alice 24
# Bob 50
# Charlie 18
# Dave 20
