import pickle

d = {'int': 100, 'bool': False, 'list': [0, 1, 2]}

with open('data/temp/my_dict.pkl', 'wb') as f:
    pickle.dump(d, f)

with open('data/temp/my_dict.pkl', 'rb') as f:
    d_load = pickle.load(f)

print(d_load)
# {'int': 100, 'bool': False, 'list': [0, 1, 2]}

b = pickle.dumps(d)
print(b)
# b'\x80\x04\x95&\x00\x00\x00\x00\x00\x00\x00}\x94(\x8c\x03int\x94Kd\x8c\x04bool\x94\x89\x8c\x04list\x94]\x94(K\x00K\x01K\x02eu.'

print(type(b))
# <class 'bytes'>

d_loads = pickle.loads(b)
print(d_loads)
# {'int': 100, 'bool': False, 'list': [0, 1, 2]}

import json

d = {'int': 100, 'bool': False, 'list': [0, 1, 2]}

j = json.dumps(d)
d_json_loads = json.loads(j)
print(d_json_loads)
# {'int': 100, 'bool': False, 'list': [0, 1, 2]}

d['set'] = {0, 1, 2}
d['complex'] = 1 + 2j

# j = json.dumps(d)
# TypeError: Object of type set is not JSON serializable

b = pickle.dumps(d)
d_pickle_loads = pickle.loads(b)
print(d_pickle_loads)
# {'int': 100, 'bool': False, 'list': [0, 1, 2], 'set': {0, 1, 2}, 'complex': (1+2j)}

class MyClass:
    def my_func(self):
        print('This is MyClass.')

mc = MyClass()

mc.a = 100

b = pickle.dumps(mc)
mc_loads = pickle.loads(b)

mc_loads.my_func()
# This is MyClass.

print(mc_loads.a)
# 100

del MyClass

# mc_loads = pickle.loads(b)
# AttributeError: Can't get attribute 'MyClass' on <module '__main__'>

class MyClass:
    def my_func(self):
        print('This is the newly defined MyClass.')

mc_loads = pickle.loads(b)

mc_loads.my_func()
# This is the newly defined MyClass.

print(mc_loads.a)
# 100
