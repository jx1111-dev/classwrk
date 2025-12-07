def letter_grade(data_input):
    
    #because of the input being a dictionary, and thus, being hard to input validate,
    #i put the whole function in a try except block to catch any errors.
    try:

        #gets the length of the dictionary 
        #to know how many scores and credits there are
        #to loop through
        x = len(data_input)

        #instead of doing the entire calculation at once, the
        #numerator and denominator totals are calculated seperately
        #and the calculation will be done after
        numerator = 0

        denominator = 0

        #iterates through the dictionary to get each score and credit
        #using i as the index
        for i in range(x):
            numerator += data_input[i]["score"] * data_input[i]["credits"]
            
            denominator += data_input[i]["credits"]
        
        #the average is calculated
        average = numerator / denominator

        #grade is automatically set to F
        grade = "F"

        #then it compares the average to determine the letter grade
        if 50 <= average < 60:
            grade = "D"
        
        elif 60 <= average < 70:
            grade = "C"
        
        elif 70 <= average < 90:
            grade = "B"

        elif average >= 90:
            grade = "A"

        return print(f"Average score: {average}\nLetter grade: {grade}")

    except:
        return print("Something went wrong. Try again.")
