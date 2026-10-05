list = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [0]
]

# print(list)             #prints the list   

# for row in list:        #prints the list in same order 
#     print(row)

for row in list:        #prints the elements of list seperately
    for col in row:
        print(col)