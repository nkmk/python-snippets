import pathlib
import os

os.makedirs('temp', exist_ok=True)

p_empty = pathlib.Path('temp/empty_file.txt')

print(p_empty)
# temp/empty_file.txt

print(type(p_empty))
# <class 'pathlib.PosixPath'>

print(p_empty.exists())
# False

p_empty.touch()

print(p_empty.exists())
# True

p_empty.touch()

# p_empty.touch(exist_ok=False)
# FileExistsError: [Errno 17] File exists: 'temp/empty_file.txt'

# pathlib.Path('temp/new_dir/empty_file.txt').touch()
# FileNotFoundError: [Errno 2] No such file or directory: 'temp/new_dir/empty_file.txt'

p_empty_new = pathlib.Path('temp/new_dir/empty_file.txt')
p_empty_new.parent.mkdir(parents=True, exist_ok=True)
p_empty_new.touch()

pathlib.Path('temp/empty_file2.txt').touch()

p_new = pathlib.Path('temp/new_file.txt')

print(p_new.exists())
# False

with p_new.open(mode='w') as f:
    f.write('line 1\nline 2\nline 3')

with p_new.open() as f:
    print(f.read())
# line 1
# line 2
# line 3

s = p_new.read_text()

print(s)
# line 1
# line 2
# line 3

print(type(s))
# <class 'str'>

i = p_new.write_text('new text')

print(i)
# 8

print(p_new.read_text())
# new text

p_new2 = pathlib.Path('temp/new_file2.txt')

print(p_new2.exists())
# False

# print(p_new2.read_text())
# FileNotFoundError: [Errno 2] No such file or directory: 'temp/new_file2.txt'

print(p_new2.write_text('new text2'))
# 9

print(p_new2.read_text())
# new text2

# print(pathlib.Path('temp/new_dir2/new_file.txt').write_text('new_text'))
# FileNotFoundError: [Errno 2] No such file or directory: 'temp/new_dir2/new_file.txt'

p_text_new = pathlib.Path('temp/new_dir2/new_file.txt')
p_text_new.parent.mkdir(parents=True, exist_ok=True)
print(p_text_new.write_text('new_text'))
# 8

print(p_text_new.read_text())
# new_text

print(pathlib.Path('temp/new_file3.txt').write_text('new_text3'))
# 9

print(pathlib.Path('temp/new_file3.txt').read_text())
# new_text3

p_empty = pathlib.Path('temp/empty_file.txt')

print(p_empty.exists())
# True

p_empty.unlink()

print(p_empty.exists())
# False

# p_empty.unlink()
# FileNotFoundError: [Errno 2] No such file or directory: 'temp/empty_file.txt'

p_dir = pathlib.Path('temp/')

# p_dir.unlink()
# PermissionError: [Errno 1] Operation not permitted: 'temp'

for p in p_dir.iterdir():
    if p.is_file():
        p.unlink()

[p.unlink() for p in p_dir.iterdir() if p.is_file()]
# []

import shutil

shutil.rmtree('temp')
