#ex 1
def calculator(num1, num2, operator):
    
    operator_list = ["+","-","*","/","<","<=",">",">=","%"]

    #validates the inputs. if they are floats, the program continues. 
    #if they werent, it would throw an exception. 
    try:
        num1 = float(num1)
        num2 = float(num2)

        #checks if the operator is one of the valid operators
        if operator not in operator_list:
            return print("Invalid operator")
    
    #runs when the program errors
    except:
        print("Your inputs are invalid. Try again.")
    
    else:

        #these if statements calculate the numbers with each operator
        if operator =="+":
            result = num1 + num2

        elif operator == "-":
            result = num1-num2

        elif operator == "*":
            result = num1*num2

        elif operator == "/":
            if num2 == 0:
                print("Error! You cannot divide by 0!")
                return
                
            result = num1/num2

        elif operator == "%":
            result = num1%num2

        elif operator == "<":
            result = num1<num2

        elif operator == "<=":
            result = num1<=num2

        elif operator == ">":
            result = num1>num2

        elif operator == ">=":
            result = num1>=num2

        #returns the result in a neat format
        return print(f"Your result is: {result}")

#ex 2    
def max_of_three(num1, num2, num3):

    #input validation
    try:
        float(num1)
        float(num2)
        float(num3)
    
    except: 
        return print("Invalid inputs. Try again.")
        
        #this if statement returns the largest number
    else:
        if num1 > (num2 and num3):
            return print(f"The largest number is: {num1}")

        elif num2 > (num1 and num3):
            return print(f"The largest number is: {num2}")
        
        else:
            return print(f"The largest number is: {num3}")

#ex 3
def winning_numbers(winning_list, guessed_list):

    #these if statements checks to see if the number is in the winning list
    if guessed_list[0] in winning_list:
        num1 = True
    else:
        num1 = False
    
    if guessed_list[1] in winning_list:
        num2 = True
    else:
        num2 = False

    if guessed_list[2] in winning_list:
        num3 = True
    else:
        num3 = False

    #then, this if statement determined the prize based on how many guessed numbers are in the winning list
    if (num1 and num2 and num3) == True:
        print("First")

    elif (num1 and num2) or (num2 and num3) or (num1 and num3) == True:
        print("Second")

    elif num1 or num2 or num3 == True:
        print("Third")

    else:
        print("No")

#ex 4
def sum_of_evens():
    #these two inputs get the maximum and minimum number

    try:

        min_num = int(input("Enter the minimum number: "))
        max_num = int(input("Enter the maximum number: "))

    except:

        return print("Invalid input.")
    
    else:

        #the sum will be added to throughout the for statement, so it is declared here
        sum = 0
        
        #the range for the for loop is set from the minimum number to the maximum number
        for i in range(min_num, max_num):
            
            #each iteration, this if statement checks if the number is even. If it is, it is added to the sum.
            if i % 2 == 0:
                sum += i
            
        print(f"Your sum is: {sum}")

#ex 5
def calculate_average(num_list):

    try:
        
        #input validation. checks if each item in the list is a float
        for i in num_list:
            i = float(i)

    except:

        return print("Invalid input. Try again.")
    
    else:

        #sum will have each iteration added to it 
        #list_length will store the length of the list for calculating the average
        sum = 0
        list_length = 0

        #iterates through each item in num_list
        for i in num_list:
            list_length += 1
            sum += i
        
        #floor division is used instead of regular division, to make sure the output is an integer
        avg = sum // list_length
        print(f"The average (rounded down) is: {avg}")

#ex 6
def calculate_weekly_pay():

    #The normal and overtime salaries are defined
    pay = 12
    overtime = 18

    #input validation
    try:
        hours_done = int(input("Enter the hours you worked: "))
        
        if hours_done < 0:
            return print("Invalid input.")

    except:
        print("Invalid input.")
        return
    
    else:
        #The program decides if it should apply normal or overtime pay,
        #then calculates the total pay.
        if hours_done < 35:
            total_pay = hours_done * pay

        else:
            total_pay = (35*pay) + ((hours_done - 35) * overtime)

    print(f"Your total pay is: {total_pay}")

#ex 7
def is_prime():

    #The prime factors are defined here
    prime_list = [2, 3, 5, 7]

    #input validation
    try:
        num = float(input("Enter your number: "))
    
    except:
        print("Invalid number.")
        return
    
    else:

        #this if statement makes all negative numbers return as false
        if num > 1:
            
            #checks if the number is directly in the prime number list
            if num in prime_list:
                print("This number is prime.")
                return
            
            else:
                
                #if it's not, it determines wether or not it's prime by
                #checking if the modulus is 0
                for i in prime_list:

                    if num % i == 0:
                        print("This number is not prime.")
                        return
                    
                    else:
                        next
                
                print("This number is prime.")
                return
        else:
            print("This number is not prime.")
            return

#ex 8
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

#ex 9
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

