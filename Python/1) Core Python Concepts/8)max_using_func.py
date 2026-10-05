def max(a,b,c):
    if (a >= b and a >= c):
        return a 
    elif (b >= a and b>= c):
        return b 
    else:
        return c
    
a = int(input("Enter num a: "))    
b = int(input("Enter num b: "))            
c = int(input("Enter num c: "))    

print(max(a,b,c))