import os

print(os.getcwd())
# /Users/mbp/Documents/my-project/python-snippets/notebook

!pwd
# /Users/mbp/Documents/my-project/python-snippets/notebook

%pwd
# '/Users/mbp/Documents/my-project/python-snippets/notebook'

!cd data

print(os.getcwd())
# /Users/mbp/Documents/my-project/python-snippets/notebook

%cd data
# /Users/mbp/Documents/my-project/python-snippets/notebook/data

print(os.getcwd())
# /Users/mbp/Documents/my-project/python-snippets/notebook/data

!pwd
# /Users/mbp/Documents/my-project/python-snippets/notebook/data

%pwd
# '/Users/mbp/Documents/my-project/python-snippets/notebook/data'

cd ..
# /Users/mbp/Documents/my-project/python-snippets/notebook

print(os.getcwd())
# /Users/mbp/Documents/my-project/python-snippets/notebook

os.chdir('data')

print(os.getcwd())
# /Users/mbp/Documents/my-project/python-snippets/notebook/data
