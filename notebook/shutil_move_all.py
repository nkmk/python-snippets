import shutil
import os

os.makedirs('temp/dir1/dir', exist_ok=True)
os.makedirs('temp/dir2', exist_ok=True)

with open('temp/dir1/file.txt', 'w') as f:
    f.write('original')

print(os.listdir('temp/dir1/'))
# ['file.txt', 'dir']

print(os.listdir('temp/dir2/'))
# []

src_dir = 'temp/dir1/'
dst_dir = 'temp/dir2/'

for p in os.listdir(src_dir):
    shutil.move(os.path.join(src_dir, p), dst_dir)

print(os.listdir(src_dir))
# []

print(os.listdir(dst_dir))
# ['file.txt', 'dir']

shutil.rmtree('temp/dir1/')
shutil.rmtree('temp/dir2/')
