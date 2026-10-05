import numpy as np

a = np.array([[1,2,3],[4,5,6]])
print(a)

min = np.min(a)
print(min)

max = np.max(a)
print(max)

sum = np.sum(a)
print(sum)

sum1 = np.sum(a, axis = 0)                    #it adds the row         
print(sum1)

