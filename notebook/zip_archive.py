import os
from pathlib import Path

os.chdir('data/temp')

Path('another_file.txt').touch()

p = Path('dir_zip')
p.joinpath('dir_sub').mkdir(parents=True, exist_ok=True)
p.joinpath('file.txt').write_text('file in dir_zip')
p.joinpath('dir_sub/file_sub.txt').write_text('file in dir_zip/dir_sub')
# 23

import shutil

shutil.make_archive('archive_shutil', format='zip', root_dir='dir_zip')
# '/Users/mbp/Documents/my-project/python-snippets/notebook/data/temp/archive_shutil.zip'

shutil.make_archive('archive_shutil_base', format='zip',
                    root_dir='.', base_dir='dir_zip')
# '/Users/mbp/Documents/my-project/python-snippets/notebook/data/temp/archive_shutil_base.zip'

shutil.unpack_archive('archive_shutil.zip', 'dir_out')

shutil.unpack_archive('archive_shutil_base.zip', 'dir_out_base')

import zipfile

with zipfile.ZipFile('archive_zipfile.zip', 'w',
                     compression=zipfile.ZIP_DEFLATED,
                     compresslevel=9) as zf:
    zf.write('dir_zip/file.txt', arcname='file.txt')
    zf.write('dir_zip/dir_sub/file_sub.txt', arcname='dir_sub/file_sub.txt')

with zipfile.ZipFile('archive_zipfile.zip', 'a') as zf:
    zf.write('another_file.txt')

with zipfile.ZipFile('archive_zipfile.zip', 'a') as zf:
    with zf.open('dir_sub/new_file.txt', 'w') as f:
        f.write(b'text in new file')

print(type(b'text'))
# <class 'bytes'>

print(type('text'.encode('utf-8')))
# <class 'bytes'>

with zipfile.ZipFile('archive_zipfile.zip') as zf:
    print(zf.namelist())
# ['file.txt', 'dir_sub/file_sub.txt', 'another_file.txt', 'dir_sub/new_file.txt']

with zipfile.ZipFile('archive_shutil.zip') as zf:
    print(zf.namelist())
# ['dir_sub/', 'file.txt', 'dir_sub/file_sub.txt']

with zipfile.ZipFile('archive_shutil.zip') as zf:
    print([x for x in zf.namelist() if not x.endswith('/')])
# ['file.txt', 'dir_sub/file_sub.txt']

with zipfile.ZipFile('archive_zipfile.zip') as zf:
    zf.extract('file.txt', 'dir_out_extract')
    zf.extract('dir_sub/file_sub.txt', 'dir_out_extract')

with zipfile.ZipFile('archive_zipfile.zip') as zf:
    zf.extractall('dir_out_extractall')

with zipfile.ZipFile('archive_zipfile.zip') as zf:
    with zf.open('dir_sub/new_file.txt') as f:
        b = f.read()

print(b)
# b'text in new file'

print(type(b))
# <class 'bytes'>

s = b.decode('utf-8')
print(s)
# text in new file

print(type(s))
# <class 'str'>

import pyzipper

with pyzipper.AESZipFile('archive_with_pass.zip', 'w',
                         encryption=pyzipper.WZ_AES) as zf:
    zf.setpassword(b'password')
    zf.write('dir_zip/file.txt', arcname='file.txt')
    zf.write('dir_zip/dir_sub/file_sub.txt', arcname='dir_sub/file_sub.txt')

with pyzipper.AESZipFile('archive_with_pass.zip') as zf:
    zf.setpassword(b'password')
    zf.extractall('dir_out_pyzipper')

# with pyzipper.AESZipFile('archive_with_pass.zip') as zf:
#     zf.setpassword(b'wrong_password')
#     zf.extractall('dir_out_pass')
# RuntimeError: Bad password for file 'file.txt'

# shutil.unpack_archive('archive_with_pass.zip', 'dir_out_pass')
# RuntimeError: File 'file.txt' is encrypted, password required for extraction

# with zipfile.ZipFile('archive_with_pass.zip') as zf:
#     zf.setpassword(b'password')
#     zf.extractall('dir_out_pass')
# NotImplementedError: That compression method is not supported

import subprocess

subprocess.run(['7z', 'x', 'archive_with_pass.zip', '-ppassword', '-odir_out_7z'])
# CompletedProcess(args=['7z', 'x', 'archive_with_pass.zip', '-ppassword', '-odir_out_7z'], returncode=0)
