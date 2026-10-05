import numpy as np

a = np.array([[1,2,3,4],[5,6,7,8]])
print(a)

b = a.reshape((4,2))
print(b)

c = a.reshape(2,2,2)                             #reshape(matrix,rows,coloumns)
print(c)


v1 = np.array([1,2,3,4])                        #vertical stacking
v2 = np.array([5,6,7,8])
v = np.vstack([v1,v2,v1,v2])
print(v)

h1 = np.array([11,12,13,14])                    #horizontal stacking
h2 = np.array([15,16,17,18])
h = np.hstack([h1,h2,h1,h2])
print(h)