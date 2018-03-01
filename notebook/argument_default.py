def func_default(arg1, arg2='default_x', arg3='default_y'):
    print(arg1)
    print(arg2)
    print(arg3)

func_default('a')
# a
# default_x
# default_y

func_default('a', 'b')
# a
# b
# default_y

func_default('a', arg3='c')
# a
# default_x
# c

# def func_default_error(arg2='default_a', arg3='default_b', arg1):
#     print(arg1)
#     print(arg2)

# SyntaxError: non-default argument follows default argument

def func_default_list(l=[0, 1, 2], v=3):
    l.append(v)
    print(l)

func_default_list([0, 0, 0], 100)
# [0, 0, 0, 100]

func_default_list()
# [0, 1, 2, 3]

func_default_list()
# [0, 1, 2, 3, 3]

func_default_list()
# [0, 1, 2, 3, 3, 3]

def func_default_dict(d={'default': 0}, k='new', v=100):
    d[k] = v
    print(d)

func_default_dict()
# {'default': 0, 'new': 100}

func_default_dict(k='new2', v=200)
# {'default': 0, 'new': 100, 'new2': 200}

def func_default_list_none(l=None, v=3):
    if l is None:
        l = [0, 1, 2]
    l.append(v)
    print(l)

func_default_list_none()
# [0, 1, 2, 3]

func_default_list_none()
# [0, 1, 2, 3]
