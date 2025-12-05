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