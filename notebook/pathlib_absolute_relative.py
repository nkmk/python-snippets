from pathlib import Path

p = Path('dir/sub_dir/file.txt')
print(p)
# dir/sub_dir/file.txt

print(type(p))
# <class 'pathlib.PosixPath'>

print(Path.cwd())
# /Users/mbp/Documents/my-project/python-snippets/notebook

print(type(Path.cwd()))
# <class 'pathlib.PosixPath'>

print(p.cwd())
# /Users/mbp/Documents/my-project/python-snippets/notebook

print(type(p.cwd()))
# <class 'pathlib.PosixPath'>

import os

print(os.getcwd())
# /Users/mbp/Documents/my-project/python-snippets/notebook

print(type(os.getcwd()))
# <class 'str'>

print(p.resolve())
# /Users/mbp/Documents/my-project/python-snippets/notebook/dir/sub_dir/file.txt

p_rel = Path('dir/sub_dir/../file.txt')
print(p_rel)
# dir/sub_dir/../file.txt

print(p_rel.resolve())
# /Users/mbp/Documents/my-project/python-snippets/notebook/dir/file.txt

p_new_file = Path('data/new_file.txt')

print(p_new_file.resolve())
# /Users/mbp/Documents/my-project/python-snippets/notebook/data/new_file.txt

# print(p_new_file.resolve(strict=True))
# FileNotFoundError: [Errno 2] No such file or directory: 'data/new_file.txt'

print(p.absolute())
# /Users/mbp/Documents/my-project/python-snippets/notebook/dir/sub_dir/file.txt

print(p_rel.absolute())
# /Users/mbp/Documents/my-project/python-snippets/notebook/dir/sub_dir/../file.txt

p_abs = Path('dir/sub_dir/file.txt').resolve()
print(p_abs)
# /Users/mbp/Documents/my-project/python-snippets/notebook/dir/sub_dir/file.txt

print(p_abs.relative_to(Path.cwd()))
# dir/sub_dir/file.txt

print(p_abs.relative_to('/Users/mbp/Documents/my-project'))
# python-snippets/notebook/dir/sub_dir/file.txt

# print(p_abs.relative_to('/usr/'))
# ValueError: '/Users/mbp/Documents/my-project/python-snippets/notebook/dir/sub_dir/file.txt' is not in the subpath of '/usr' OR one path is relative and the other is absolute.

print(p.relative_to('dir'))
# sub_dir/file.txt

print(p_abs.is_absolute())
# True

print(p.is_absolute())
# False

print(p_abs.is_relative_to(Path.cwd()))
# True

print(p.is_relative_to(Path.cwd()))
# False

print(p.is_relative_to('dir/sub_dir'))
# True
