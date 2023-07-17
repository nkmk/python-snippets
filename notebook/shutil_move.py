import os
from pathlib import Path

os.chdir('data/temp')

p = Path('temp')
p.joinpath('dir1/subdir').mkdir(parents=True, exist_ok=True)
p.joinpath('dir2').mkdir(parents=True, exist_ok=True)
p.joinpath('dir3/subdir').mkdir(parents=True, exist_ok=True)
p.joinpath('dir1/file.txt').touch()
p.joinpath('dir1/subdir/subfile.txt').touch()
p.joinpath('dir3/file.txt').touch()

!tree temp -nF  # Only works in Jupyter Notebook
# temp/
# ├── dir1/
# │   ├── file.txt
# │   └── subdir/
# │       └── subfile.txt
# ├── dir2/
# └── dir3/
#     ├── file.txt
#     └── subdir/
# 
# 6 directories, 3 files

import shutil

new_path = shutil.move('temp/dir1/file.txt', 'temp/dir2')
print(new_path)
# temp/dir2/file.txt

!tree temp -nF
# temp/
# ├── dir1/
# │   └── subdir/
# │       └── subfile.txt
# ├── dir2/
# │   └── file.txt
# └── dir3/
#     ├── file.txt
#     └── subdir/
# 
# 6 directories, 3 files

# new_path = shutil.move('temp/dir2/file.txt', 'temp/dir3')
# Error: Destination path 'temp/dir3/file.txt' already exists

new_path = shutil.move('temp/dir1/subdir', 'temp/dir2')
print(new_path)
# temp/dir2/subdir

!tree temp -nF
# temp/
# ├── dir1/
# ├── dir2/
# │   ├── file.txt
# │   └── subdir/
# │       └── subfile.txt
# └── dir3/
#     ├── file.txt
#     └── subdir/
# 
# 6 directories, 3 files

# new_path = shutil.move('temp/dir2/subdir', 'temp/dir3')
# Error: Destination path 'temp/dir3/subdir' already exists

# new_path = shutil.move('temp/dir2/subdir', 'temp/dir2/file.txt')
# FileExistsError: [Errno 17] File exists: 'temp/dir2/file.txt'

shutil.rmtree('temp/dir3')

new_path = shutil.move('temp/dir2/file.txt', 'temp/dir1/file_new.txt')
print(new_path)
# temp/dir1/file_new.txt

!tree temp -nF
# temp/
# ├── dir1/
# │   └── file_new.txt
# └── dir2/
#     └── subdir/
#         └── subfile.txt
# 
# 4 directories, 2 files

# new_path = shutil.move('temp/dir1/file_new.txt', 'temp/dir2/dir_new/file_new.txt')
# FileNotFoundError: [Errno 2] No such file or directory: 'temp/dir2/dir_new/file_new.txt'

new_path = shutil.move('temp/dir2/subdir', 'temp/dir1/subdir_new')
print(new_path)
# temp/dir1/subdir_new

!tree temp -nF
# temp/
# ├── dir1/
# │   ├── file_new.txt
# │   └── subdir_new/
# │       └── subfile.txt
# └── dir2/
# 
# 4 directories, 2 files

new_path = shutil.move('temp/dir1/subdir_new', 'temp/dir2/subdir/subdir2')
print(new_path)
# temp/dir2/subdir/subdir2

!tree temp -nF
# temp/
# ├── dir1/
# │   └── file_new.txt
# └── dir2/
#     └── subdir/
#         └── subdir2/
#             └── subfile.txt
# 
# 5 directories, 2 files

with open('temp/dir2/file_other.txt', 'w') as f:
    f.write('text in file_other.txt')

!tree temp -nF
# temp/
# ├── dir1/
# │   └── file_new.txt
# └── dir2/
#     ├── file_other.txt
#     └── subdir/
#         └── subdir2/
#             └── subfile.txt
# 
# 5 directories, 3 files

new_path = shutil.move('temp/dir2/file_other.txt', 'temp/dir1/file_new.txt')
print(new_path)
# temp/dir1/file_new.txt

!tree temp -nF
# temp/
# ├── dir1/
# │   └── file_new.txt
# └── dir2/
#     └── subdir/
#         └── subdir2/
#             └── subfile.txt
# 
# 5 directories, 2 files

with open('temp/dir1/file_new.txt') as f:
    print(f.read())
# text in file_other.txt

shutil.rmtree('temp')
