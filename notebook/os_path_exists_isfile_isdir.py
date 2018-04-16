import os

filepath = './data/temp/dir/file.txt'
dirpath = './data/temp/dir'

print(os.path.exists(filepath))
# True

print(os.path.exists(dirpath))
# True

print(os.path.isfile(filepath))
# True

print(os.path.isfile(dirpath))
# False

print(os.path.isdir(filepath))
# False

print(os.path.isdir(dirpath))
# True

dirpath_with_sep = './data/temp/dir/'

print(os.path.isfile(dirpath_with_sep))
# False

print(os.path.isdir(dirpath_with_sep))
# True
