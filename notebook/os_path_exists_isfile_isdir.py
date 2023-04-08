import os

file_path = './data/temp/dir/file.txt'
dir_path = './data/temp/dir'
non_existent_path = './non_exist'

os.makedirs(dir_path, exist_ok=True)
with open(file_path, mode='w') as f:
    f.write('')

print(os.path.isfile(file_path))
# True

print(os.path.isfile(dir_path))
# False

print(os.path.isfile(non_existent_path))
# False

print(os.path.isdir(file_path))
# False

print(os.path.isdir(dir_path))
# True

print(os.path.isdir(non_existent_path))
# False

print(os.path.exists(file_path))
# True

print(os.path.exists(dir_path))
# True

print(os.path.exists(non_existent_path))
# False

dir_path_with_sep = './data/temp/dir/'

print(os.path.exists(dir_path_with_sep))
# True

print(os.path.isfile(dir_path_with_sep))
# False

print(os.path.isdir(dir_path_with_sep))
# True
