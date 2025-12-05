def calculate_average(num_list):

    try:

        for i in num_list:
            i = float(i)

    except:

        return print("Invalid input. Try again.")
    
    else:

        #sum will have each iteration added to it 
        #list_length will store the length of the list for calculating the average
        sum = 0
        list_length = 0

        #iterates through each item in num_list
        for i in num_list:
            list_length += 1
            sum += i
        
        #floor division is used instead of regular division, to make sure the output is an integer
        avg = sum // list_length
        print(f"The average (rounded down) is: {avg}")