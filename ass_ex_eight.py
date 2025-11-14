def are_anagrams():
    word1 = list(input("Enter your first word: ").lower())
    word2 = list(input("Enter your second word: ").lower())

    if word1 == word2:
        print("These words are anagrams.")
        return
    
    else:
        print("These words are not anagrams.")
        return
    
are_anagrams()

