from sklearn.datasets import fetch_olivetti_faces

data = fetch_olivetti_faces()

print(type(data))
# <class 'sklearn.utils.Bunch'>

print(data.keys())
# dict_keys(['data', 'images', 'target', 'DESCR'])

print(data.data.shape)
# (400, 4096)

print(data.target.shape)
# (400,)

print(data.images.shape)
# (400, 64, 64)
