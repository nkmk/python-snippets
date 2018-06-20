a = 1  # comment

a = 1  # comment # b = 2

# a = 1

a = 1
# b = 2
# c = 3
# d = 4
e = 5

# No:
a = 1 # comment

# Yes:
a = 1  # comment

a = 1      # comment
xyz = 100  # comment

# No:
a = 1  #comment
a = 1  #  comment

# Yes:
a = 1  # comment

# No:
#comment

# Yes:
# comment
#     indented comment

# No:
## comment

# Yes:
# comment

def test(a, b):
    '''docstring
    description
    '''
    print(a)
    print(b)

a = 1
'''
b = 2
c = 3
d = 4
'''
e = 5

def test(a, b):
    print(a)
    '''
    comment line1
    comment line2
    comment line3
    '''
    print(b)

def test(a, b):
    print(a)
'''
comment line1
comment line2
comment line3
'''
    print(b)

# IndentationError: unexpected indent

def test(a, b):
    print(a)
    # comment line1
    # comment line2
    # comment line3
    print(b)

def test(a, b):
    print(a)
# comment line1
# comment line2
# comment line3
    print(b)
