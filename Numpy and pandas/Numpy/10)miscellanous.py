import numpy as np

a = np.genfromtxt(r'F:\Python\Week 2\1) Numpy\num.txt',delimiter=',',dtype='int32')
print(a)

# Advanced Indexing and Boolean Masking

b = ((a>50) & (a<100))
print(b)

c = (~((a>50) & (a<100)))  #for reverse of upper
print(c)