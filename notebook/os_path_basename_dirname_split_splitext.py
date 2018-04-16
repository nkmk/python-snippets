import os

filepath = './dir/subdir/filename.ext'

print(os.sep)
# /

print(os.sep is os.path.sep)
# True

basename = os.path.basename(filepath)

print(basename)
# filename.ext

print(type(basename))
# <class 'str'>

dirname = os.path.dirname(filepath)

print(dirname)
# ./dir/subdir

print(type(dirname))
# <class 'str'>

subdirname = os.path.basename(os.path.dirname(filepath))

print(subdirname)
# subdir

base_dir_pair = os.path.split(filepath)

print(base_dir_pair)
# ('./dir/subdir', 'filename.ext')

print(type(base_dir_pair))
# <class 'tuple'>

print(os.path.split(filepath)[0] == os.path.dirname(filepath))
print(os.path.split(filepath)[1] == os.path.basename(filepath))
# True
# True

dirname, basename = os.path.split(filepath)

print(dirname)
print(basename)
# ./dir/subdir
# filename.ext

dirpath_without_sep = '../dir/subdir'

print(os.path.split(dirpath_without_sep))
# ('../dir', 'subdir')

print(os.path.basename(dirpath_without_sep))
# subdir

dirpath_with_sep = '../dir/subdir/'

print(os.path.split(dirpath_with_sep))
# ('../dir/subdir', '')

print(os.path.basename(os.path.dirname(dirpath_with_sep)))
# subdir

root_ext_pair = os.path.splitext(filepath)

print(root_ext_pair)
# ('./dir/subdir/filename', '.ext')

print(type(root_ext_pair))
# <class 'tuple'>

root, ext = os.path.splitext(filepath)

path = root + ext

print(path)
# ./dir/subdir/filename.ext

other_ext_filepath = os.path.splitext(filepath)[0] + '.jpg'

print(other_ext_filepath)
# ./dir/subdir/filename.jpg

ext_without_period = os.path.splitext(filepath)[1][1:]

print(ext_without_period)
# ext

path = os.path.join('dir', 'subdir', 'filename.ext')
print(path)
# dir/subdir/filename.ext

other_filepath = os.path.join(os.path.dirname(filepath), 'other_file.ext')

print(other_filepath)
# ./dir/subdir/other_file.ext
