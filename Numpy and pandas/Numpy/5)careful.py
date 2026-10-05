import numpy as np

a = np.array([1,2,3])
b = a.copy()                    #we are using (.copy()) here just bcz when we replace value in b it automatically
b[1] = 99                       #replaces the value in a, so to avoid that we use (.copy()), it generates copy of a 
print(a)