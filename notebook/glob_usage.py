import os
from pathlib import Path

os.chdir('data/temp')

p = Path('temp')
p.joinpath('dir/sub_dir1').mkdir(parents=True, exist_ok=True)
p.joinpath('dir/sub_dir2').mkdir(parents=True, exist_ok=True)
p.joinpath('aaa.jpg').touch()
p.joinpath('1.txt').touch()
p.joinpath('12.jpg').touch()
p.joinpath('123.txt').touch()
p.joinpath('[x].txt').touch()
p.joinpath('dir/bbb.txt').touch()
p.joinpath('dir/987.jpg').touch()
p.joinpath('dir/sub_dir1/98.txt').touch()
p.joinpath('dir/sub_dir1/ccc.jpg').touch()
p.joinpath('dir/sub_dir2/ddd.jpg').touch()

!tree temp -nF  # Only works in Jupyter Notebook
# temp/
# ├── 1.txt
# ├── 12.jpg
# ├── 123.txt
# ├── [x].txt
# ├── aaa.jpg
# └── dir/
#     ├── 987.jpg
#     ├── bbb.txt
#     ├── sub_dir1/
#     │   ├── 98.txt
#     │   └── ccc.jpg
#     └── sub_dir2/
#         └── ddd.jpg
# 
# 4 directories, 10 files

import glob
import os

l = glob.glob('temp/*.txt')
print(l)
# ['temp/[x].txt', 'temp/1.txt', 'temp/123.txt']

print(type(l))
# <class 'list'>

print(glob.glob('temp/*'))
# ['temp/[x].txt', 'temp/12.jpg', 'temp/aaa.jpg', 'temp/dir', 'temp/1.txt', 'temp/123.txt']

print(glob.glob('temp/*.jpg'))
# ['temp/12.jpg', 'temp/aaa.jpg']

print(glob.glob('temp/dir/*/*.jpg'))
# ['temp/dir/sub_dir1/ccc.jpg', 'temp/dir/sub_dir2/ddd.jpg']

print(glob.glob('temp/???.*'))
# ['temp/[x].txt', 'temp/aaa.jpg', 'temp/123.txt']

print(glob.glob('temp/[0-9].*'))
# ['temp/1.txt']

print(glob.glob('temp/[0-9][0-9].*'))
# ['temp/12.jpg']

print(glob.glob('temp/[a-z][a-z][a-z].*'))
# ['temp/aaa.jpg']

print(glob.glob('temp/[!a-z].*'))
# ['temp/1.txt']

print(glob.glob('temp/[[]*'))
# ['temp/[x].txt']

print(glob.glob('temp/*/*.jpg'))
# ['temp/dir/987.jpg']

print(glob.glob('temp/**/*.jpg', recursive=True))
# ['temp/12.jpg', 'temp/aaa.jpg', 'temp/dir/987.jpg', 'temp/dir/sub_dir1/ccc.jpg', 'temp/dir/sub_dir2/ddd.jpg']

print(glob.glob('temp/**', recursive=True))
# ['temp/', 'temp/[x].txt', 'temp/12.jpg', 'temp/aaa.jpg', 'temp/dir', 'temp/dir/987.jpg', 'temp/dir/sub_dir1', 'temp/dir/sub_dir1/ccc.jpg', 'temp/dir/sub_dir1/98.txt', 'temp/dir/bbb.txt', 'temp/dir/sub_dir2', 'temp/dir/sub_dir2/ddd.jpg', 'temp/1.txt', 'temp/123.txt']

print(glob.glob('temp/*.txt'))
# ['temp/[x].txt', 'temp/1.txt', 'temp/123.txt']

print(glob.glob('*.txt', root_dir='temp'))
# ['[x].txt', '1.txt', '123.txt']

print([p for p in glob.glob('temp/**', recursive=True) if os.path.isfile(p)])
# ['temp/[x].txt', 'temp/12.jpg', 'temp/aaa.jpg', 'temp/dir/987.jpg', 'temp/dir/sub_dir1/ccc.jpg', 'temp/dir/sub_dir1/98.txt', 'temp/dir/bbb.txt', 'temp/dir/sub_dir2/ddd.jpg', 'temp/1.txt', 'temp/123.txt']

print([os.path.basename(p) for p in glob.glob('temp/**', recursive=True)
       if os.path.isfile(p)])
# ['[x].txt', '12.jpg', 'aaa.jpg', '987.jpg', 'ccc.jpg', '98.txt', 'bbb.txt', 'ddd.jpg', '1.txt', '123.txt']

print([p for p in glob.glob('**', recursive=True, root_dir='temp')
       if os.path.isfile(os.path.join('temp', p))])
# ['[x].txt', '12.jpg', 'aaa.jpg', 'dir/987.jpg', 'dir/sub_dir1/ccc.jpg', 'dir/sub_dir1/98.txt', 'dir/bbb.txt', 'dir/sub_dir2/ddd.jpg', '1.txt', '123.txt']

print(glob.glob('temp/**/', recursive=True))
# ['temp/', 'temp/dir/', 'temp/dir/sub_dir1/', 'temp/dir/sub_dir2/']

print(glob.glob('temp/*/**/', recursive=True))
# ['temp/dir/', 'temp/dir/sub_dir1/', 'temp/dir/sub_dir2/']

print(glob.glob('**/', recursive=True, root_dir='temp'))
# ['dir/', 'dir/sub_dir1/', 'dir/sub_dir2/']

print([p.rstrip(os.sep) for p in glob.glob('temp/**/', recursive=True)])
# ['temp', 'temp/dir', 'temp/dir/sub_dir1', 'temp/dir/sub_dir2']

print([os.path.basename(p.rstrip(os.sep)) for p
       in glob.glob(os.path.join('temp/**/'), recursive=True)])
# ['temp', 'dir', 'sub_dir1', 'sub_dir2']

print([os.path.basename(p.rstrip(os.sep)) + os.sep for p
       in glob.glob(os.path.join('temp/**/'), recursive=True)])
# ['temp/', 'dir/', 'sub_dir1/', 'sub_dir2/']

import re

print([p for p in glob.glob('temp/**', recursive=True)
       if re.search('\d+\.txt', p)])
# ['temp/dir/sub_dir1/98.txt', 'temp/1.txt', 'temp/123.txt']

print([p for p in glob.glob('temp/**', recursive=True)
       if re.search('\D{3}\.(txt|jpg)', p)])
# ['temp/[x].txt', 'temp/aaa.jpg', 'temp/dir/sub_dir1/ccc.jpg', 'temp/dir/bbb.txt', 'temp/dir/sub_dir2/ddd.jpg']

print(type(glob.iglob('temp/*.txt')))
# <class 'generator'>

for p in glob.iglob('temp/*.txt'):
    print(p)
# temp/[x].txt
# temp/1.txt
# temp/123.txt

import shutil

shutil.rmtree('temp')
