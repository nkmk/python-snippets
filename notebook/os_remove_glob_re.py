import os
import glob
import re

def remove_glob_re(pattern, pathname, recursive=True):
    for p in glob.glob(pathname, recursive=recursive):
        if os.path.isfile(p) and re.search(pattern, p):
            os.remove(p)

remove_glob_re('\d+.txt', 'temp/**')
