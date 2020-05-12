import platform
import numpy
import scipy

print('Python:       ', platform.python_version())
print('NumPy:        ', numpy.__version__)
print('SciPy:        ', scipy.__version__)

try:
    import sklearn
    import numba
    import networkx

    print('scikit-learn: ', sklearn.__version__)
    print('Numba:        ', numba.__version__)
    print('NetworkX:     ', networkx.__version__)
except:
    pass
