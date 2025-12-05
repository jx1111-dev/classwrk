def count_vowels():

    #the vowel list is defined
    vowel_list = ['a', 'e', 'i', 'o', 'u']

    #because the vowel list is lowercase,
    #the .lower function is used to make the input fully lowercase
    #stores the word as a list so it can be iterated through
    text = list(input("Enter your text: ").lower())

    #vowel_tally is used as a tally of how many vowels are in the input
    vowel_tally = 0

    #iterates through each letter in the input, adds to the tally for each vowel
    for i in text:

        if i in vowel_list:
            vowel_tally += 1
    
    print(f"Your text has {vowel_tally} vowels.")
