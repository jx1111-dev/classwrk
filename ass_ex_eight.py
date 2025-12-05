def are_anagrams():

    #gets the words and stores them as lists
    #then, all items in the list are made lowercase (to make them the same)
    #and then they are sorted, which arranges all the letters in the same order,
    #if the words are the same.
    word1 = list(input("Enter your first word: ").lower())
    word1 = word1.sort()
    word2 = list(input("Enter your second word: ").lower())
    word2 = word2.sort()

    #compares the elements of each list. If they have the same letters, it means
    #it's an anagram
    if word1 == word2:
        print("These words are anagrams.")
        return
    
    else:
        print("These words are not anagrams.")
        return
    
are_anagrams()

