import os
from pathlib import Path

os.chdir('data/temp')

def setup():
    p = Path('temp')
    p.joinpath('dir').mkdir(parents=True, exist_ok=True)
    p.joinpath('dir2').mkdir(parents=True, exist_ok=True)
    p.joinpath('dir/000.csv').touch()
    p.joinpath('dir/789.txt').touch()
    p.joinpath('dir/xyz.jpg').touch()
    p.joinpath('123.jpg').touch()
    p.joinpath('456.txt').touch()
    p.joinpath('abc.txt').touch()

setup()

!tree temp -nF  # Only works in Jupyter Notebook
# temp/
# ├── 123.jpg
# ├── 456.txt
# ├── abc.txt
# ├── dir/
# │   ├── 000.csv
# │   ├── 789.txt
# │   └── xyz.jpg
# └── dir2/
# 
# 3 directories, 6 files

import shutil
import glob
import re

for p in glob.glob('temp/**/*.txt', recursive=True):
    shutil.move(p, 'temp/dir2')

!tree temp -nF
# temp/
# ├── 123.jpg
# ├── dir/
# │   ├── 000.csv
# │   └── xyz.jpg
# └── dir2/
#     ├── 456.txt
#     ├── 789.txt
#     └── abc.txt
# 
# 3 directories, 6 files

shutil.rmtree('temp')

setup()

!tree temp -nF
# temp/
# ├── 123.jpg
# ├── 456.txt
# ├── abc.txt
# ├── dir/
# │   ├── 000.csv
# │   ├── 789.txt
# │   └── xyz.jpg
# └── dir2/
# 
# 3 directories, 6 files

for p in glob.glob('temp/**', recursive=True):
    if re.search('\d+\.(txt|csv)', p):
        shutil.move(p, 'temp/dir2')

!tree temp -nF
# temp/
# ├── 123.jpg
# ├── abc.txt
# ├── dir/
# │   └── xyz.jpg
# └── dir2/
#     ├── 000.csv
#     ├── 456.txt
#     └── 789.txt
# 
# 3 directories, 6 files

shutil.rmtree('temp')
