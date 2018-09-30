import os
import shutil


def glob_example_detail():
    if os.path.exists('temp'):
        shutil.rmtree('temp')
    
    os.makedirs('temp/dir/', exist_ok=True)
    os.makedirs('temp/dir/sub_dir1/', exist_ok=True)
    os.makedirs('temp/dir/sub_dir2/', exist_ok=True)
    
    with open('temp/aaa.text', 'w'): pass
    with open('temp/1.txt', 'w'): pass
    with open('temp/12.text', 'w'): pass
    with open('temp/123.txt', 'w'): pass
    with open('temp/[x].txt', 'w'): pass
    
    with open('temp/dir/bbb.txt', 'w'): pass
    with open('temp/dir/987.text', 'w'): pass

    with open('temp/dir/sub_dir1/98.txt', 'w'): pass
    with open('temp/dir/sub_dir1/ccc.text', 'w'): pass
    
    with open('temp/dir/sub_dir2/ddd.text', 'w'): pass


def pathlib_basic():
    if os.path.exists('temp'):
        shutil.rmtree('temp')
    
    os.makedirs('temp/dir/sub_dir/', exist_ok=True)

    with open('temp/file.txt', 'w'): pass
    with open('temp/dir/sub_dir/file2.txt', 'w'): pass
