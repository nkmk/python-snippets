import os
from pathlib import Path

os.chdir('data/temp')

p = Path('temp')
p.joinpath('dir1').mkdir(parents=True, exist_ok=True)
p.joinpath('dir2').mkdir(parents=True, exist_ok=True)
p.joinpath('file1').touch()
p.joinpath('file2.txt').touch()
p.joinpath('file3.jpg').touch()
p.joinpath('dir1/file_in_dir').touch()

!tree temp -nF  # Only works in Jupyter Notebook
# temp/
# ├── dir1/
# │   └── file_in_dir
# ├── dir2/
# ├── file1
# ├── file2.txt
# └── file3.jpg
# 
# 3 directories, 4 files

import os

dir_path = "temp"

files = os.listdir(dir_path)
print(files)
# ['file2.txt', 'dir2', 'file3.jpg', 'file1', 'dir1']

print(type(files))
# <class 'list'>

print(sorted(files))
# ['dir1', 'dir2', 'file1', 'file2.txt', 'file3.jpg']

files_file = [
    f for f in os.listdir(dir_path) if os.path.isfile(os.path.join(dir_path, f))
]
print(files_file)
# ['file2.txt', 'file3.jpg', 'file1']

files_dir = [
    f for f in os.listdir(dir_path) if os.path.isdir(os.path.join(dir_path, f))
]
print(files_dir)
# ['dir2', 'dir1']

import shutil

shutil.rmtree(dir_path)
