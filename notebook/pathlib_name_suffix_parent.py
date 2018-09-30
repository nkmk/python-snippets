import util_make_files

util_make_files.pathlib_basic()

import pathlib

p_file = pathlib.Path('temp/file.txt')

print(p_file)
# temp/file.txt

print(type(p_file))
# <class 'pathlib.PosixPath'>

print(str(p_file))
# temp/file.txt

print(type(str(p_file)))
# <class 'str'>

print(p_file.name)
# file.txt

print(type(p_file.name))
# <class 'str'>

print(p_file.stem)
# file

print(type(p_file.stem))
# <class 'str'>

p_dir = pathlib.Path('temp/dir/')

print(p_dir)
# temp/dir

print(type(p_dir))
# <class 'pathlib.PosixPath'>

print(p_dir.name)
# dir

print(p_dir.stem)
# dir

print(p_file.suffix)
# .txt

print(type(p_file.suffix))
# <class 'str'>

print(p_dir.suffix)
# 

print(p_file.suffix.lstrip('.'))
# txt

print(p_file.suffix[1:])
# txt

print(p_dir.suffix.lstrip('.'))
# 

print(p_dir.suffix[1:])
# 

p_sub = pathlib.Path('temp/dir/sub_dir/file2.txt')

print(p_sub)
# temp/dir/sub_dir/file2.txt

print(p_sub.parent)
# temp/dir/sub_dir

print(type(p_sub.parent))
# <class 'pathlib.PosixPath'>

print(p_sub.parents[0])
# temp/dir/sub_dir

print(p_sub.parents[1])
# temp/dir

print(p_sub.parents[2])
# temp

print(p_sub.parents[3])
# .

# print(p_sub.parents[4])
# IndexError: 4

p_abs = p_sub.resolve()

print(p_abs)
# /Users/mbp/Documents/my-project/python-snippets/notebook/temp/dir/sub_dir/file2.txt

print(p_abs.parents[4])
# /Users/mbp/Documents/my-project/python-snippets

# print(p_abs.parents[10])
# IndexError: 10

p_file = pathlib.Path('temp/file.txt')

print(p_file)
# temp/file.txt

p_file_rel = pathlib.Path('temp/dir/sub_dir/../../file.txt')

print(p_file_rel)
# temp/dir/sub_dir/../../file.txt

print(p_file.samefile(p_file_rel))
# True

print(p_file.parents[0])
# temp

print(p_file.parents[1])
# .

print(p_file_rel.parents[0])
# temp/dir/sub_dir/../..

print(p_file_rel.parents[1])
# temp/dir/sub_dir/..

print(p_file_rel.parents[2])
# temp/dir/sub_dir

print(p_file_rel.parents[3])
# temp/dir

print(p_file_rel.resolve())
# /Users/mbp/Documents/my-project/python-snippets/notebook/temp/file.txt

print(p_file_rel.resolve().relative_to(p_file_rel.cwd()))
# temp/file.txt

print(p_file.with_name('file_new.txt'))
# temp/file_new.txt

print(type(p_file.with_name('file_new.txt')))
# <class 'pathlib.PosixPath'>

print(p_dir.with_name('dir_new'))
# temp/dir_new

print(p_dir.with_name('file_new.txt'))
# temp/file_new.txt

p_file.with_name('file_new.txt').touch()

print(p_file.with_name('file_new.txt').exists())
# True

print(p_file.with_suffix('.text'))
# temp/file.text

print(type(p_file.with_suffix('.text')))
# <class 'pathlib.PosixPath'>

# print(p_file.with_suffix('text'))
# ValueError: Invalid suffix 'text'

import shutil

shutil.rmtree('temp')
