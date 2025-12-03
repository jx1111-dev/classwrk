def max_of_three(num1, num2, num3):

    #input validation
    try:
        float(num1)
        float(num2)
        float(num3)
    
    except: 
        return print("Invalid inputs. Try again.")
        
        
    else:
        #this if statement returns the largest number by comparing num1
        #with both num2 and num3 at the same time
        if num1 > (num2 and num3):
            return print(f"The largest number is: {num1}")
        
        #the same happens for num2
        elif num2 > (num1 and num3):
            return print(f"The largest number is: {num2}")
        
        #if neither num1 or num2 are the largest, it automatically means num3 is the largest
        else:
            return print(f"The largest number is: {num3}")