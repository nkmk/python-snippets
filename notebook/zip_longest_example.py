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

points = [100, 85]

for name, age, point in zip_longest(names, ages, points, fillvalue=20):
    print(name, age, point)
# Alice 24 100
# Bob 50 85
# Charlie 18 20
# Dave 20 20

fill_name = 'XXX'
fill_age = 20
fill_point = 50

len_names = len(names)
len_ages = len(ages)
len_points = len(points)

max_len = max(len_names, len_ages, len_points)

names = names + [fill_name] * (max_len - len_names)
ages = ages + [fill_age] * (max_len - len_ages)
points = points + [fill_point] * (max_len - len_points)

print(names)
print(ages)
print(points)
# ['Alice', 'Bob', 'Charlie', 'Dave']
# [24, 50, 18, 20]
# [100, 85, 50, 50]

for name, age, point in zip(names, ages, points):
    print(name, age, point)
# Alice 24 100
# Bob 50 85
# Charlie 18 50
# Dave 20 50

def my_zip_longest(iterables, fillvalues):
    max_len = max(len(i) for i in iterables)
    return zip(*[list(i) + [v] * (max_len - len(i)) for i, v in zip(iterables, fillvalues)])

for name, age, point in my_zip_longest((names, ages, points), ('XXX', 20, 50)):
    print(name, age, point)
# Alice 24 100
# Bob 50 85
# Charlie 18 50
# Dave 20 50
