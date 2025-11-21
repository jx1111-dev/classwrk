def is_palindrome(text):
    text = str(text).lower()
    text_forwards = text
    text_backwards = list(text)
    text_backwards.reverse()

    if text_forwards == ''.join(str(i) for i in text_backwards):
        return True, print("It is a palindrome")
    
    else:
        return False, print("It is not a palindrome")
    
is_palindrome("madam")
        