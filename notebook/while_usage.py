i = 0

while i < 3:
    print(i)
    i += 1
# 0
# 1
# 2

i = 0

while i < 3:
    print(i)
    if i == 1:
        print('!!BREAK!!')
        break
    i += 1
# 0
# 1
# !!BREAK!!

i = 0

while i < 3:
    if i == 1:
        print('!!CONTINUE!!')
        i += 1
        continue
    print(i)
    i += 1
# 0
# !!CONTINUE!!
# 2

i = 0

while i < 3:
    print(i)
    i += 1
else:
    print('!!FINISH!!')
# 0
# 1
# 2
# !!FINISH!!

i = 0

while i < 3:
    print(i)
    if i == 1:
        print('!!BREAK!!')
        break
    i += 1
else:
    print('!!FINISH!!')
# 0
# 1
# !!BREAK!!

i = 0

while i < 3:
    if i == 1:
        print('!!SKIP!!')
        i += 1
        continue
    print(i)
    i += 1
else:
    print('!!FINISH!!')
# 0
# !!SKIP!!
# 2
# !!FINISH!!

import time

start = time.time()

while True:
    time.sleep(1)
    print('processing...')
    if time.time() - start > 5:
        print('!!BREAK!!')
        break
# processing...
# processing...
# processing...
# processing...
# processing...
# !!BREAK!!

start = time.time()

while 1:
    time.sleep(1)
    print('processing...')
    if time.time() - start > 5:
        print('!!BREAK!!')
        break
# processing...
# processing...
# processing...
# processing...
# processing...
# !!BREAK!!

start = time.time()

while time.time() - start <= 5:
    time.sleep(1)
    print('processing...')
else:
    print('!!FINISH!!')
# processing...
# processing...
# processing...
# processing...
# processing...
# !!FINISH!!
