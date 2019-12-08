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

basename_without_ext = os.path.splitext(os.path.basename(filepath))[0]
print(basename_without_ext)
# filename

filepath_tar_gz = './dir/subdir/filename.tar.gz'

print(os.path.splitext(os.path.basename(filepath_tar_gz))[0])
# filename.tar

print(os.path.basename(filepath_tar_gz).split('.', 1)[0])
# filename

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
# True

print(os.path.split(filepath)[1] == os.path.basename(filepath))
# True

dirname, basename = os.path.split(filepath)
print(dirname)
# ./dir/subdir

print(basename)
# filename.ext

dirpath_without_sep = './dir/subdir'
print(os.path.split(dirpath_without_sep))
# ('./dir', 'subdir')

print(os.path.basename(dirpath_without_sep))
# subdir

dirpath_with_sep = './dir/subdir/'
print(os.path.split(dirpath_with_sep))
# ('./dir/subdir', '')

print(os.path.basename(os.path.dirname(dirpath_with_sep)))
# subdir

root_ext_pair = os.path.splitext(filepath)
print(root_ext_pair)
# ('./dir/subdir/filename', '.ext')

print(type(root_ext_pair))
# <class 'tuple'>

root, ext = os.path.splitext(filepath)
print(root)
# ./dir/subdir/filename

print(ext)
# .ext

path = root + ext
print(path)
# ./dir/subdir/filename.ext

other_ext_filepath = os.path.splitext(filepath)[0] + '.jpg'
print(other_ext_filepath)
# ./dir/subdir/filename.jpg

ext_without_dot = os.path.splitext(filepath)[1][1:]
print(ext_without_dot)
# ext

print(os.path.splitext(filepath_tar_gz))
# ('./dir/subdir/filename.tar', '.gz')

print(filepath_tar_gz.split('.', 1))
# ['', '/dir/subdir/filename.tar.gz']

dirname, basename = os.path.split(filepath_tar_gz)
basename_without_ext, ext = basename.split('.', 1)
path_without_ext = os.path.join(dirname, basename_without_ext)
print(path_without_ext)
# ./dir/subdir/filename

print(ext)
# tar.gz

ext_with_dot = '.' + ext
print(ext_with_dot)
# .tar.gz

path = os.path.join('dir', 'subdir', 'filename.ext')
print(path)
# dir/subdir/filename.ext

other_filepath = os.path.join(os.path.dirname(filepath), 'other_file.ext')
print(other_filepath)
# ./dir/subdir/other_file.ext
