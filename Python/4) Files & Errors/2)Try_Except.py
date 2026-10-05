try:
    value = 10/0
    num = int(input("Enter a num: "))
    print(num)

# except ValueError:
#     print("invalid input")   

# except ZeroDivisionError:            
#     print("num is divided by zero")    

except ZeroDivisionError as err:       #it gives us the type of error
    print(err)     