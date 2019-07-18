pwd
# /Users/mbp/Documents/my-project/python-snippets/notebook/dir_import_test

python3 dir/main_absolute.py
# -- mod1.func is called
# -- dir_for_mod.mod2.func is called

cd dir

pwd
# /Users/mbp/Documents/my-project/python-snippets/notebook/dir_import_test/dir

python3 main_absolute.py
# Traceback (most recent call last):
#   File "main_absolute.py", line 1, in <module>
#     import mod1
# ModuleNotFoundError: No module named 'mod1'
