import shutil
import glob
import os

def move_glob(dst_path, pathname, recursive=True):
    for p in glob.glob(pathname, recursive=recursive):
        shutil.move(p, dst_path)

os.mkdir('temp/dir2')

move_glob('temp/dir2', 'temp/**/*.txt')
