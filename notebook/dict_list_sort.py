import pprint

l = [{'Name': 'Alice', 'Age': 40, 'Point': 80},
     {'Name': 'Bob', 'Age': 20},
     {'Name': 'Charlie', 'Age': 30, 'Point': 70}]
pprint.pprint(l)
# [{'Age': 40, 'Name': 'Alice', 'Point': 80},
#  {'Age': 20, 'Name': 'Bob'},
#  {'Age': 30, 'Name': 'Charlie', 'Point': 70}]

# sorted(l)
# TypeError: '<' not supported between instances of 'dict' and 'dict'

pprint.pprint(sorted(l, key=lambda x: x['Age']))
# [{'Age': 20, 'Name': 'Bob'},
#  {'Age': 30, 'Name': 'Charlie', 'Point': 70},
#  {'Age': 40, 'Name': 'Alice', 'Point': 80}]

pprint.pprint(sorted(l, key=lambda x: x['Name']))
# [{'Age': 40, 'Name': 'Alice', 'Point': 80},
#  {'Age': 20, 'Name': 'Bob'},
#  {'Age': 30, 'Name': 'Charlie', 'Point': 70}]

pprint.pprint(sorted(l, key=lambda x: x['Age'], reverse=True))
# [{'Age': 40, 'Name': 'Alice', 'Point': 80},
#  {'Age': 30, 'Name': 'Charlie', 'Point': 70},
#  {'Age': 20, 'Name': 'Bob'}]

# sorted(l, key=lambda x: x['Point'])
# KeyError: 'Point'

# sorted(l, key=lambda x: x.get('Point'))
# TypeError: '<' not supported between instances of 'int' and 'NoneType'

pprint.pprint(sorted(l, key=lambda x: x.get('Point', 75)))
# [{'Age': 30, 'Name': 'Charlie', 'Point': 70},
#  {'Age': 20, 'Name': 'Bob'},
#  {'Age': 40, 'Name': 'Alice', 'Point': 80}]

pprint.pprint(sorted(l, key=lambda x: x.get('Point', float('inf'))))
# [{'Age': 30, 'Name': 'Charlie', 'Point': 70},
#  {'Age': 40, 'Name': 'Alice', 'Point': 80},
#  {'Age': 20, 'Name': 'Bob'}]

pprint.pprint(sorted(l, key=lambda x: x.get('Point', -float('inf'))))
# [{'Age': 20, 'Name': 'Bob'},
#  {'Age': 30, 'Name': 'Charlie', 'Point': 70},
#  {'Age': 40, 'Name': 'Alice', 'Point': 80}]

import operator

pprint.pprint(sorted(l, key=operator.itemgetter('Age')))
# [{'Age': 20, 'Name': 'Bob'},
#  {'Age': 30, 'Name': 'Charlie', 'Point': 70},
#  {'Age': 40, 'Name': 'Alice', 'Point': 80}]

pprint.pprint(sorted(l, key=operator.itemgetter('Name')))
# [{'Age': 40, 'Name': 'Alice', 'Point': 80},
#  {'Age': 20, 'Name': 'Bob'},
#  {'Age': 30, 'Name': 'Charlie', 'Point': 70}]

# sorted(l, key=operator.itemgetter('Point'))
# KeyError: 'Point'

l_dup = [{'Name': 'Alice', 'Age': 40, 'Point': 80, 'State': 'LA'},
         {'Name': 'Bob', 'Age': 20, 'State': 'NY'},
         {'Name': 'Charlie', 'Age': 30, 'Point': 70, 'State': 'LA'}]
pprint.pprint(l_dup)
# [{'Age': 40, 'Name': 'Alice', 'Point': 80, 'State': 'LA'},
#  {'Age': 20, 'Name': 'Bob', 'State': 'NY'},
#  {'Age': 30, 'Name': 'Charlie', 'Point': 70, 'State': 'LA'}]

pprint.pprint(sorted(l_dup, key=operator.itemgetter('State')))
# [{'Age': 40, 'Name': 'Alice', 'Point': 80, 'State': 'LA'},
#  {'Age': 30, 'Name': 'Charlie', 'Point': 70, 'State': 'LA'},
#  {'Age': 20, 'Name': 'Bob', 'State': 'NY'}]

pprint.pprint(sorted(l_dup, key=operator.itemgetter('State', 'Age')))
# [{'Age': 30, 'Name': 'Charlie', 'Point': 70, 'State': 'LA'},
#  {'Age': 40, 'Name': 'Alice', 'Point': 80, 'State': 'LA'},
#  {'Age': 20, 'Name': 'Bob', 'State': 'NY'}]

pprint.pprint(sorted(l_dup, key=operator.itemgetter('Age', 'State')))
# [{'Age': 20, 'Name': 'Bob', 'State': 'NY'},
#  {'Age': 30, 'Name': 'Charlie', 'Point': 70, 'State': 'LA'},
#  {'Age': 40, 'Name': 'Alice', 'Point': 80, 'State': 'LA'}]

pprint.pprint(sorted(l_dup, key=lambda x: (x['State'], x['Age'])))
# [{'Age': 30, 'Name': 'Charlie', 'Point': 70, 'State': 'LA'},
#  {'Age': 40, 'Name': 'Alice', 'Point': 80, 'State': 'LA'},
#  {'Age': 20, 'Name': 'Bob', 'State': 'NY'}]

# max(l)
# TypeError: '>' not supported between instances of 'dict' and 'dict'

print(max(l, key=lambda x: x['Age']))
# {'Name': 'Alice', 'Age': 40, 'Point': 80}

print(min(l, key=lambda x: x['Age']))
# {'Name': 'Bob', 'Age': 20}

print(max(l, key=lambda x: x['Age'])['Age'])
# 40

print(max(l, key=operator.itemgetter('Age')))
# {'Name': 'Alice', 'Age': 40, 'Point': 80}
