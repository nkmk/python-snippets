import os
from pathlib import Path

os.chdir('data/temp')

p = Path('temp')
p.joinpath('dir1/dir2/dir3').mkdir(parents=True, exist_ok=True)
p.joinpath('dir1/file.txt').touch()

!tree temp -nF
# temp/
# └── dir1/
#     ├── dir2/
#     │   └── dir3/
#     └── file.txt
# 
# 4 directories, 1 file

os.removedirs('temp/dir1/dir2/dir3')

!tree temp -nF
# temp/
# └── dir1/
#     └── file.txt
# 
# 2 directories, 1 file

import shutil

shutil.rmtree('temp')
