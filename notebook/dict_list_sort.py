import pprint

l = [{'Name': 'Alice', 'Age': 40, 'Point': 80}, 
     {'Name': 'Bob', 'Age': 20},
     {'Name': 'Charlie', 'Age': 30, 'Point': 70}]

pprint.pprint(l)
# [{'Age': 40, 'Name': 'Alice', 'Point': 80},
#  {'Age': 20, 'Name': 'Bob'},
#  {'Age': 30, 'Name': 'Charlie', 'Point': 70}]

# l.sort()
# TypeError: '<' not supported between instances of 'dict' and 'dict'

l.sort(key=lambda x: x['Age'])

pprint.pprint(l)
# [{'Age': 20, 'Name': 'Bob'},
#  {'Age': 30, 'Name': 'Charlie', 'Point': 70},
#  {'Age': 40, 'Name': 'Alice', 'Point': 80}]

l.sort(key=lambda x: x['Name'])

pprint.pprint(l)
# [{'Age': 40, 'Name': 'Alice', 'Point': 80},
#  {'Age': 20, 'Name': 'Bob'},
#  {'Age': 30, 'Name': 'Charlie', 'Point': 70}]

# l.sort(key=lambda x: x['Point'])
# KeyError: 'Point'

# l.sort(key=lambda x: x.get('Point'))
# TypeError: '<' not supported between instances of 'int' and 'NoneType'

l.sort(key=lambda x: x.get('Point', 0))

pprint.pprint(l)
# [{'Age': 20, 'Name': 'Bob'},
#  {'Age': 30, 'Name': 'Charlie', 'Point': 70},
#  {'Age': 40, 'Name': 'Alice', 'Point': 80}]

l.sort(key=lambda x: x.get('Point', 100))

pprint.pprint(l)
# [{'Age': 30, 'Name': 'Charlie', 'Point': 70},
#  {'Age': 40, 'Name': 'Alice', 'Point': 80},
#  {'Age': 20, 'Name': 'Bob'}]

l.sort(key=lambda x: x['Name'], reverse=True)

pprint.pprint(l)
# [{'Age': 30, 'Name': 'Charlie', 'Point': 70},
#  {'Age': 20, 'Name': 'Bob'},
#  {'Age': 40, 'Name': 'Alice', 'Point': 80}]

l_sorted = sorted(l, key=lambda x: x['Age'], reverse=True)

pprint.pprint(l_sorted)
# [{'Age': 40, 'Name': 'Alice', 'Point': 80},
#  {'Age': 30, 'Name': 'Charlie', 'Point': 70},
#  {'Age': 20, 'Name': 'Bob'}]
