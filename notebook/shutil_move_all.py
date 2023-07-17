import os
from pathlib import Path

os.chdir('data/temp')

p = Path('temp')
p.joinpath('dir1/dir').mkdir(parents=True, exist_ok=True)
p.joinpath('dir2').mkdir(parents=True, exist_ok=True)
p.joinpath('dir1/file.txt').touch()

!tree temp -nF  # Only works in Jupyter Notebook
# temp/
# ├── dir1/
# │   ├── dir/
# │   └── file.txt
# └── dir2/
# 
# 4 directories, 1 file

import shutil
import os

src_dir = 'temp/dir1'
dst_dir = 'temp/dir2'

for p in os.listdir(src_dir):
    shutil.move(os.path.join(src_dir, p), dst_dir)

!tree temp -nF
# temp/
# ├── dir1/
# └── dir2/
#     ├── dir/
#     └── file.txt
# 
# 4 directories, 1 file

shutil.rmtree('temp')
