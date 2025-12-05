def calculate_weekly_pay():

    #The normal and overtime salaries are defined
    pay = 12
    overtime = 18

    #input validation
    try:
        hours_done = int(input("Enter the hours you worked: "))
        
        if hours_done < 0:
            return print("Invalid input.")

    except:
        print("Invalid input.")
        return
    
    else:
        #The program decides if it should apply normal or overtime pay,
        #then calculates the total pay.
        if hours_done < 35:
            total_pay = hours_done * pay

        else:
            total_pay = (35*pay) + ((hours_done - 35) * overtime)

    print(f"Your total pay is: {total_pay}")