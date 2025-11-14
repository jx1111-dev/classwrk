vowel_list = ['a', 'e', 'i', 'o', 'u']

def count_vowels():
    text = list(input("Enter your text: ").lower())
    vowel_tally = 0

    for i in text:

        if i in vowel_list:
            vowel_tally += 1
    
    print(f"Your text has {vowel_tally} vowels.")

count_vowels()
