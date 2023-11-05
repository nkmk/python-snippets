from pathlib import Path

Path('temp').mkdir()

p_empty = Path('temp/empty_file.txt')
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

p_empty_new_dir = Path('temp/new_dir/empty_file.txt')

# p_empty_new_dir.touch()
# FileNotFoundError: [Errno 2] No such file or directory: 'temp/new_dir/empty_file.txt'

p_empty_new_dir.parent.mkdir(parents=True, exist_ok=True)
p_empty_new_dir.touch()

Path('temp/empty_file2.txt').touch()

p_new = Path('temp/new_file.txt')

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

p_new2 = Path('temp/new_file2.txt')

print(p_new2.exists())
# False

# print(p_new2.read_text())
# FileNotFoundError: [Errno 2] No such file or directory: 'temp/new_file2.txt'

print(p_new2.write_text('new text2'))
# 9

print(p_new2.read_text())
# new text2

p_text_new_dir = Path('temp/new_dir2/new_file.txt')

# print(p_text_new_dir.write_text('new_text'))
# FileNotFoundError: [Errno 2] No such file or directory: 'temp/new_dir2/new_file.txt'

p_text_new_dir.parent.mkdir(parents=True, exist_ok=True)
print(p_text_new_dir.write_text('new_text'))
# 8

print(p_text_new_dir.read_text())
# new_text

print(Path('temp/new_file3.txt').write_text('new_text3'))
# 9

print(Path('temp/new_file3.txt').read_text())
# new_text3

p_bin = Path('temp/new_file.bin')

print(p_bin.write_bytes(b'binary'))
# 6

print(p_bin.read_bytes())
# b'binary'

p_empty = Path('temp/empty_file.txt')

print(p_empty.exists())
# True

p_empty.unlink()

print(p_empty.exists())
# False

# p_empty.unlink()
# FileNotFoundError: [Errno 2] No such file or directory: 'temp/empty_file.txt'

p_empty.unlink(missing_ok=True)

p_dir = Path('temp/')

# p_dir.unlink()
# PermissionError: [Errno 1] Operation not permitted: 'temp'

for p in p_dir.iterdir():
    if p.is_file():
        p.unlink()

[p.unlink() for p in p_dir.iterdir() if p.is_file()]
# []

import shutil

shutil.rmtree('temp')
