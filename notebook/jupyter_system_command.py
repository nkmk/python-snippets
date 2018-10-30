!date
# 2018年 10月30日 火曜日 22時26分11秒 JST

!echo Hello
# Hello

!ls array*
# array_example.ipynb array_example.py

!ls -l array*
# -rw-r--r--  1 mbp  staff  1995  4 15  2018 array_example.ipynb
# -rw-r--r--  1 mbp  staff   358  4 15  2018 array_example.py

!mkdir test_dir

!rmdir test_dir

output = !date

print(output)
# ['2018年 10月30日 火曜日 22時26分12秒 JST']

print(type(output))
# <class 'IPython.utils.text.SList'>

print(isinstance(output, list))
# True

print(len(output))
# 1

print(output[0])
# 2018年 10月30日 火曜日 22時26分12秒 JST

print(type(output[0]))
# <class 'str'>

output = !ls -l array*

print(output)
# ['-rw-r--r--  1 mbp  staff  1995  4 15  2018 array_example.ipynb', '-rw-r--r--  1 mbp  staff   358  4 15  2018 array_example.py']

print(len(output))
# 2

print(output[0])
# -rw-r--r--  1 mbp  staff  1995  4 15  2018 array_example.ipynb

print(output[1])
# -rw-r--r--  1 mbp  staff   358  4 15  2018 array_example.py

print(output.n)
# -rw-r--r--  1 mbp  staff  1995  4 15  2018 array_example.ipynb
# -rw-r--r--  1 mbp  staff   358  4 15  2018 array_example.py

print(type(output.n))
# <class 'str'>

print('\n'.join(output))
# -rw-r--r--  1 mbp  staff  1995  4 15  2018 array_example.ipynb
# -rw-r--r--  1 mbp  staff   358  4 15  2018 array_example.py

!ls array*
# array_example.ipynb array_example.py

output = !ls array*

print(output)
# ['array_example.ipynb', 'array_example.py']

print(len(output))
# 2

!ls array*
# array_example.ipynb array_example.py

!ls array* | head
# array_example.ipynb
# array_example.py

!ls -C array*
# array_example.ipynb array_example.py

output = !ls -C array*

print(output)
# ['array_example.ipynb\tarray_example.py']

print(len(output))
# 1

print(output[0])
# array_example.ipynb	array_example.py
