pwd
# /Users/mbp/Documents/my-project/python-snippets/notebook

python3 dir/main_relative.py
# Traceback (most recent call last):
#   File "dir/main_relative.py", line 1, in <module>
#     from .my_package import mod1
# ModuleNotFoundError: No module named '__main__.my_package'; '__main__' is not a package

pwd
# /Users/mbp/Documents/my-project/python-snippets/notebook

python3 dir/main_absolute.py
# mod1, func

cd dir

python3 main_absolute.py
# Traceback (most recent call last):
#   File "main_absolute.py", line 1, in <module>
#     from my_package import mod1
# ModuleNotFoundError: No module named 'my_package'

pwd
# /Users/mbp/Documents/my-project/python-snippets/notebook/dir

python3 main_sys_path_append.py
# mod1, func

cd ..

python3 dir/main_sys_path_append.py
# mod1, func

cd ..

python3 notebook/dir/main_sys_path_append.py
# mod1, func
