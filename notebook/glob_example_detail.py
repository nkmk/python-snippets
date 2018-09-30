import util_make_files

util_make_files.glob_example_detail()

import glob
import re
import os

l = glob.glob('temp/*.txt')

print(l)
# ['temp/[x].txt', 'temp/1.txt', 'temp/123.txt']

print(type(l))
# <class 'list'>

print(glob.glob('temp/*'))
# ['temp/[x].txt', 'temp/aaa.text', 'temp/dir', 'temp/1.txt', 'temp/12.text', 'temp/123.txt']

print(glob.glob('temp/*.txt'))
# ['temp/[x].txt', 'temp/1.txt', 'temp/123.txt']

print(glob.glob('temp/dir/*/*.text'))
# ['temp/dir/sub_dir1/ccc.text', 'temp/dir/sub_dir2/ddd.text']

print(glob.glob('temp/???.*'))
# ['temp/[x].txt', 'temp/aaa.text', 'temp/123.txt']

print(glob.glob('temp/[0-9].*'))
# ['temp/1.txt']

print(glob.glob('temp/[0-9][0-9].*'))
# ['temp/12.text']

print(glob.glob('temp/[a-z][a-z][a-z].*'))
# ['temp/aaa.text']

print(glob.glob('temp/[[]*'))
# ['temp/[x].txt']

print(glob.glob('temp/dir/*/*.text'))
# ['temp/dir/sub_dir1/ccc.text', 'temp/dir/sub_dir2/ddd.text']

print(glob.glob('temp/**/*.text', recursive=True))
# ['temp/aaa.text', 'temp/12.text', 'temp/dir/987.text', 'temp/dir/sub_dir1/ccc.text', 'temp/dir/sub_dir2/ddd.text']

print(glob.glob('temp/**', recursive=True))
# ['temp/', 'temp/[x].txt', 'temp/aaa.text', 'temp/dir', 'temp/dir/sub_dir1', 'temp/dir/sub_dir1/98.txt', 'temp/dir/sub_dir1/ccc.text', 'temp/dir/987.text', 'temp/dir/bbb.txt', 'temp/dir/sub_dir2', 'temp/dir/sub_dir2/ddd.text', 'temp/1.txt', 'temp/12.text', 'temp/123.txt']

print([p for p in glob.glob('temp/**', recursive=True)
       if os.path.isfile(p)])
# ['temp/[x].txt', 'temp/aaa.text', 'temp/dir/sub_dir1/98.txt', 'temp/dir/sub_dir1/ccc.text', 'temp/dir/987.text', 'temp/dir/bbb.txt', 'temp/dir/sub_dir2/ddd.text', 'temp/1.txt', 'temp/12.text', 'temp/123.txt']

print([os.path.basename(p) for p in glob.glob('temp/**', recursive=True)
       if os.path.isfile(p)])
# ['[x].txt', 'aaa.text', '98.txt', 'ccc.text', '987.text', 'bbb.txt', 'ddd.text', '1.txt', '12.text', '123.txt']

print(glob.glob('temp/**/', recursive=True))
# ['temp/', 'temp/dir/', 'temp/dir/sub_dir1/', 'temp/dir/sub_dir2/']

print(os.path.join('temp', '**' + os.sep))
# temp/**/

print(glob.glob(os.path.join('temp', '**' + os.sep), recursive=True))
# ['temp/', 'temp/dir/', 'temp/dir/sub_dir1/', 'temp/dir/sub_dir2/']

print([os.path.basename(p.rstrip(os.sep)) for p
       in glob.glob(os.path.join('temp', '**' + os.sep), recursive=True)])
# ['temp', 'dir', 'sub_dir1', 'sub_dir2']

print([p for p in glob.glob('temp/**', recursive=True)
       if re.search('\d+\.txt', p)])
# ['temp/dir/sub_dir1/98.txt', 'temp/1.txt', 'temp/123.txt']

print([p for p in glob.glob('temp/**', recursive=True)
       if re.search('/\D{3}\.(txt|text)', p)])
# ['temp/[x].txt', 'temp/aaa.text', 'temp/dir/sub_dir1/ccc.text', 'temp/dir/bbb.txt', 'temp/dir/sub_dir2/ddd.text']

print(type(glob.iglob('temp/*.txt')))
# <class 'generator'>

for p in glob.iglob('temp/*.txt'):
    print(p)
# temp/[x].txt
# temp/1.txt
# temp/123.txt

import shutil

shutil.rmtree('temp')
os.mkdir('temp')
