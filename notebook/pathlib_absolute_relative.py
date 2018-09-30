import util_make_files

util_make_files.pathlib_basic()

import pathlib
import os

p = pathlib.Path('temp/file.txt')

print(p)
# temp/file.txt

print(type(p))
# <class 'pathlib.PosixPath'>

print(p.cwd())
# /Users/mbp/Documents/my-project/python-snippets/notebook

print(type(p.cwd()))
# <class 'pathlib.PosixPath'>

print(pathlib.Path.cwd())
# /Users/mbp/Documents/my-project/python-snippets/notebook

print(type(pathlib.Path.cwd()))
# <class 'pathlib.PosixPath'>

print(os.getcwd())
# /Users/mbp/Documents/my-project/python-snippets/notebook

print(type(os.getcwd()))
# <class 'str'>

print(p.resolve())
# /Users/mbp/Documents/my-project/python-snippets/notebook/temp/file.txt

p_rel = pathlib.Path('temp/dir/../file.txt')

print(p_rel)
# temp/dir/../file.txt

print(p_rel.resolve())
# /Users/mbp/Documents/my-project/python-snippets/notebook/temp/file.txt

p_abs = pathlib.Path('/Users/mbp/Documents/my-project/python-snippets/notebook/temp/file.txt')

print(p_abs)
# /Users/mbp/Documents/my-project/python-snippets/notebook/temp/file.txt

print(p_abs.relative_to(p.cwd()))
# temp/file.txt

print(p_abs.relative_to('/Users/mbp/Documents/my-project'))
# python-snippets/notebook/temp/file.txt

# print(p_abs.relative_to('/usr/'))
# ValueError: '/Users/mbp/Documents/my-project/python-snippets/notebook/temp/file.txt' does not start with '/usr'

p_rel = pathlib.Path('temp/dir/sub_dir/file2.txt')

print(p_rel.relative_to('temp/dir'))
# sub_dir/file2.txt

print(p_abs)
# /Users/mbp/Documents/my-project/python-snippets/notebook/temp/file.txt

print(p_abs.is_absolute())
# True

print(p_rel)
# temp/dir/sub_dir/file2.txt

print(p_rel.is_absolute())
# False

import shutil

shutil.rmtree('temp')
