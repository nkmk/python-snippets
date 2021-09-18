d = {'apple': 1, 'banana': 10, 'orange': 100}

dc = {k: v for k, v in d.items() if v % 2 == 0}
print(dc)
# {'banana': 10, 'orange': 100}

dc = {k: v for k, v in d.items() if v % 2 == 1}
print(dc)
# {'apple': 1}

dc = {k: v for k, v in d.items() if k.endswith('e')}
print(dc)
# {'apple': 1, 'orange': 100}

dc = {k: v for k, v in d.items() if not k.endswith('e')}
print(dc)
# {'banana': 10}

dc = {k: v for k, v in d.items() if v % 2 == 0 and k.endswith('e')}
print(dc)
# {'orange': 100}
