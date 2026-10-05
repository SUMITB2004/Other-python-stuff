num1 = float(input("Enter first num: "))
op = input("Enter a operator: ")
num2 = float(input("Enter secound num: "))

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "/":
    print(num1 / num2)
elif op == "*":
    print(num1 * num2)

else:
    print("Invalid Operator")        

