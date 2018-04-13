d = {'key1': 'val1', 'key2': 'val2', 'key3': 'val3'}

d_swap = {v: k for k, v in d.items()}
print(d_swap)
# {'val1': 'key1', 'val2': 'key2', 'val3': 'key3'}

def get_swap_dict(d):
    return {v: k for k, v in d.items()}

d_swap = get_swap_dict(d)
print(d_swap)
# {'val1': 'key1', 'val2': 'key2', 'val3': 'key3'}

d_duplicate = {'key1': 'val1', 'key2': 'val1', 'key3': 'val3'}

d_duplicate_swap = get_swap_dict(d_duplicate)
print(d_duplicate_swap)
# {'val1': 'key2', 'val3': 'key3'}
