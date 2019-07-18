pwd
# /Users/mbp/Documents/my-project/python-snippets/notebook/dir_import_test

python3 dir/main_sys_path_append.py
# -- mod1.func is called
# -- dir_for_mod.mod2.func is called

cd dir

pwd
# /Users/mbp/Documents/my-project/python-snippets/notebook/dir_import_test/dir

python3 main_sys_path_append.py
# -- mod1.func is called
# -- dir_for_mod.mod2.func is called

cd ../..

pwd
# /Users/mbp/Documents/my-project/python-snippets/notebook

python3 dir_import_test/dir/main_sys_path_append.py
# -- mod1.func is called
# -- dir_for_mod.mod2.func is called
