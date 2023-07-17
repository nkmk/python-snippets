import os
from pathlib import Path

os.chdir('data/temp')

p = Path('temp')
p.joinpath('dir1/subdir').mkdir(parents=True, exist_ok=True)
p.joinpath('dir1/file.txt').touch()
p.joinpath('dir1/subdir/file2.txt').touch()

!tree temp -nF  # Only works in Jupyter Notebook
# temp/
# └── dir1/
#     ├── file.txt
#     └── subdir/
#         └── file2.txt
# 
# 3 directories, 2 files

import shutil

new_path = shutil.copytree('temp/dir1', 'temp/dir2/new_dir')
print(new_path)
# temp/dir2/new_dir

!tree temp -nF
# temp/
# ├── dir1/
# │   ├── file.txt
# │   └── subdir/
# │       └── file2.txt
# └── dir2/
#     └── new_dir/
#         ├── file.txt
#         └── subdir/
#             └── file2.txt
# 
# 6 directories, 4 files

# new_path = shutil.copytree('temp/dir1', 'temp/dir2/new_dir')
# FileExistsError: [Errno 17] File exists: 'temp/dir2/new_dir'

new_path = shutil.copytree('temp/dir1', 'temp/dir2/new_dir', dirs_exist_ok=True)
print(new_path)
# temp/dir2/new_dir

import os

new_path = shutil.copytree('temp/dir1', 'temp/dir_copy2')
print(new_path)
# temp/dir_copy2

print(os.path.getmtime('temp/dir1/file.txt') == os.path.getmtime('temp/dir_copy2/file.txt'))
# True

new_path = shutil.copytree('temp/dir1', 'temp/dir_copy', copy_function=shutil.copy)
print(new_path)
# temp/dir_copy

print(os.path.getmtime('temp/dir1/file.txt') == os.path.getmtime('temp/dir_copy/file.txt'))
# False

shutil.rmtree('temp')

p = Path('temp')
p.joinpath('dir1/subdir').mkdir(parents=True, exist_ok=True)
p.joinpath('dir1/.dir').mkdir(parents=True, exist_ok=True)
p.joinpath('dir1/file.txt').touch()
p.joinpath('dir1/.config').touch()
p.joinpath('dir1/subdir/file.txt').touch()
p.joinpath('dir1/subdir/file.jpg').touch()
p.joinpath('dir1/subdir/file.txt').touch()

!tree temp -anF
# temp/
# └── dir1/
#     ├── .config
#     ├── .dir/
#     ├── file.txt
#     └── subdir/
#         ├── file.jpg
#         └── file.txt
# 
# 4 directories, 4 files

new_path = shutil.copytree(
    'temp/dir1', 'temp/dir2', ignore=shutil.ignore_patterns('.*', '*.jpg')
)
print(new_path)
# temp/dir2

!tree temp -anF
# temp/
# ├── dir1/
# │   ├── .config
# │   ├── .dir/
# │   ├── file.txt
# │   └── subdir/
# │       ├── file.jpg
# │       └── file.txt
# └── dir2/
#     ├── file.txt
#     └── subdir/
#         └── file.txt
# 
# 6 directories, 6 files

shutil.rmtree('temp')
