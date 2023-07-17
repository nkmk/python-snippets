import os
from pathlib import Path

os.chdir('data/temp')

def setup():
    p = Path('temp')
    p.joinpath('dir1/subdir').mkdir(parents=True, exist_ok=True)
    p.joinpath('dir1/subdir/000.csv').touch()
    p.joinpath('dir1/subdir/789.txt').touch()
    p.joinpath('dir1/subdir/xyz.jpg').touch()
    p.joinpath('dir1/123.jpg').touch()
    p.joinpath('dir1/456.txt').touch()
    p.joinpath('dir1/abc.txt').touch()

setup()

!tree temp -nF  # Only works in Jupyter Notebook
# temp/
# └── dir1/
#     ├── 123.jpg
#     ├── 456.txt
#     ├── abc.txt
#     └── subdir/
#         ├── 000.csv
#         ├── 789.txt
#         └── xyz.jpg
# 
# 3 directories, 6 files

import shutil
import glob
import os
import re

os.makedirs('temp/dir2')

for p in glob.glob('temp/dir1/**/*.txt', recursive=True):
    if os.path.isfile(p):
        shutil.copy(p, 'temp/dir2')

!tree temp -nF
# temp/
# ├── dir1/
# │   ├── 123.jpg
# │   ├── 456.txt
# │   ├── abc.txt
# │   └── subdir/
# │       ├── 000.csv
# │       ├── 789.txt
# │       └── xyz.jpg
# └── dir2/
#     ├── 456.txt
#     ├── 789.txt
#     └── abc.txt
# 
# 4 directories, 9 files

src_dir = 'temp/dir1'
dst_dir = 'temp/dir3'

for p in glob.glob('**/*.txt', recursive=True, root_dir=src_dir):
    if os.path.isfile(os.path.join(src_dir, p)):
        os.makedirs(os.path.join(dst_dir, os.path.dirname(p)), exist_ok=True)
        shutil.copy(os.path.join(src_dir, p), os.path.join(dst_dir, p))

!tree temp -nF
# temp/
# ├── dir1/
# │   ├── 123.jpg
# │   ├── 456.txt
# │   ├── abc.txt
# │   └── subdir/
# │       ├── 000.csv
# │       ├── 789.txt
# │       └── xyz.jpg
# ├── dir2/
# │   ├── 456.txt
# │   ├── 789.txt
# │   └── abc.txt
# └── dir3/
#     ├── 456.txt
#     ├── abc.txt
#     └── subdir/
#         └── 789.txt
# 
# 6 directories, 12 files

shutil.rmtree('temp')

setup()

!tree temp -nF
# temp/
# └── dir1/
#     ├── 123.jpg
#     ├── 456.txt
#     ├── abc.txt
#     └── subdir/
#         ├── 000.csv
#         ├── 789.txt
#         └── xyz.jpg
# 
# 3 directories, 6 files

os.makedirs('temp/dir2')

for p in glob.glob('temp/dir1/**', recursive=True):
    if os.path.isfile(p) and re.search('\d+\.(txt|csv)', p):
        shutil.copy(p, 'temp/dir2')

!tree temp -nF
# temp/
# ├── dir1/
# │   ├── 123.jpg
# │   ├── 456.txt
# │   ├── abc.txt
# │   └── subdir/
# │       ├── 000.csv
# │       ├── 789.txt
# │       └── xyz.jpg
# └── dir2/
#     ├── 000.csv
#     ├── 456.txt
#     └── 789.txt
# 
# 4 directories, 9 files

src_dir = 'temp/dir1'
dst_dir = 'temp/dir3'

for p in glob.glob('**', recursive=True, root_dir=src_dir):
    if os.path.isfile(os.path.join(src_dir, p)) and re.search('\d+\.(txt|csv)', p):
        os.makedirs(os.path.join(dst_dir, os.path.dirname(p)), exist_ok=True)
        shutil.copy(os.path.join(src_dir, p), os.path.join(dst_dir, p))

!tree temp -nF
# temp/
# ├── dir1/
# │   ├── 123.jpg
# │   ├── 456.txt
# │   ├── abc.txt
# │   └── subdir/
# │       ├── 000.csv
# │       ├── 789.txt
# │       └── xyz.jpg
# ├── dir2/
# │   ├── 000.csv
# │   ├── 456.txt
# │   └── 789.txt
# └── dir3/
#     ├── 456.txt
#     └── subdir/
#         ├── 000.csv
#         └── 789.txt
# 
# 6 directories, 12 files

shutil.rmtree('temp')
