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

new_path = shutil.move('temp/dir1/file.txt', 'temp/dir2/')

print(new_path)
# temp/dir2/file.txt

print(os.listdir('temp/dir1/'))
# ['dir']

print(os.listdir('temp/dir2/'))
# ['file.txt']

# new_path = shutil.move('temp/dir2/file.txt', 'temp/dir1/new_dir/')
# FileNotFoundError: [Errno 2] No such file or directory: 'temp/dir1/new_dir/'

new_path = shutil.move('temp/dir1/dir/', 'temp/dir2/')

print(new_path)
# temp/dir2/dir

print(os.listdir('temp/dir1/'))
# []

print(os.listdir('temp/dir2/'))
# ['file.txt', 'dir']

new_path = shutil.move('temp/dir2/file.txt', 'temp/dir1/file_new.txt')

print(new_path)
# temp/dir1/file_new.txt

print(os.listdir('temp/dir1/'))
# ['file_new.txt']

print(os.listdir('temp/dir2/'))
# ['dir']

# new_path = shutil.move('temp/dir1/file_new.txt', 'temp/dir2/dir_new/file_new.txt')
# FileNotFoundError: [Errno 2] No such file or directory: 'temp/dir2/dir_new/file_new.txt'

new_path = shutil.move('temp/dir2/dir/', 'temp/dir1/dir_new/')

print(new_path)
# temp/dir1/dir_new/

print(os.listdir('temp/dir1/'))
# ['dir_new', 'file_new.txt']

print(os.listdir('temp/dir2/'))
# []

new_path = shutil.move('temp/dir1/dir_new', 'temp/dir2/dir_new/dir_new2/')

print(new_path)
# temp/dir2/dir_new/dir_new2/

print(os.listdir('temp/dir1/'))
# ['file_new.txt']

print(os.listdir('temp/dir2/'))
# ['dir_new']

print(os.listdir('temp/dir2/dir_new/'))
# ['dir_new2']

with open('temp/dir2/file_other.txt', 'w') as f:
    f.write('other')

new_path = shutil.move('temp/dir1/file_new.txt', 'temp/dir2/file_other.txt')

print(new_path)
# temp/dir2/file_other.txt

print(os.listdir('temp/dir1/'))
# []

print(os.listdir('temp/dir2/'))
# ['file_other.txt', 'dir_new']

with open('temp/dir2/file_other.txt') as f:
    print(f.read())
# original

shutil.rmtree('temp/dir1/')
shutil.rmtree('temp/dir2/')
