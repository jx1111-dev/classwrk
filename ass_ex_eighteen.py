def my_split(my_str, sep):
    
    split_list = []

    #iterates through each character in the string
    for i in my_str:

        #if the character is the separator, a new item is added to the list
        if i == sep:
            split_list.append('')
        
        #if the character is not the separator, it is added to the last item in the list
        else:
            if len(split_list) == 0:
                split_list.append(i)

            else:
                #adds the character to the last item in the list
                split_list[-1] += i
        
    return print(split_list)