def print_len_lbyl_list(x):
    if isinstance(x, list):
        print(len(x))
    else:
        print('x is not list')

print_len_lbyl_list([0, 1, 2])
# 3

print_len_lbyl_list(100)
# x is not list

print_len_lbyl_list((0, 1, 2))
# x is not list

print_len_lbyl_list('abc')
# x is not list

def print_len_lbyl_list_tuple(x):
    if isinstance(x, (list, tuple)):
        print(len(x))
    else:
        print('x is not list or tuple')

print_len_lbyl_list_tuple([0, 1, 2])
# 3

print_len_lbyl_list_tuple(100)
# x is not list or tuple

print_len_lbyl_list_tuple((0, 1, 2))
# 3

print_len_lbyl_list_tuple('abc')
# x is not list or tuple
