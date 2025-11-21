import string
def password_strength(password):
    spec_chars = ["@","$","£"]
    upper_alpha = list(string.ascii_uppercase)
    
    password = list(str(password))

    flag = True
    special_char = False
    upper_char = False

    while flag:

        for i in password:

            if i in spec_chars:
                special_char = True
            
            if i in upper_alpha:
                upper_char = True
        
            if (special_char and upper_char) == True:
                flag = False
        
        if i == password[-1]:
            flag = False
        
    if (len(password) < 6) or (special_char == False and upper_char == False):

        return print("Weak")
    
    elif ((6 <= len(password) <= 10) and (special_char == True and upper_char == True)):

        return print("Medium")
    elif ((len(password) > 10) and (special_char == True and upper_char == True)):

        return print("Strong")
    
    else:

        return print("Weak")
    

password_strength("ffF@fffff")


            
            






