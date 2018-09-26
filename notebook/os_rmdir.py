import os

os.makedirs('temp/dir_empty/', exist_ok=True)

print(os.listdir('temp/'))
# ['dir_empty']

os.rmdir('temp/dir_empty/')

print(os.listdir('temp/'))
# []

os.makedirs('temp/dir_not_empty/', exist_ok=True)

with open('temp/dir_not_empty/file.txt', 'w') as f:
    f.write('')

# os.rmdir('temp/dir_not_empty/')
# OSError: [Errno 66] Directory not empty: 'temp/dir_not_empty/'

try:
    os.rmdir('temp/dir_not_empty/')
except OSError as e:
    pass

import shutil

shutil.rmtree('temp/dir_not_empty/')

print(os.listdir('temp/'))
# []
