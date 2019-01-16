import csv

with open('data/temp/sample_writer_row.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow([0, 1, 2])
    writer.writerow(['a', 'b', 'c'])

with open('data/temp/sample_writer_row.csv') as f:
    print(f.read())
# 0,1,2
# a,b,c
# 

l = [[11, 12, 13, 14], [21, 22, 23, 24], [31, 32, 33, 34]]
print(l)
# [[11, 12, 13, 14], [21, 22, 23, 24], [31, 32, 33, 34]]

with open('data/temp/sample_writer.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerows(l)

with open('data/temp/sample_writer.csv') as f:
    print(f.read())
# 11,12,13,14
# 21,22,23,24
# 31,32,33,34
# 

with open('data/temp/sample_writer_row.csv') as f:
    print(f.read())
# 0,1,2
# a,b,c
# 

with open('data/temp/sample_writer_row.csv', 'a') as f:
    writer = csv.writer(f)
    writer.writerow(['X', 'Y', 'Z'])

with open('data/temp/sample_writer_row.csv') as f:
    print(f.read())
# 0,1,2
# a,b,c
# X,Y,Z
# 

with open('data/temp/sample_writer.tsv', 'w') as f:
    writer = csv.writer(f, delimiter='\t')
    writer.writerows(l)

with open('data/temp/sample_writer.tsv') as f:
    print(f.read())
# 11	12	13	14
# 21	22	23	24
# 31	32	33	34
# 

l = [[0, 1, 2], ['a,b,c', 'x', 'y']]

with open('data/temp/sample_writer_quote.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerows(l)

with open('data/temp/sample_writer_quote.csv') as f:
    print(f.read())
# 0,1,2
# "a,b,c",x,y
# 

with open('data/temp/sample_writer_quote_all.csv', 'w') as f:
    writer = csv.writer(f, quoting=csv.QUOTE_ALL)
    writer.writerows(l)

with open('data/temp/sample_writer_quote_all.csv') as f:
    print(f.read())
# "0","1","2"
# "a,b,c","x","y"
# 

with open('data/temp/sample_writer_quote_nonnumeric.csv', 'w') as f:
    writer = csv.writer(f, quoting=csv.QUOTE_NONNUMERIC)
    writer.writerows(l)

with open('data/temp/sample_writer_quote_nonnumeric.csv') as f:
    print(f.read())
# 0,1,2
# "a,b,c","x","y"
# 

with open('data/temp/sample_writer_quote_none.csv', 'w') as f:
    writer = csv.writer(f, quoting=csv.QUOTE_NONE, escapechar='\\')
    writer.writerows(l)

with open('data/temp/sample_writer_quote_none.csv') as f:
    print(f.read())
# 0,1,2
# a\,b\,c,x,y
# 

with open('data/temp/sample_writer_quote_char.csv', 'w') as f:
    writer = csv.writer(f, quotechar="'")
    writer.writerows(l)

with open('data/temp/sample_writer_quote_char.csv') as f:
    print(f.read())
# 0,1,2
# 'a,b,c',x,y
# 

l = [[0, 1, 2], ['a\nb', 'x', 'y']]

with open('data/temp/sample_writer_linebreak.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(l)

with open('data/temp/sample_writer_linebreak.csv') as f:
    print(f.read())
# 0,1,2
# "a
# b",x,y
# 

l = [[11, 12, 13, 14], [21, 22, 23, 24], [31, 32, 33, 34]]
print(l)
# [[11, 12, 13, 14], [21, 22, 23, 24], [31, 32, 33, 34]]

header = ['', 'a', 'b', 'c', 'd']
index = ['ONE', 'TWO', 'THREE']

with open('data/temp/sample_writer_header_index.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    for i, row in zip(index, l):
        writer.writerow([i] + row)

with open('data/temp/sample_writer_header_index.csv') as f:
    print(f.read())
# ,a,b,c,d
# ONE,11,12,13,14
# TWO,21,22,23,24
# THREE,31,32,33,34
# 
