def sort_list(number_list):

    #flag for the while loop
    repeat = True
    #gets the length of the list
    n = len(number_list)

    #this while loop only repeats if a number in the list is smaller
    #than the next one in the list
    while repeat:
        repeat = False

        #because lists start from zero, i have to subtract 1 from the length of the list
        for i in range(n-1):
            
            #if this if statement fails, it means the list is sorted,
            #so the while loop doesn't repeat
            if number_list[i] > number_list[i + 1]:
                number_list[i], number_list[i + 1] = number_list[i + 1], number_list[i]
                #if a change does happen, 
                #repeat is set to true so the program repeats
                repeat = True
            
    
    return print(number_list)