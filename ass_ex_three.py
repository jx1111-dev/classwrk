def winning_numbers(winning_list, guessed_list):

    #these if statements checks to see if the number is in the winning list
    if guessed_list[0] in winning_list:
        num1 = True
    else:
        num1 = False
    
    if guessed_list[1] in winning_list:
        num2 = True
    else:
        num2 = False

    if guessed_list[2] in winning_list:
        num3 = True
    else:
        num3 = False

    if (num1 and num2 and num3) == True:
        print("First")

    elif (num1 and num2) or (num2 and num3) or (num1 and num3) == True:
        print("Second")

    elif num1 or num2 or num3 == True:
        print("Third")

    else:
        print("No")

winning_numbers(["a", "b", "c"], ["d", "e", "f"])