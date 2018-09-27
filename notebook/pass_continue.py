for i in range(3):
    print(i)
    if i == 1:
        continue
        print('CONTINUE')
# 0
# 1
# 2

for i in range(3):
    print(i)
    if i == 1:
        pass
        print('PASS')
# 0
# 1
# PASS
# 2
