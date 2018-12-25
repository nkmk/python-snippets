import re

s = 'file5.txt'

print(re.search(r'\d+', s).group())
# 5

print(type(re.search(r'\d+', s).group()))
# <class 'str'>

print(type(int(re.search(r'\d+', s).group())))
# <class 'int'>

l = ['file10.txt', 'file1.txt', 'file5.txt']

print(sorted(l))
# ['file1.txt', 'file10.txt', 'file5.txt']

print(sorted(l, key=lambda s: int(re.search(r'\d+', s).group())))
# ['file1.txt', 'file5.txt', 'file10.txt']

p = re.compile(r'\d+')
print(sorted(l, key=lambda s: int(p.search(s).group())))
# ['file1.txt', 'file5.txt', 'file10.txt']

s = '100file5.txt'

print(re.search(r'\d+', s).group())
# 100

print(re.findall(r'\d+', s))
# ['100', '5']

print(re.findall(r'\d+', s)[1])
# 5

print(re.search(r'file(\d+)', s).groups())
# ('5',)

print(re.search(r'file(\d+)', s).groups()[0])
# 5

print(re.search(r'(\d+)\.', s).groups()[0])
# 5

l = ['100file10.txt', '100file1.txt', '100file5.txt']

print(sorted(l, key=lambda s: int(re.findall(r'\d+', s)[1])))
# ['100file1.txt', '100file5.txt', '100file10.txt']

print(sorted(l, key=lambda s: int(re.search(r'file(\d+)', s).groups()[0])))
# ['100file1.txt', '100file5.txt', '100file10.txt']

print(sorted(l, key=lambda s: int(re.search(r'(\d+)\.', s).groups()[0])))
# ['100file1.txt', '100file5.txt', '100file10.txt']

p = re.compile(r'file(\d+)')
print(sorted(l, key=lambda s: int(p.search(s).groups()[0])))
# ['100file1.txt', '100file5.txt', '100file10.txt']

l = ['file10.txt', 'file1.txt', 'file5.txt', 'file.txt']

# print(sorted(l, key=lambda s:int(re.search(r'\d+', s).group())))
# AttributeError: 'NoneType' object has no attribute 'group'

def extract_num(s, p, ret=0):
    search = p.search(s)
    if search:
        return int(search.groups()[0])
    else:
        return ret

p = re.compile(r'(\d+)')

print(extract_num('file10.txt', p))
# 10

print(extract_num('file.txt', p))
# 0

print(extract_num('file.txt', p, 100))
# 100

print(sorted(l, key=lambda s: extract_num(s, p)))
# ['file.txt', 'file1.txt', 'file5.txt', 'file10.txt']

print(sorted(l, key=lambda s: extract_num(s, p, float('inf'))))
# ['file1.txt', 'file5.txt', 'file10.txt', 'file.txt']

l = ['100file10.txt', '100file1.txt', '100file5.txt', '100file.txt']

p = re.compile(r'file(\d+)')
print(sorted(l, key=lambda s: extract_num(s, p)))
# ['100file.txt', '100file1.txt', '100file5.txt', '100file10.txt']

print(sorted(l, key=lambda s: extract_num(s, p, float('inf'))))
# ['100file1.txt', '100file5.txt', '100file10.txt', '100file.txt']
