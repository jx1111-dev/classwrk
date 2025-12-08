def sum_of_digits(num):
    #the number is turned into a string, and into a list
    #so we can iterate through each digit
    num = list(str(num))
    #x will act as the sum
    x = 0

    #input validation
    try:

        for i in num:
            i = int(i)
    
    except:

        return print("Invalid input.")
    
    else:

        #iterates through the list (contains all digits),
        #and adds it to the sum
        for i in num:
            x+= int(i)
        
    return print(x)