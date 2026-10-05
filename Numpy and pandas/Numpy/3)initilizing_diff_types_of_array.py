import numpy as np

a = np.zeros((2,3), dtype = "int8")            #for matrix of zeros
print(a)

b = np.ones((4,2,2), dtype = "int8")           #for matrix of ones
print(b)

c = np.full((2,2),4)                           #to create matrix
print(c)

d = np.full_like(b,4)                          #to create matrix like recent
print(d)

e = np.random.rand(4,2)                        #for random matrix
print(e)

f = np.random.randint(5,10, size=(3,3))        #random matrix with range (start,end, size=(rows,coloumns))
print(f)

g = np.identity((3), dtype = "int8")
print(g)