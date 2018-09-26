import os

os.makedirs('temp/dir1/dir2/dir3/', exist_ok=True)

with open('temp/file.txt', 'w') as f:
    f.write('')

print(os.listdir('temp/'))
# ['file.txt', 'dir1']

os.removedirs('temp/dir1/dir2/dir3/')

print(os.listdir('temp/'))
# ['file.txt']

os.remove('temp/file.txt')
