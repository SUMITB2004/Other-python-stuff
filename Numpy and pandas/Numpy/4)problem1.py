import numpy as np

a = np.ones((5,5), dtype = 'int8')
print(a)

b = np.zeros((3,3), dtype = 'int')
b[1,1] = 9
print(b)

c = a[1:4,1:4] = b
print(a)