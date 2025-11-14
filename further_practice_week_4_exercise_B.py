thirty_day_months = [4, 9, 6, 11]


def date_validation():
    day = int(input("Enter the day: "))
    month = int(input("Enter the month number: "))

    if 1 <= month <= 12:
        if month in thirty_day_months:
            if 1 <= day <= 30:
                print("This date is valid.")
                return
            else:
                print("This date is invalid.")
                return


        elif month == 2:
            if 1 <= day <= 28:
                print("This date is valid.")
                return
            
            else:
                print("This date is invalid.")
                return
        

        else:
            if 1 <= day <= 31:
                print("This date is valid.")
                return
            
            else:
                print("This date is invalid.")
                return


    else:
        print("The date is not valid.")

date_validation()
