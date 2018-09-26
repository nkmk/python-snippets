import os
import shutil

os.makedirs('temp/dir/', exist_ok=True)

with open('file.txt', 'w') as f:
    f.write('')

print(os.listdir('temp/'))
# ['dir', 'test.txt']

target_dir = 'temp'

shutil.rmtree(target_dir)
os.mkdir(target_dir)

print(os.listdir('temp/'))
# []
