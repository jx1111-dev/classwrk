year = ""

def leap_year_checker(year):
    year = int(input("Enter a year: "))

    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print("It is a leap year.")
                return
            else:
                print("It is not a leap year.")
                return

        print("It is a leap year.")
    
    else:
        print("It is not a leap year.")

leap_year_checker(year)