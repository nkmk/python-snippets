import util_make_files

util_make_files.pathlib_basic()

!tree temp -nF  # Only works in Jupyter Notebook
# temp/
# ├── dir/
# │   └── sub_dir/
# │       └── file2.txt
# └── file.txt
# 
# 3 directories, 2 files

import pathlib

p_file = pathlib.Path('temp/file.txt')
print(p_file)
# temp/file.txt

print(type(p_file))
# <class 'pathlib.PosixPath'>

print(issubclass(pathlib.PosixPath, pathlib.Path))
# True

print(issubclass(pathlib.WindowsPath, pathlib.Path))
# True

print(issubclass(pathlib.Path, pathlib.PurePath))
# True

print(p_file.is_file())
# True

print(p_file.suffix)
# .txt

p_new_file = pathlib.Path('temp/new_file.txt')

print(p_new_file.exists())
# False

p_new_file.touch()

print(p_new_file.exists())
# True

pathlib.Path('temp/new_file2.txt').touch()

for p in pathlib.Path('temp').iterdir():
    print(p)
# temp/file.txt
# temp/new_file.txt
# temp/new_file2.txt
# temp/dir

p_dir = pathlib.Path('temp/dir')

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

print(p_file_join.resolve().relative_to(pathlib.Path.cwd()))
# temp/file.txt

print(p_dir.parent)
# temp

print(p_dir.parent.joinpath('file.txt'))
# temp/file.txt

print(p_file_join.parent)
# temp/dir/..

print(p_file_join.parent.parent)
# temp/dir

print(p_file.with_name('new_file.txt'))
# temp/new_file.txt

s = str(p_file)
print(s)
# temp/file.txt

print(type(s))
# <class 'str'>

import os

print(os.path.isfile('temp/file.txt'))
# True

print(os.path.isfile(pathlib.Path('temp/file.txt')))
# True

import shutil

shutil.rmtree('temp')
