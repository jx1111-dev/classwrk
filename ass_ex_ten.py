num_list = [10, 9, 8, 7]

def sort_list(number_list):

    #flag for the while loop
    flag = True

    while flag:

        #each iteration of the loop has the index of the character and the character
        for index, char in enumerate(num_list):
            next_index = index+1
            print(index)
            print(char)

            #compares the current item in the list to the one at the next position.
            #if it is smaller than the next, it goes to the next iteration.
            #if the next position is outside of the list, it throws an exception,
            #ending the loop.
            try:
                if char < num_list[next_index]:
                    next
            
            #ends the loop if an exception is thrown.
            except:
                print(number_list)
                flag = False
            
            else:
                
                try:
                    #compares the current character to the one at the next position
                    if char > num_list[next_index]:
                            
                            #if it's bigger, the char is stored as bigger_number
                            bigger_number = char

                            #the number at the next index is stored as next_number
                            next_number = num_list[next_index]

                            #the number at the next position is replaced by the bigger number
                            num_list[next_index] = bigger_number

                            #the number at the current position is replaced by the smaller number
                            num_list[index] = next_number
                
                #in case it fails, it goes to the next loop
                except:
                    next     

sort_list(num_list)
