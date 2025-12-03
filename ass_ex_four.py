def sum_of_evens():
    #these two inputs get the maximum and minimum number

    try:

        min_num = int(input("Enter the minimum number: "))
        max_num = int(input("Enter the maximum number: "))

    except:

        return print("Invalid input.")
    
    else:

        #the sum will be added to throughout the for statement, so it is declared here
        sum = 0
        
        #the range for the for loop is set from the minimum number to the maximum number
        for i in range(min_num, max_num):
            
            #each iteration, this if statement checks if the number is even. If it is, it is added to the sum.
            if i % 2 == 0:
                sum += i
            
        print(f"Your sum is: {sum}")