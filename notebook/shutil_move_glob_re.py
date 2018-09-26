import shutil
import glob
import re
import os

def move_glob_re(dst_path, pattern, pathname, recursive=True):
    for p in glob.glob(pathname, recursive=recursive):
        if re.search(pattern, p):
            shutil.move(p, dst_path)

os.mkdir('temp/dir2')

move_glob_re('temp/dir2', '\d+.txt', 'temp/**')
