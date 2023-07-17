import os
import shutil
from pathlib import Path

os.chdir('data/temp')

def setup():
    p = Path('temp')
    p.joinpath('dir').mkdir(parents=True, exist_ok=True)
    p.joinpath('dir/000.csv').touch()
    p.joinpath('dir/789.txt').touch()
    p.joinpath('dir/xyz.jpg').touch()
    p.joinpath('123.jpg').touch()
    p.joinpath('456.txt').touch()
    p.joinpath('abc.txt').touch()

setup()

!tree temp -nF
# temp/
# ├── 123.jpg
# ├── 456.txt
# ├── abc.txt
# └── dir/
#     ├── 000.csv
#     ├── 789.txt
#     └── xyz.jpg
# 
# 2 directories, 6 files

import os
import glob
import re

for p in glob.glob('temp/**/*.txt', recursive=True):
    if os.path.isfile(p):
        os.remove(p)

!tree temp -nF
# temp/
# ├── 123.jpg
# └── dir/
#     ├── 000.csv
#     └── xyz.jpg
# 
# 2 directories, 3 files

shutil.rmtree('temp')

setup()

for p in glob.glob('temp/**', recursive=True):
    if os.path.isfile(p) and re.search('\d+\.(txt|csv)', p):
        os.remove(p)

!tree temp -nF
# temp/
# ├── 123.jpg
# ├── abc.txt
# └── dir/
#     └── xyz.jpg
# 
# 2 directories, 3 files

shutil.rmtree('temp')
