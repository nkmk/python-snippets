pwd
# /Users/mbp/Documents/my-project/python-snippets/notebook/my_package

python3 main.py
# Traceback (most recent call last):
#   File "main.py", line 1, in <module>
#     from sub_package2 import sub_mod2
#   File "/Users/mbp/Documents/my-project/python-snippets/notebook/my_package/sub_package2/sub_mod2.py", line 1, in <module>
#     from .. import mod1
# ValueError: attempted relative import beyond top-level package
