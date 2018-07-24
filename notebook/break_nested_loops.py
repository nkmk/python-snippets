l1 = [1, 2, 3]
l2 = [10, 20, 30]

for i in l1:
    for j in l2:
        print(i, j)
# 1 10
# 1 20
# 1 30
# 2 10
# 2 20
# 2 30
# 3 10
# 3 20
# 3 30

for i in l1:
    for j in l2:
        print(i, j)
        if i == 2 and j == 20 :
            print('BREAK')
            break
# 1 10
# 1 20
# 1 30
# 2 10
# 2 20
# BREAK
# 3 10
# 3 20
# 3 30

for i in l1:
    for j in l2:
        print(i, j)
        if i == 2 and j == 20:
            print('BREAK')
            break
    else:
        continue
    break
# 1 10
# 1 20
# 1 30
# 2 10
# 2 20
# BREAK

for i in l1:
    print('Start outer loop')

    for j in l2:
        print('--', i, j)
        if i == 2 and j == 20:
            print('-- BREAK inner loop')
            break
    else:
        print('-- Finish inner loop without BREAK')
        continue

    print('BREAK outer loop')
    break
# Start outer loop
# -- 1 10
# -- 1 20
# -- 1 30
# -- Finish inner loop without BREAK
# Start outer loop
# -- 2 10
# -- 2 20
# -- BREAK inner loop
# BREAK outer loop

l1 = [1, 2, 3]
l2 = [10, 20, 30]
l3 = [100, 200, 300]

for i in l1:
    for j in l2:
        for k in l3:
            print(i, j, k)
            if i == 2 and j == 20 and k == 200:
                print('BREAK')
                break
        else:
            continue
        break
    else:
        continue
    break
# 1 10 100
# 1 10 200
# 1 10 300
# 1 20 100
# 1 20 200
# 1 20 300
# 1 30 100
# 1 30 200
# 1 30 300
# 2 10 100
# 2 10 200
# 2 10 300
# 2 20 100
# 2 20 200
# BREAK

l1 = [1, 2, 3]
l2 = [10, 20, 30]

flag = False
for i in l1:
    for j in l2:
        print(i, j)
        if i == 2 and j == 20:
            flag = True
            print('BREAK')
            break
    if flag:
        break
# 1 10
# 1 20
# 1 30
# 2 10
# 2 20
# BREAK

l1 = [1, 2, 3]
l2 = [10, 20, 30]
l3 = [100, 200, 300]

flag = False
for i in l1:
    for j in l2:
        for k in l3:
            print(i, j, k)
            if i == 2 and j == 20 and k == 200:
                flag = True
                print('BREAK')
                break
        if flag:
            break
    if flag:
        break
# 1 10 100
# 1 10 200
# 1 10 300
# 1 20 100
# 1 20 200
# 1 20 300
# 1 30 100
# 1 30 200
# 1 30 300
# 2 10 100
# 2 10 200
# 2 10 300
# 2 20 100
# 2 20 200
# BREAK
