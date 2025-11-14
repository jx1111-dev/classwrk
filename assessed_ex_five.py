num_list = [1, 8, 9]

def calculate_average():
    sum = 0
    list_length = 0

    for i in num_list:
        list_length += 1
        sum += i
    
    avg = sum // list_length
    print(f"The average (rounded down) is: {avg}")

calculate_average()