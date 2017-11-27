names = ['Alice', 'Bob', 'Charlie']
ages = [24, 50, 18]

for name, age in zip(names, ages):
    print(name, age)
# Alice 24
# Bob 50
# Charlie 18

points = [100, 85, 90]

for name, age, point in zip(names, ages, points):
    print(name, age, point)
# Alice 24 100
# Bob 50 85
# Charlie 18 90

names = ['Alice', 'Bob', 'Charlie', 'Dave']
ages = [24, 50, 18]

for name, age in zip(names, ages):
    print(name, age)
# Alice 24
# Bob 50
# Charlie 18

names = ['Alice', 'Bob', 'Charlie']
ages = (24, 50, 18)

z = zip(names, ages)
print(z)
print(type(z))
# <zip object at 0x10b57b888>
# <class 'zip'>

l = list(zip(names, ages))
print(l)
print(type(l))
print(type(l[0]))
# [('Alice', 24), ('Bob', 50), ('Charlie', 18)]
# <class 'list'>
# <class 'tuple'>
