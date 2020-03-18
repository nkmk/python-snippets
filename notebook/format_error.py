l = [0, 1]
print(type(l))
# <class 'list'>

# print('{:*^16}'.format(l))
# TypeError: unsupported format string passed to list.__format__

print(type(str(l)))
# <class 'str'>

print('{:*^16}'.format(str(l)))
# *****[0, 1]*****
