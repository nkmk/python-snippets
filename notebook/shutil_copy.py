import os
from pathlib import Path

os.chdir('data/temp')

p = Path('temp')
p.joinpath('dir1').mkdir(parents=True, exist_ok=True)
p.joinpath('dir2').mkdir(parents=True, exist_ok=True)
p.joinpath('file.txt').touch()
p.joinpath('dir2/file.txt').touch()
p.joinpath('dir2/file2.txt').touch()

!tree temp -nF  # Only works in Jupyter Notebook
# temp/
# ├── dir1/
# ├── dir2/
# │   ├── file.txt
# │   └── file2.txt
# └── file.txt
# 
# 3 directories, 3 files

import shutil

new_path = shutil.copy('temp/file.txt', 'temp/dir1')
print(new_path)
# temp/dir1/file.txt

new_path = shutil.copy('temp/file.txt', 'temp/dir2')
print(new_path)
# temp/dir2/file.txt

new_path = shutil.copy('temp/file.txt', 'temp/dir1/file2.txt')
print(new_path)
# temp/dir1/file2.txt

# new_path = shutil.copy('temp/file.txt', 'temp/dir2/new_dir/file2.txt')
# FileNotFoundError: [Errno 2] No such file or directory: 'temp/dir2/new_dir/file2.txt'

new_path = shutil.copy('temp/file.txt', 'temp/dir2/file2.txt')
print(new_path)
# temp/dir2/file2.txt

!tree temp -nF
# temp/
# ├── dir1/
# │   ├── file.txt
# │   └── file2.txt
# ├── dir2/
# │   ├── file.txt
# │   └── file2.txt
# └── file.txt
# 
# 3 directories, 5 files

import os

new_path = shutil.copy('temp/file.txt', 'temp/file_copy.txt')
print(new_path)
# temp/file_copy.txt

print(os.path.getmtime('temp/file.txt') == os.path.getmtime('temp/file_copy.txt'))
# False

new_path = shutil.copy2('temp/file.txt', 'temp/file_copy2.txt')
print(new_path)
# temp/file_copy2.txt

print(os.path.getmtime('temp/file.txt') == os.path.getmtime('temp/file_copy2.txt'))
# True

shutil.rmtree('temp')
