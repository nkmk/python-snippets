pwd
# /Users/mbp/Documents/my-project/python-snippets/notebook

python3 my_package/mod2.py
# Traceback (most recent call last):
#   File "my_package/mod2.py", line 1, in <module>
#     from . import mod1
# ImportError: cannot import name 'mod1' from '__main__' (my_package/mod2.py)

python3 -m my_package.mod2
# from mod2
# -- sub_mod1.func1 is called

cd my_package

pwd
# /Users/mbp/Documents/my-project/python-snippets/notebook/my_package

python3 -m mod2
# Traceback (most recent call last):
#   File "/usr/local/Cellar/python/3.7.4/Frameworks/Python.framework/Versions/3.7/lib/python3.7/runpy.py", line 193, in _run_module_as_main
#     "__main__", mod_spec)
#   File "/usr/local/Cellar/python/3.7.4/Frameworks/Python.framework/Versions/3.7/lib/python3.7/runpy.py", line 85, in _run_code
#     exec(code, run_globals)
#   File "/Users/mbp/Documents/my-project/python-snippets/notebook/my_package/mod2.py", line 1, in <module>
#     from . import mod1
# ImportError: attempted relative import with no known parent package
