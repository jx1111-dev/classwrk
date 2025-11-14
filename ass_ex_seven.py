prime_list = [2, 3, 5, 7]

def is_prime():

    try:
        num = int(input("Enter your number: "))
    
    except:
        print("Invalid number.")
        return
    
    else:
        if num > 1:

            if num in prime_list:
                print("This number is prime.")
                return
            
            else:

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

is_prime()
