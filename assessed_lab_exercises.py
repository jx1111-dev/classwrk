def calculator():
    
    operator_list = ["+","-","*","/","<","<=",">",">="]

    #gets the inputs
    try:
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        operator = input("Enter the operator: ")

        #checks if the operator is one of the valid operators
        if operator not in operator_list:
            return print("Invalid operator")
    
    #runs when the program errors
    except:
        print("Your inputs are invalid. Try again.")
    
    else:

        #these if statements calculate the numbers with each operator
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

        #returns the result in a neat format
        return print(f"Your result is: {result}")