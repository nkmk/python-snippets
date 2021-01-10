import os
import pathlib
import pprint
import joblib

src_dir = 'data/temp/joblib/src_file'

os.makedirs(src_dir, exist_ok=True)

for i in range(10):
    pathlib.Path(src_dir).joinpath(f'file{i:05}.txt').write_text(f'This is file{i:05}')

def func_write(i):
    pathlib.Path(src_dir).joinpath(f'file{i:05}.txt').write_text(f'This is file{i:05}')

_ = joblib.Parallel(n_jobs=-1)(joblib.delayed(func_write)(i) for i in range(10))

first_lines = []
for p in pathlib.Path(src_dir).glob('*.txt'):
    with p.open() as f:
        first_lines.append((p.name, f.readline()))

pprint.pprint(sorted(first_lines))
# [('file00000.txt', 'This is file00000'),
#  ('file00001.txt', 'This is file00001'),
#  ('file00002.txt', 'This is file00002'),
#  ('file00003.txt', 'This is file00003'),
#  ('file00004.txt', 'This is file00004'),
#  ('file00005.txt', 'This is file00005'),
#  ('file00006.txt', 'This is file00006'),
#  ('file00007.txt', 'This is file00007'),
#  ('file00008.txt', 'This is file00008'),
#  ('file00009.txt', 'This is file00009')]

def func_read_first_line(p):
    with p.open() as f:
        return p.name, f.readline()

first_lines = joblib.Parallel(n_jobs=-1)(
    joblib.delayed(func_read_first_line)(p) for p in pathlib.Path(src_dir).glob('*.txt')
)

pprint.pprint(sorted(first_lines))
# [('file00000.txt', 'This is file00000'),
#  ('file00001.txt', 'This is file00001'),
#  ('file00002.txt', 'This is file00002'),
#  ('file00003.txt', 'This is file00003'),
#  ('file00004.txt', 'This is file00004'),
#  ('file00005.txt', 'This is file00005'),
#  ('file00006.txt', 'This is file00006'),
#  ('file00007.txt', 'This is file00007'),
#  ('file00008.txt', 'This is file00008'),
#  ('file00009.txt', 'This is file00009')]
