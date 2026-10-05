import numpy as np

a = np.array([[1,2,3,4,5,6,7],[8,9,10,11,12,13,14]])
print(a)

b = a[1,5]          #access specific num
print(b)

c = a[0, : ]        #access specific coloumn
print(c)

d = a[ :, 2]        #access specific row
print(d)

e = a[1, 0:6:3]     #little more fancy (row, start pt:end pt:gap)
print(f"it is e :{e}")

g = (a[1,2] == 11)  #for true and false
print(g)

a[1,1] = 99         #to replace the value
print(a)

a[:,2] = [1,2]      #to replace the row
print(a)


b = np.array([[1,2],[3,4],[5,6],[7,8]])
print(b)

c = b[1,1]
print(c)

d = b[1:4:2]
print(d) 

b[1:4:2] = [9,9] , [8,8]
print(b) 