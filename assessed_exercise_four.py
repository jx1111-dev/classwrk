def sum_of_events():
    min_num = int(input("Enter the minimum number: "))
    max_num = int(input("Enter the maximum number: "))

    sum = 0
    
    for i in range(min_num, max_num):
        

        if i % 2 == 0:
            sum += i
            

    print(f"Your sum is: {sum}")

sum_of_events()