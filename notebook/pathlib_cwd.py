from pathlib import Path

p = Path.cwd()
print(p)
# /Users/mbp/Documents/my-project/python-snippets/notebook

print(type(p))
# <class 'pathlib.PosixPath'>

print(p.cwd())
# /Users/mbp/Documents/my-project/python-snippets/notebook

import os

os.chdir(p.parent)

print(Path.cwd())
# /Users/mbp/Documents/my-project/python-snippets

os.chdir(p / 'data')

print(Path.cwd())
# /Users/mbp/Documents/my-project/python-snippets/notebook/data