#ex 10
def sort_list(number_list):

    #flag for the while loop
    repeat = True
    #gets the length of the list
    n = len(number_list)

    #this while loop only repeats if a number in the list is smaller
    #than the next one in the list
    while repeat:
        repeat = False

        #because lists start from zero, i have to subtract 1 from the length of the list
        for i in range(n-1):
            
            #if this if statement fails, it means the list is sorted,
            #so the while loop doesn't repeat
            if number_list[i] > number_list[i + 1]:
                number_list[i], number_list[i + 1] = number_list[i + 1], number_list[i]
                #if a change does happen, 
                #repeat is set to true so the program repeats
                repeat = True
            
    
    return print(number_list)

#ex 11
def sum_of_digits(num):
    #the number is turned into a string, and into a list
    #so we can iterate through each digit
    num = list(str(num))
    #x will act as the sum
    x = 0

    #input validation
    try:

        for i in num:
            i = int(i)
    
    except:

        return print("Invalid input.")
    
    else:

        #iterates through the list (contains all digits),
        #and adds it to the sum
        for i in num:
            x+= int(i)
        
    return print(x)

#ex 12
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

#ex 13
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

#ex 14
def letter_grade(data_input):
    
    #because of the input being a dictionary, and thus, being hard to input validate,
    #i put the whole function in a try except block to catch any errors.
    try:

        #gets the length of the dictionary 
        #to know how many scores and credits there are
        #to loop through
        x = len(data_input)

        #instead of doing the entire calculation at once, the
        #numerator and denominator totals are calculated seperately
        #and the calculation will be done after
        numerator = 0

        denominator = 0

        #iterates through the dictionary to get each score and credit
        #using i as the index
        for i in range(x):
            numerator += data_input[i]["score"] * data_input[i]["credits"]
            
            denominator += data_input[i]["credits"]
        
        #the average is calculated
        average = numerator / denominator

        #grade is automatically set to F
        grade = "F"

        #then it compares the average to determine the letter grade
        if 50 <= average < 60:
            grade = "D"
        
        elif 60 <= average < 70:
            grade = "C"
        
        elif 70 <= average < 90:
            grade = "B"

        elif average >= 90:
            grade = "A"

        return print(f"Average score: {average}\nLetter grade: {grade}")

    except:
        return print("Something went wrong. Try again.")

#ex 15
def maximum_gap(list1, list2):
    
    #gets the maximum value of both lists
    list1_max = max(list1)
    list2_max = max(list2)

    #depending on which one is bigger, 
    #the minimum of the other list gets subtracted from it,
    #which is max_gap
    if list1_max > list2_max:
        max_gap = list1_max - min(list2)
    
    else:
        max_gap = list2_max - min(list1)

    #then, max gap is printed
    return print(max_gap)

#ex 16
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

#ex 17
def net_annual_income(gross_salary):

    #input validation
    try:
        float(gross_salary)
    
    except:
        return print("Invalid input. Try again.")
    
    else:
        #tax is automatically set to 0
        tax = 0

        #all the conditions are set
        if  12570 < gross_salary:
            
            if gross_salary <= 50270:
                tax += (gross_salary - 12570) * 0.2
            
            else:
                tax += (50270 - 12570) * 0.2
        
        if  50270 < gross_salary:
            
            if gross_salary <= 125140:
                tax += (gross_salary - 50270) * 0.4
            
            else:
                tax += (125140 - 50270) * 0.4

        if  125140 < gross_salary:
            
            tax += (gross_salary - 125140) * 0.45

        #net income calculated
        net_income = gross_salary - tax

        return print(f"Your net annual income is: £{net_income}")

#ex 18
def my_split(my_str, sep):
    
    split_list = []

    #iterates through each character in the string
    for i in my_str:

        #if the character is the separator, a new item is added to the list
        if i == sep:
            split_list.append('')
        
        #if the character is not the separator, it is added to the last item in the list
        else:
            if len(split_list) == 0:
                split_list.append(i)

            else:
                #adds the character to the last item in the list
                split_list[-1] += i
        
    return print(split_list)

#ex 19
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

#ex 20
def closest_pair_under_budget(prices, budget):

    #this is where all pairs found and their cost will be stored
    pairs = []

    #iterates through each item
    for i in range(len(prices)):

        #iterates through each item
        for j in range(len(prices)):

            #but skips the loop if the items are the same (they need to be distinct)
            if j == i:
                continue
            
            else:
                #item names and prices are stored as variables
                item1_name, item1_price = prices[i]
                item2_name, item2_price = prices[j]

                #total price of both items is calculated
                total_price = item1_price + item2_price

                #if the price outweighs the budget, the loop is skipped because we cant
                #afford them with the budget
                if budget - total_price < 0:
                    continue
                
                #the leftover is how much is left if the total price is smaller than the budget
                leftover = budget - total_price

                #this stores the item names and leftover as a tuple
                current_pair = (item1_name, item2_name, leftover)

                #then it is appended to the list
                pairs.append(current_pair)
    
    #then we use the min function with key=lambda telling it to compare them based on the
    #leftover money
    closest = min(pairs, key=lambda x: x[2])
    #which gets us the closest pair
    return print(closest)
