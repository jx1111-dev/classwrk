def cipher_text(input_text, key):

    #inut validation makes sure key is a positive integer
    try:

        int(key)


    except:
        print("Invalid key. Try again.")
    
    else:

        #input validation pt2
        if key < 0:

            return print("Invalid key. Try again")
        
        #converts the string to a list so it can be iterated through
        input_text = list(input_text)

        #gets the length of the list
        n = len(input_text)

        #iterates through the length of the list
        for i in range (n):
            
            #the character at position i is replaced by the decrypted character
            input_text[i] = chr((ord(input_text[i]) - key) % 256)

        #the list is joined back into a string
        input_text = ''.join(str(i) for i in input_text)
        
        return print(input_text)
    