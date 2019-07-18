pwd
# /Users/mbp/Documents/my-project/python-snippets/notebook/dir_import_test

python3 dir/main_relative.py
# Traceback (most recent call last):
#   File "dir/main_relative.py", line 1, in <module>
#     from .. import mod1
# ValueError: attempted relative import beyond top-level package

cd ..

pwd
# /Users/mbp/Documents/my-project/python-snippets/notebook

python3 -m dir_import_test.dir.main_relative
# -- mod1.func is called
# -- dir_for_mod.mod2.func is called
