def max_of_three(num1, num2, num3):

    #input validation
    try:
        float(num1)
        float(num2)
        float(num3)
    
    except: 
        return print("Invalid inputs. Try again.")
        
        #this if statement returns the largest number
    else:
        if num1 > (num2 and num3):
            return print(f"The largest number is: {num1}")

        elif num2 > (num1 and num3):
            return print(f"The largest number is: {num2}")
        
        else:
            return print(f"The largest number is: {num3}")