import csv

with open('data/src/sample.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
# ['11', '12', '13', '14']
# ['21', '22', '23', '24']
# ['31', '32', '33', '34']

with open('data/src/sample_space.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
# ['11', ' 12', ' 13', ' 14']
# ['21', ' 22', ' 23', ' 24']
# ['31', ' 32', ' 33', ' 34']

with open('data/src/sample_space.csv', 'r') as f:
    reader = csv.reader(f, skipinitialspace=True)
    for row in reader:
        print(row)
# ['11', '12', '13', '14']
# ['21', '22', '23', '24']
# ['31', '32', '33', '34']

with open('data/src/sample_double_quotation.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
# ['one,one', ' "two', 'two"', ' "three', 'three"']

with open('data/src/sample_double_quotation.csv', 'r') as f:
    reader = csv.reader(f, skipinitialspace=True)
    for row in reader:
        print(row)
# ['one,one', 'two,two', 'three,three']
