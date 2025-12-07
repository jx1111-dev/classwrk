def net_annual_income(gross_salary):

    #input validation
    try:
        float(gross_salary)
    
    except:
        return print("Invalid input. Try again.")
    
    else:
        #tax is automatically set to 0
        tax = 0

        #all the conditions are set
        if  12570 < gross_salary:
            
            if gross_salary <= 50270:
                tax += (gross_salary - 12570) * 0.2
            
            else:
                tax += (50270 - 12570) * 0.2
        
        if  50270 < gross_salary:
            
            if gross_salary <= 125140:
                tax += (gross_salary - 50270) * 0.4
            
            else:
                tax += (125140 - 50270) * 0.4

        if  125140 < gross_salary:
            
            tax += (gross_salary - 125140) * 0.45

        #net income calculated
        net_income = gross_salary - tax

        return print(f"Your net annual income is: £{net_income}")
    