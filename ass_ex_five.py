num_list = [1, 8, 9]

def calculate_average():
    #sum will have each iteration added to it 
    #list_length will store the length of the list for the end
    sum = 0
    list_length = 0

    for i in num_list:
        list_length += 1
        sum += i
    
    #floor division is used instead of regular division, to make sure the output is an integer
    avg = sum // list_length
    print(f"The average (rounded down) is: {avg}")

calculate_average()