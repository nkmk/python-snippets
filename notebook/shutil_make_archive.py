import shutil

shutil.make_archive('data/temp/new_shutil', 'zip', root_dir='data/temp/dir')

shutil.make_archive('data/temp/new_shutil_sub', 'zip', root_dir='data/temp/dir', base_dir='dir_sub')
