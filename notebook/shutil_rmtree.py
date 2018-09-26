import shutil
import os

os.makedirs('temp/dir/sub_dir/', exist_ok=True)

with open('temp/dir/file.txt', 'w') as f:
    f.write('')

print(os.listdir('temp/'))
# ['dir']

print(os.listdir('temp/dir/'))
# ['file.txt', 'sub_dir']

# shutil.rmtree('temp/dir/file.txt')
# NotADirectoryError: [Errno 20] Not a directory: 'temp/dir/file.txt'

shutil.rmtree('temp/dir/')

print(os.listdir('temp/'))
# []
