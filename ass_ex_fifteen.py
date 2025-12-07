def maximum_gap(list1, list2):
    
    #gets the maximum value of both lists
    list1_max = max(list1)
    list2_max = max(list2)

    #depending on which one is bigger, 
    #the minimum of the other list gets subtracted from it,
    #which is max_gap
    if list1_max > list2_max:
        max_gap = list1_max - min(list2)
    
    else:
        max_gap = list2_max - min(list1)

    #then, max gap is printed
    return print(max_gap)