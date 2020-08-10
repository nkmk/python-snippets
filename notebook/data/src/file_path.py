import os

print('getcwd:      ', os.getcwd())
print('__file__:    ', __file__)
print('basename:    ', os.path.basename(__file__))
print('dirname:     ', os.path.dirname(__file__))
print('abspath:     ', os.path.abspath(__file__))
print('abs dirname: ', os.path.dirname(os.path.abspath(__file__)))

print()
print('[set target path 1]')
target_path_1 = os.path.join(os.path.dirname(__file__), 'target_1.txt')

print('target_path_1: ', target_path_1)

print('read target file:')
with open(target_path_1) as f:
    print(f.read())

print()
print('[set target path 2]')
target_path_2 = os.path.join(os.path.dirname(__file__), '../dst/target_2.txt')

print('target_path_2: ', target_path_2)
print('normalize    : ', os.path.normpath(target_path_2))

print('read target file:')
with open(target_path_2) as f:
    print(f.read())

print()
print('[change directory]')
os.chdir(os.path.dirname(os.path.abspath(__file__)))
print('getcwd:      ', os.getcwd())

print()
print('[set target path 1 (after chdir)]')
target_path_1 = 'target_1.txt'

print('target_path_1: ', target_path_1)

print('read target file:')
with open(target_path_1) as f:
    print(f.read())

print()
print('[set target path 2 (after chdir)]')
target_path_2 = '../dst/target_2.txt'

print('target_path_2: ', target_path_2)

print('read target file:')
with open(target_path_2) as f:
    print(f.read())
