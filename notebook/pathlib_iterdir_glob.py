import util_make_files

util_make_files.glob_example_detail()

import pathlib
import glob
import re
import pprint

p_temp = pathlib.Path('temp')

print(p_temp)
# temp

print(type(p_temp))
# <class 'pathlib.PosixPath'>

print(type(p_temp.iterdir()))
# <class 'generator'>

pprint.pprint(list(p_temp.iterdir()))
# [PosixPath('temp/[x].txt'),
#  PosixPath('temp/aaa.text'),
#  PosixPath('temp/dir'),
#  PosixPath('temp/1.txt'),
#  PosixPath('temp/12.text'),
#  PosixPath('temp/123.txt')]

# print(list(pathlib.Path('temp/1.txt').iterdir()))
# NotADirectoryError: [Errno 20] Not a directory: 'temp/1.txt'

p_temp = pathlib.Path('temp')

print(type(p_temp.glob('**/*.txt')))
# <class 'generator'>

pprint.pprint(list(p_temp.glob('**/*.txt')))
# [PosixPath('temp/[x].txt'),
#  PosixPath('temp/1.txt'),
#  PosixPath('temp/123.txt'),
#  PosixPath('temp/dir/bbb.txt'),
#  PosixPath('temp/dir/sub_dir1/98.txt')]

pprint.pprint(list(p_temp.glob('*')))
# [PosixPath('temp/[x].txt'),
#  PosixPath('temp/aaa.text'),
#  PosixPath('temp/dir'),
#  PosixPath('temp/1.txt'),
#  PosixPath('temp/12.text'),
#  PosixPath('temp/123.txt')]

pprint.pprint(list(p_temp.glob('dir/*/*.text')))
# [PosixPath('temp/dir/sub_dir1/ccc.text'),
#  PosixPath('temp/dir/sub_dir2/ddd.text')]

pprint.pprint(list(p_temp.glob('???.*')))
# [PosixPath('temp/[x].txt'),
#  PosixPath('temp/aaa.text'),
#  PosixPath('temp/123.txt')]

pprint.pprint(list(p_temp.glob('[a-z][a-z][a-z].*')))
# [PosixPath('temp/aaa.text')]

pprint.pprint(glob.glob('temp/**', recursive=True))
# ['temp/',
#  'temp/[x].txt',
#  'temp/aaa.text',
#  'temp/dir',
#  'temp/dir/sub_dir1',
#  'temp/dir/sub_dir1/98.txt',
#  'temp/dir/sub_dir1/ccc.text',
#  'temp/dir/987.text',
#  'temp/dir/bbb.txt',
#  'temp/dir/sub_dir2',
#  'temp/dir/sub_dir2/ddd.text',
#  'temp/1.txt',
#  'temp/12.text',
#  'temp/123.txt']

pprint.pprint(list(p_temp.glob('**')))
# [PosixPath('temp'),
#  PosixPath('temp/dir'),
#  PosixPath('temp/dir/sub_dir1'),
#  PosixPath('temp/dir/sub_dir2')]

pprint.pprint(list(p_temp.glob('**/*')))
# [PosixPath('temp/[x].txt'),
#  PosixPath('temp/aaa.text'),
#  PosixPath('temp/dir'),
#  PosixPath('temp/1.txt'),
#  PosixPath('temp/12.text'),
#  PosixPath('temp/123.txt'),
#  PosixPath('temp/dir/sub_dir1'),
#  PosixPath('temp/dir/987.text'),
#  PosixPath('temp/dir/bbb.txt'),
#  PosixPath('temp/dir/sub_dir2'),
#  PosixPath('temp/dir/sub_dir1/98.txt'),
#  PosixPath('temp/dir/sub_dir1/ccc.text'),
#  PosixPath('temp/dir/sub_dir2/ddd.text')]

pprint.pprint([p for p in p_temp.glob('**/*')
               if re.search('\d+\.txt', str(p))])
# [PosixPath('temp/1.txt'),
#  PosixPath('temp/123.txt'),
#  PosixPath('temp/dir/sub_dir1/98.txt')]

pprint.pprint([p for p in p_temp.glob('**/*')
               if re.search('/\D{3}\.(txt|text)', str(p))])
# [PosixPath('temp/[x].txt'),
#  PosixPath('temp/aaa.text'),
#  PosixPath('temp/dir/bbb.txt'),
#  PosixPath('temp/dir/sub_dir1/ccc.text'),
#  PosixPath('temp/dir/sub_dir2/ddd.text')]

pprint.pprint([p.resolve() for p in p_temp.iterdir()])
# [PosixPath('/Users/mbp/Documents/my-project/python-snippets/notebook/temp/[x].txt'),
#  PosixPath('/Users/mbp/Documents/my-project/python-snippets/notebook/temp/aaa.text'),
#  PosixPath('/Users/mbp/Documents/my-project/python-snippets/notebook/temp/dir'),
#  PosixPath('/Users/mbp/Documents/my-project/python-snippets/notebook/temp/1.txt'),
#  PosixPath('/Users/mbp/Documents/my-project/python-snippets/notebook/temp/12.text'),
#  PosixPath('/Users/mbp/Documents/my-project/python-snippets/notebook/temp/123.txt')]

pprint.pprint([str(p) for p in p_temp.iterdir()])
# ['temp/[x].txt',
#  'temp/aaa.text',
#  'temp/dir',
#  'temp/1.txt',
#  'temp/12.text',
#  'temp/123.txt']

pprint.pprint([p for p in p_temp.iterdir() if p.is_file()])
# [PosixPath('temp/[x].txt'),
#  PosixPath('temp/aaa.text'),
#  PosixPath('temp/1.txt'),
#  PosixPath('temp/12.text'),
#  PosixPath('temp/123.txt')]

pprint.pprint([p for p in p_temp.iterdir() if p.is_dir()])
# [PosixPath('temp/dir')]

pprint.pprint([p.name for p in p_temp.iterdir() if p.is_file()])
# ['[x].txt', 'aaa.text', '1.txt', '12.text', '123.txt']

pprint.pprint([p for p in p_temp.glob('**/*')
               if re.search('\d+\.txt', str(p))])
# [PosixPath('temp/1.txt'),
#  PosixPath('temp/123.txt'),
#  PosixPath('temp/dir/sub_dir1/98.txt')]

for p in p_temp.glob('**/*'):
    if re.search('\d+\.txt', str(p)) and p.is_file():
        p.unlink()

pprint.pprint([p for p in p_temp.glob('**/*')
               if re.search('\d+\.txt', str(p))])
# []

[p.unlink() for p in p_temp.glob('**/*') if re.search('\d+\.txt', str(p)) and p.is_file()]
# []

import shutil

shutil.rmtree('temp')
