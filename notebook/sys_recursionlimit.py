import sys
import resource

print(sys.getrecursionlimit())
# 1000

def recu_test(n):
    if n == 1:
        print('Finish')
        return
    recu_test(n - 1)

recu_test(950)
# Finish

# recu_test(1500)
# RecursionError: maximum recursion depth exceeded in comparison

# recu_test(995)
# RecursionError: maximum recursion depth exceeded while calling a Python object

sys.setrecursionlimit(2000)

print(sys.getrecursionlimit())
# 2000

recu_test(1500)
# Finish

sys.setrecursionlimit(4)
print(sys.getrecursionlimit())
# 4

# sys.setrecursionlimit(3)
# RecursionError: cannot set the recursion limit to 3 at the recursion depth 1: the limit is too low

sys.setrecursionlimit(10 ** 9)
print(sys.getrecursionlimit())
# 1000000000

# sys.setrecursionlimit(10 ** 10)
# OverflowError: signed integer is greater than maximum

recu_test(10 ** 4)
# Finish

# recu_test(10 ** 5)
# Segmentation fault

print(resource.getrlimit(resource.RLIMIT_STACK))
# (8388608, -1)

resource.setrlimit(resource.RLIMIT_STACK, (-1, -1))

print(resource.getrlimit(resource.RLIMIT_STACK))
# (-1, -1)

recu_test(10 ** 5)
# Finish
