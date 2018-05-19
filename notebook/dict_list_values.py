l = [{'Name': 'Alice', 'Age': 40, 'Point': 80}, 
     {'Name': 'Bob', 'Age': 20},
     {'Name': 'Charlie', 'Age': 30, 'Point': 70}]

l_name = [d.get('Name') for d in l]
print(l_name)
# ['Alice', 'Bob', 'Charlie']

l_age = [d.get('Age') for d in l]
print(l_age)
# [40, 20, 30]

l_point = [d.get('Point') for d in l]
print(l_point)
# [80, None, 70]

l_name = [d['Name'] for d in l]
print(l_name)
# ['Alice', 'Bob', 'Charlie']

# l_point = [d['Point'] for d in l]
# KeyError: 'Point'

l_point_default = [d.get('Point', 0) for d in l]
print(l_point_default)
# [80, 0, 70]

l_point_ignore = [d.get('Point') for d in l if d.get('Point')]
print(l_point_ignore)
# [80, 70]
