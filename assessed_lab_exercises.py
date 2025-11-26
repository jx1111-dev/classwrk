def calculator(num1, num2, operator):
    
    operator_list = ["+","-","*","/","<","<=",">",">="]

    #validates the inputs. if they are floats, the program continues. 
    #if they werent, it would throw an exception. 
    try:
        num1 = float(num1)
        num2 = float(num2)

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