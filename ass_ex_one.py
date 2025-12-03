def calculator():
    
    #This contains the list of operators the calculator can use
    operator_list = ["+","-","*","/","<","<=",">",">="]

    #try statement is used for validation
    try:
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        operator = input("Enter the operator: ")

        #the program ends if the operator isnt in the list
        if operator not in operator_list:
            return print("Invalid operator")
    
    #executes in the case of an error
    except:
        print("Your inputs are invalid. Try again.")
    
    else:

        #performs calculations with all the operators
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