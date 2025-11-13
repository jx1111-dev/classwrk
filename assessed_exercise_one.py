num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
operator = input("Enter the operator: ")
operator_list = ["+","-","*","/","<","<=",">",">="]

def calculator(num1, num2, operator):

    if operator not in operator_list:
        print("Invalid operator")
        return "Invalid operator"
    
    if operator =="+":
        result = num1 + num2

    elif operator == "-":
        result = num1-num2

    elif operator == "*":
        result = num1*num2

    elif operator == "/":
        if num2 == 0:
            print("Error! You cannot divide by 0!")
            return "error"
            
        result = num1/num2


    elif operator == "%":
        result = num1%num2

    elif operator == "<":
        result = num1<num2


    elif operator == "<=":
        result = num1<=num2


    elif operator == ">":
        result = num1>num2

    elif operator == ">=":
        result = num1>=num2


    return result

print(calculator(num1, num2, operator))