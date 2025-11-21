def sum_of_digits(num):
    num = list(str(num))
    x = 0

    for i in num:
        x+= int(i)
    
    return x

print(sum_of_digits(0))