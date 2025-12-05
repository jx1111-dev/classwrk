def is_palindrome(text):

    #gets the text and converts it to lowercase.
    #this is so having any uppercase letters doesn't affect
    #the output.
    text = str(text).lower()

    #the normal text is stored as text_forwards
    text_forwards = text

    #the reversed text is converted to a list (so it can be reversed),
    #then reversed
    text_backwards = list(text)
    text_backwards.reverse()

    #compares the normal text to the joined letters of the 
    #text_backwards list
    if text_forwards == ''.join(str(i) for i in text_backwards):
        #if it's the same, its a palindrome
        return True, print("It is a palindrome")
    
    else:
        #if not, it's not a palindrome
        return False, print("It is not a palindrome")
    
is_palindrome("M3d2m")
        