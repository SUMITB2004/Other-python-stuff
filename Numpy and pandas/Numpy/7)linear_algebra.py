import numpy as np

a = np.ones((2,3), dtype= "int8")
print(a)

b = np.full((3,2), 2)
print(b)

c = np.matmul(a,b)
print(c)

d = np.identity(3)              #identify the determinant
det = np.linalg.det(d)
print(det)