import os

path = os.getcwd()

print(path)
# /Users/mbp/Documents/my-project/python-snippets/notebook

print(type(path))
# <class 'str'>

os.chdir('../')

print(os.getcwd())
# /Users/mbp/Documents/my-project/python-snippets
