import csv

d1 = {'a': 1, 'b': 2, 'c': 3}
d2 = {'a': 10, 'c': 30}

with open('data/temp/sample_dictwriter.csv', 'w') as f:
    writer = csv.DictWriter(f, ['a', 'b', 'c'])
    writer.writeheader()
    writer.writerow(d1)
    writer.writerow(d2)

with open('data/temp/sample_dictwriter.csv') as f:
    print(f.read())
# a,b,c
# 1,2,3
# 10,,30
# 

with open('data/temp/sample_dictwriter_list.csv', 'w') as f:
    writer = csv.DictWriter(f, ['a', 'b', 'c'])
    writer.writeheader()
    writer.writerows([d1, d2])

with open('data/temp/sample_dictwriter_list.csv') as f:
    print(f.read())
# a,b,c
# 1,2,3
# 10,,30
# 

with open('data/temp/sample_dictwriter_ignore.csv', 'w') as f:
    writer = csv.DictWriter(f, ['a', 'c'], extrasaction='ignore')
    writer.writeheader()
    writer.writerows([d1, d2])

with open('data/temp/sample_dictwriter_ignore.csv') as f:
    print(f.read())
# a,c
# 1,3
# 10,30
# 
