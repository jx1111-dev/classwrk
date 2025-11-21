def max_of_three(num1, num2, num3):#

    if num1 > (num2 and num3):
        return num1

    elif num2 > (num1 and num3):
        return num2
    
    else:
        return num3
    
print(max_of_three(12388, 3874, 12388))