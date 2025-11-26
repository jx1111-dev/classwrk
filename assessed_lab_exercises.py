def calculator():
    
    operator_list = ["+","-","*","/","<","<=",">",">="]

    try:
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        operator = input("Enter the operator: ")

        if operator not in operator_list:
            return print("Invalid operator")
    
    except:
        print("Your inputs are invalid. Try again.")
    
    else:

        if operator =="+":
            result = num1 + num2

        elif operator == "-":
            result = num1-num2

        elif operator == "*":
            result = num1*num2

        elif operator == "/":
            if num2 == 0:
                print("Error! You cannot divide by 0!")
                return
                
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

        return print(f"Your result is: {result}")