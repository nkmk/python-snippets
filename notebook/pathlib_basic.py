import util_make_files

util_make_files.pathlib_basic()

import pathlib
import os
import pprint

p_file = pathlib.Path('temp/file.txt')

print(p_file)
# temp/file.txt

print(type(p_file))
# <class 'pathlib.PosixPath'>

p_dir = pathlib.Path('temp/dir')

print(p_dir)
# temp/dir

print(type(p_dir))
# <class 'pathlib.PosixPath'>

print(p_file.is_file())
# True

print(p_dir.is_file())
# False

p_new_file = pathlib.Path('temp/new_file.txt')

print(p_new_file.exists())
# False

p_new_file.touch()

print(p_new_file.exists())
# True

pathlib.Path('temp/new_file2.txt').touch()

pprint.pprint(list(pathlib.Path('temp').iterdir()))
# [PosixPath('temp/file.txt'),
#  PosixPath('temp/new_file.txt'),
#  PosixPath('temp/new_file2.txt'),
#  PosixPath('temp/dir')]

p_sub_dir_file = p_dir / 'sub_dir' / 'file2.txt'

print(p_sub_dir_file)
# temp/dir/sub_dir/file2.txt

print(p_sub_dir_file.is_file())
# True

p_sub_dir_file = p_dir.joinpath('sub_dir', 'file2.txt')

print(p_sub_dir_file)
# temp/dir/sub_dir/file2.txt

print(p_sub_dir_file.is_file())
# True

p_file_join = p_dir.joinpath('..', 'file.txt')

print(p_file_join)
# temp/dir/../file.txt

print(p_file)
# temp/file.txt

print(p_file.samefile(p_file_join))
# True

print(p_file == p_file_join)
# False

print(p_file_join.resolve())
# /Users/mbp/Documents/my-project/python-snippets/notebook/temp/file.txt

print(p_file.resolve())
# /Users/mbp/Documents/my-project/python-snippets/notebook/temp/file.txt

print(p_file_join.resolve() == p_file.resolve())
# True

print(type(p_file.resolve()))
# <class 'pathlib.PosixPath'>

print(p_file_join.resolve().relative_to(pathlib.Path.cwd()))
# temp/file.txt

print(p_dir.parent)
# temp

print(p_dir.parent.joinpath('file.txt'))
# temp/file.txt

print(p_file_join.parent)
# temp/dir/..

print(p_file.parent)
# temp

s = str(p_file)

print(s)
# temp/file.txt

print(type(s))
# <class 'str'>

print(os.path.isfile('temp/file.txt'))
# True

print(os.path.isfile(p_file))
# True

import shutil

shutil.rmtree('temp')
