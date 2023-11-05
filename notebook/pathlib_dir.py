from pathlib import Path

p = Path('temp')
print(p)
# temp

print(type(p))
# <class 'pathlib.PosixPath'>

print(p.exists())
# False

p.mkdir()

print(p.exists())
# True

print(p.is_dir())
# True

Path('temp/dir').mkdir()

print(Path('temp/dir').is_dir())
# True

# Path('temp/dir/sub_dir/sub_dir2').mkdir()
# FileNotFoundError: [Errno 2] No such file or directory: 'temp/dir/sub_dir/sub_dir2'

Path('temp/dir/sub_dir/sub_dir2').mkdir(parents=True)

print(Path('temp/dir/sub_dir/sub_dir2').is_dir())
# True

# Path('temp/dir').mkdir()
# FileExistsError: [Errno 17] File exists: 'temp/dir'

Path('temp/dir').mkdir(exist_ok=True)

Path('temp/dir/file').touch()

print(Path('temp/dir/file').is_file())
# True

# Path('temp/dir/file').mkdir(exist_ok=True)
# FileExistsError: [Errno 17] File exists: 'temp/dir/file'

p_sub_dir = Path('temp/dir/sub_dir/sub_dir2')

print(p_sub_dir.is_dir())
# True

p_sub_dir.rmdir()

print(p_sub_dir.exists())
# False

p = Path('temp')

# p.rmdir()
# OSError: [Errno 66] Directory not empty: 'temp'

import shutil

shutil.rmtree(p)

print(p.exists())
# False
