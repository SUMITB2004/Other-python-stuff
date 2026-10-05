import numpy as np


a = np.array([1,2,3])                  #1D
print(a)

b = np.array([[1,2,3],[4,5,6]])        #2D
print(b)

c = b.ndim                             #to get D
print(c)

d = b.shape                            #to get shape
print(d)

e = b.itemsize                         #to get item size
print(e)

f = a.nbytes                           #to get ued byte
print(f)

