def longest_repetition(text):
    
    char_tuple = []
    rep_count = 1

    current_char = text[0]

    #iterates through the string
    for i in range(1, len(text)):
        
        #if the character at position i is the current character,
        #adds 1 to rep count
        if text[i] == current_char:
            rep_count += 1

        #if it isnt, the current_char is replaced by the new character.
        else:
            #the previous rep count and the character it counted are then
            #stored in this list
            char_tuple.append((current_char, rep_count))
            #and the current character and rep count are reset
            current_char = text[i]
            rep_count = 1

    #when the for loop finishes, it adds the last tuple
    char_tuple.append((current_char, rep_count))
    #this tells the max function to compare using the second item in the tuple as
    #opposed to the first, because then it would print the answer based on alphabetical
    #order
    print(max(char_tuple, key= lambda x: x[1]))
