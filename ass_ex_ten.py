num_list = [10, 9, 8, 7]

def sort_list(number_list):
    flag = True

    while flag:
        for char, i in enumerate(num_list):
            next_char = char+1

            try:
                if i < num_list[next_char]:
                    next
            
            except:
                print(number_list)
                flag = False
            
            else:
                
                try:
                    if i > num_list[next_char]:
                            bigger_number = i
                            next_number = num_list[next_char]
                            num_list[next_char] = bigger_number
                            num_list[char] = next_number
                        
                except:
                    next     

sort_list(num_list)

