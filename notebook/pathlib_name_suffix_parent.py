from pathlib import Path

p_file = Path('dir/sub_dir/file.txt')
print(p_file)
# dir/sub_dir/file.txt

print(type(p_file))
# <class 'pathlib.PosixPath'>

print(p_file.name)
# file.txt

print(type(p_file.name))
# <class 'str'>

print(p_file.stem)
# file

print(type(p_file.stem))
# <class 'str'>

p_dir = Path('dir/sub_dir/')
print(p_dir)
# dir/sub_dir

print(p_dir.name)
# sub_dir

print(p_dir.stem)
# sub_dir

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

p_tar_gz = Path('dir/sub_dir/file.tar.gz')
print(p_tar_gz)
# dir/sub_dir/file.tar.gz

print(p_tar_gz.suffix)
# .gz

print(p_tar_gz.suffixes)
# ['.tar', '.gz']

print(p_file.suffixes)
# ['.txt']

print(p_dir.suffixes)
# []

print(p_file.parent)
# dir/sub_dir

print(type(p_file.parent))
# <class 'pathlib.PosixPath'>

print(p_file.parent.name)
# sub_dir

print(type(p_file.parent.name))
# <class 'str'>

print(p_file.parents[0])
# dir/sub_dir

print(p_file.parents[1])
# dir

print(p_file.parents[2])
# .

# print(p_file.parents[3])
# IndexError: 3

p_abs = p_file.resolve()
print(p_abs)
# /Users/mbp/Documents/my-project/python-snippets/notebook/dir/sub_dir/file.txt

print(p_abs.parents[3])
# /Users/mbp/Documents/my-project/python-snippets

# print(p_abs.parents[9])
# IndexError: 9

print(p_file.parents[-1])
# .

print(p_file.parents[-2])
# dir

print(p_file.parents[-3])
# dir/sub_dir

print(p_abs.parents[-1])
# /

print(p_abs.parents[-2])
# /Users

print(p_abs.parents[-3])
# /Users/mbp

p_file_rel = Path('dir/sub_dir/../sub_dir/file.txt')
print(p_file_rel)
# dir/sub_dir/../sub_dir/file.txt

print(p_file_rel.parents[0])
# dir/sub_dir/../sub_dir

print(p_file_rel.parents[1])
# dir/sub_dir/..

print(p_file_rel.parents[2])
# dir/sub_dir

print(p_file.resolve())
# /Users/mbp/Documents/my-project/python-snippets/notebook/dir/sub_dir/file.txt

print(p_file_rel.resolve())
# /Users/mbp/Documents/my-project/python-snippets/notebook/dir/sub_dir/file.txt

print(p_file.resolve() == p_file_rel.resolve())
# True

print(p_file_rel.resolve().relative_to(Path.cwd()))
# dir/sub_dir/file.txt

print(p_file.with_name('new_file.txt'))
# dir/sub_dir/new_file.txt

print(type(p_file.with_name('new_file.txt')))
# <class 'pathlib.PosixPath'>

print(p_dir.with_name('new_dir'))
# dir/new_dir

print(p_dir.with_name('new_file.txt'))
# dir/new_file.txt

print(p_dir.joinpath('new_dir'))
# dir/sub_dir/new_dir

print(p_dir / 'new_file.txt')
# dir/sub_dir/new_file.txt

p_file.with_name('new_dir').mkdir(parents=True)
p_file.with_name('new_file.txt').touch()

p_file.with_name('new_file.txt').unlink()
p_file.with_name('new_dir').rmdir()
p_file.parent.rmdir()
p_file.parent.parent.rmdir()

print(p_file.with_suffix('.text'))
# dir/sub_dir/file.text

print(type(p_file.with_suffix('.text')))
# <class 'pathlib.PosixPath'>

# print(p_file.with_suffix('text'))
# ValueError: Invalid suffix 'text'

print(p_dir.with_suffix('.text'))
# dir/sub_dir.text

print(p_file.with_stem('new_file'))
# dir/sub_dir/new_file.txt

print(type(p_file.with_stem('new_file')))
# <class 'pathlib.PosixPath'>

print(p_dir.with_stem('new_dir'))
# dir/new_dir
