def calculate_weekly_pay():
    pay = 12
    overtime = 18
    try:
        hours_done = int(input("Enter the hours you worked: "))

    except:
        print("Invalid number inputted.")
        return
    
    else:
        if hours_done < 35:
            total_pay = hours_done * pay

        else:
            total_pay = (35*pay) + ((hours_done - 35) * overtime)

    print(f"Your total pay is: {total_pay}")

calculate_weekly_pay()