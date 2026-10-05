Comments_file = open("1)Comments.py","r")

# print(Comments_file.readable())            #tell the file is readable or not 
# print(Comments_file.read())                #to extract the input of the file 
# print(Comments_file.readline())            #use to extract only sinlge or particular line
# print(Comments_file.readlines())           #use to print multiple lines at once  
# print(Comments_file.readlines()[0])        #use to print particular line using index number

for i in Comments_file:                      #use to print complete file 
    print(i)
Comments_file.close()
