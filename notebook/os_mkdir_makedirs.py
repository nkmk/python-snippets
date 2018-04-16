import os

new_dir_path = 'data/temp/new-dir'

os.mkdir(new_dir_path)

# os.mkdir(new_dir_path)
# FileExistsError: [Errno 17] File exists: 'data/temp/new-dir/'

new_dir_path_recursive = 'data/temp/new-dir2/new-sub-dir'

# os.mkdir(new_dir_path_recursive)
# FileNotFoundError: [Errno 2] No such file or directory: 'data/temp/new-dir2/new-sub-dir'

new_dir_path_recursive = 'data/temp/new-dir2/new-sub-dir'

os.makedirs(new_dir_path_recursive)

# os.makedirs(new_dir_path_recursive)
# FileExistsError: [Errno 17] File exists: 'data/temp/new-dir2/new-sub-dir'

os.makedirs(new_dir_path_recursive, exist_ok=True)

try:
    os.makedirs(new_dir_path_recursive)
except FileExistsError:
    pass

def my_makedirs(path):
    if not os.path.isdir(path):
        os.makedirs(path)

my_makedirs(new_dir_path_recursive)
