
def password_strength(password):
    #the string library is used to generate the ASCII alphabet to 
    #make the code look neater
    import string
    #stores specified special characters
    spec_chars = ["@","$","£"]
    #this requires the string library
    upper_alpha = list(string.ascii_uppercase)
    
    #converts the list to a list so it can be
    #iterated through
    password = list(str(password))

    flag = True
    special_char = False
    upper_char = False

    while flag:
        
        #iterates through each character in the password
        #and checks if it contains at least one special character
        #or one uppercase letter
        #or both
        for i in password:

            if i in spec_chars:
                special_char = True
            
            if i in upper_alpha:
                upper_char = True
        
            if (special_char and upper_char) == True:
                flag = False
        
        #if the loop has reached the end of the password,
        #the flag is set to false to end the while loop
        if i == password[-1]:
            flag = False
        
    #these if statements determine the strength of the password
    if (len(password) < 6) or (special_char == False and upper_char == False):

        return print("Weak")
    
    elif ((6 <= len(password) <= 10) and (special_char == True and upper_char == True)):

        return print("Medium")
    
    elif ((len(password) > 10) and (special_char == True and upper_char == True)):

        return print("Strong")
    
    else:

        return print("Weak")
    

password_strength("111111111A$")


            
            






