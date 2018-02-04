import os

print(os.path.getsize('data/src/lena_square.png'))
# 473831

def get_dir_size(path='.'):
    total = 0
    with os.scandir(path) as it:
        for entry in it:
            if entry.is_file():
                total += entry.stat().st_size
            elif entry.is_dir():
                total += get_dir_size(entry.path)
    return total

print(get_dir_size('data/src'))
# 56130856

def get_size(path='.'):
    if os.path.isfile(path):
        return os.path.getsize(path)
    elif os.path.isdir(path):
        return get_dir_size(path)

print(get_size('data/src'))
# 56130856

print(get_size('data/src/lena_square.png'))
# 473831

def get_dir_size_old(path='.'):
    total = 0
    for p in os.listdir(path):
        full_path = os.path.join(path, p)
        if os.path.isfile(full_path):
            total += os.path.getsize(full_path)
        elif os.path.isdir(full_path):
            total += get_dir_size_old(full_path)
    return total

print(get_dir_size_old('data/src'))
# 56130856

def get_size_old(path='.'):
    if os.path.isfile(path):
        return os.path.getsize(path)
    elif os.path.isdir(path):
        return get_dir_size_old(path)

print(get_size_old('data/src'))
# 56130856

print(get_size_old('data/src/lena_square.png'))
# 473831
