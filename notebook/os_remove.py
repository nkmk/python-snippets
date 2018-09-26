import os

os.makedirs('temp/', exist_ok=True)

with open('temp/file.txt', 'w') as f:
    f.write('')

print(os.listdir('temp'))
# ['file.txt']

os.remove('temp/file.txt')

print(os.listdir('temp'))
# []

# os.remove('temp/')
# PermissionError: [Errno 1] Operation not permitted: 'temp/'
