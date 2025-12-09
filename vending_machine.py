def main_menu():

    #the inventory will be fixed each time the function runs.
    #this is unrealistic, but in order to have access to a real time inventory, i would need to set up a database,
    #which i feel is out of scope for the program
    
    inventory = {
        1 : {'name' : 'Water', 'price' : 1.20, 'stock' : 5},
        2 : {'name' : 'Soda', 'price' : 1.50, 'stock' : 5},
        3 : {'name' : 'Chocolate', 'price' : 2.50, 'stock' : 5},
        4 : {'name' : 'Crisps', 'price' : 1.40, 'stock' : 5},
        5 : {'name' : 'Sandwich','price' : 3.80, 'stock' : 5},
    }

    def add_balance():
        
        #stays true if the user wishes to add more coins
        balance_repeat_flag = True

        #stores the balance that will be returned at the end,
        #this variable is added to each pass of the while loop.
        #also gets displayed each pass so the user knows their balance.
        sum_of_balance = 0

        while balance_repeat_flag:
            balance_repeat_flag = False

            coin_input = input(f"Your balance: £{round(sum_of_balance, 2)}\nEnter a coin:\n1. £1\n2. £2\n3. 50p\n4. 20p\n5. Exit\n")

            #adds 1 pound coin
            if coin_input == "1":
                sum_of_balance += 1
                balance_repeat_flag = True
            
            #adds 2 pound coin
            elif coin_input == "2":
                sum_of_balance += 2
                balance_repeat_flag = True
            
            #adds 50p
            elif coin_input == "3":
                sum_of_balance += 0.5
                balance_repeat_flag = True
            
            #adds 20p
            elif coin_input == "4":
                sum_of_balance += 0.2
                balance_repeat_flag = True
            
            #exits and returns the user's inputted balance
            #only exit point
            elif coin_input == "5":
                return sum_of_balance
            
            #input validation
            else:
                input("Invalid input. Press any key to try again.")
                balance_repeat_flag = True

    def buy_items():

        cart_to_be_returned = []
        total = 0
        
        #lets the user choose more items
        #if false the buy items function ends
        add_to_cart_flag = True

        #each pass, lets the user choose another item to add to the cart.
        while add_to_cart_flag:
            add_to_cart_flag = False
            #prints the cart each pass
            print(f"Current cart:")
            #prints each list tuple without brackets and parenthesis
            for name, price in cart_to_be_returned:
                #some item names are too short and fall in the previous tab portion. they will use 2 tabs instead of 1
                if len(name) < 6:
                    print(f"{name}, \t\t£{price}")
                #item names over 6 letters are fine and only use one tab for the prices
                else:
                    print(f"{name}, \t£{price}")

            print(f"Total: \t\t£{round(total, 2)}")
            print("Select an item:")
            
            #for each key and value in the items of the inventory dict
            for k, v in inventory.items():
                
                #some item names are too short and fall in the previous tab portion. they will use 2 tabs instead of 1
                if len(v['name']) < 7:               
                    print(f"{k}, \t{v['name']}\t\t£{v['price']}\t Stock: {v['stock']}")
                
                #item names over 6 letters are fine and only use one tab for the prices
                else:
                    print(f"{k}, \t{v['name']}\t£{v['price']}\t Stock: {v['stock']}")
            #user can also choose a finished option to go to checkout
            print(f"6, \tFinished")
            
            #choice will be used to access the item in the dictionary
            choice = input()

            try:
                #input validation for the key
                key = int(choice)
            
            except:
                input("Invalid input. Press any key to try again.")
                add_to_cart_flag = True
            
            else:
                
                #checks if the key is in the inventory
                if key in inventory: 
                    #if it is, it assigns it to the variable item,
                    #so that the entry in the dictionary can be accessed
                    item = inventory[key]

                    #if the stock value of the item stored at that key is empty,
                    #the program makes the user choose another item
                    if item['stock'] <= 0:
                        input("Item is out of stock. Select another item.")
                        add_to_cart_flag = True
                        continue
                    
                    #if it isn't, it takes the 'name' field and the 'price' field,
                    #adds them to a tuple and appends them to the list. 
                    else:
                        entry = (item['name'], item['price'])
                        cart_to_be_returned.append(entry)

                        #the price of the item is added to a total
                        total += item['price']

                        #one stock is removed from the 'stock' field
                        item['stock'] -= 1
                        
                        add_to_cart_flag = True
                
                elif key == 6:
                    return cart_to_be_returned, total

                #if the key isnt in the dictionary, it makes the user choose it again
                else:
                    input("Invalid entry number. Press any key to try again.")
                    add_to_cart_flag = True

    def calculate_discount(cart_list, total):
        #if the user spends more than 7 pounds, apply a 15% discount
        if total > 7:
            discount = 0.85
        #if more than 5, apply 10% discount
        elif total > 5:
            discount = 0.90
        #if more than 3 items are ordered, apply 5% discount
        elif len(cart_list) > 3:
            discount = 0.95
        
        else:
            discount = 1
        
        discounted_total = total * discount

        return discount, discounted_total

    def checkout(balance, discount_total, order_num):

        change = balance - discount_total
        print("Outputting items...")
        print(f"Remaining balance: {change}")

        order_num += 1

        return change, order_num

    def change_calculation(change, order_num):

        if change % 2 == 0:
            num_of_coins = change / 2
            print(f"Your change is: {num_of_coins} £2 coin(s).")
        
        elif change % 1 == 0:
            num_of_coins = change / 1
            print(f"Your change is: {num_of_coins} £1 coin(s).")
        
        elif change % 0.5 == 0:
            num_of_coins = change / 0.5
            print(f"Your change is: {num_of_coins} 50p coin(s).")
        
        elif change % 0.2 == 0:
            num_of_coins = change / 0.2
            print(f"Your change is: {num_of_coins} 20p coin(s).")
        
        else:
            print("The machine cannot output your change.")
        
        if order_num % 2 != 0:
            print("Because your order number was odd, you got an extra pound change!")
            change += 1
        
        
        return change

    def make_csv_file(order_num, cart_list, total_cost, discount, discounted_total_cost, remaining_balance):
        import csv

        filename = (f"Order Number#{order_num}.csv")
        file = open(filename, "w", newline="")
        filewriter = csv.writer(file)

        filewriter.writerow(["Order Number:", order_num])
        filewriter.writerow(["Shopping cart:", cart_list])
        filewriter.writerow(["Total cost:", round(total_cost, 2)])
        filewriter.writerow(["Discount applied:", discount])
        filewriter.writerow(["Discounted total cost:", round(discounted_total_cost, 2)])
        filewriter.writerow(["Remaining balance:", remaining_balance])

        file.close()

        print(f"Your receipt has been saved as \"{filename}\".")

    #stores the number of orders so far
    order_number = 0

    #hold tuples of the item names and prices the user wants to buy
    cart = []

    #sum of all item prices in the cart
    cart_total = 0

    #user balance, will be used in buy_items
    user_balance = 0

    #amount the user has left over after checking out
    change = 0 

    #discount that will be applied to cart_total cost at checkout
    discount = 0

    #price after cart_total is discounted
    discounted_cart_total = 0

    #used to repeat the main menu, only false if user wants to end the program
    main_menu_flag_repeat = True

    while main_menu_flag_repeat:

        main_menu_flag_repeat = False

        print("-----------Welcome to the vending machine-----------")
        print("Your cart:")

        for name, price in cart:
                #some item names are too short and fall in the previous tab portion. they will use 2 tabs instead of 1
                if len(name) < 6:
                    print(f"{name}, \t\t{price}")
                #item names over 6 letters are fine and only use one tab for the prices
                else:
                    print(f"{name}, \t{price}")

        print(f"Total: \t\t£{round(cart_total, 2)}")

        print(f"Your balance: \t£{round(user_balance, 2)}")

        ans = input("\nWhat would you like to do?\n1: Add balance\n2: Buy items\n3: Checkout\n4: Exit\n")



        if ans == "1":
            #runs the add_balance() function
            user_balance = add_balance()
            main_menu_flag_repeat = True

        elif ans == "2":
            #runs the buy_items() function
            cart, cart_total = buy_items()
            main_menu_flag_repeat = True
        
        elif ans == "3":
            discount, discounted_cart_total = calculate_discount(cart, cart_total)

            if user_balance < discounted_cart_total:
                input("Your balance is too low. Input more money to check out.")
                main_menu_flag_repeat = True
                continue

            change, order_number = checkout(user_balance, discounted_cart_total, order_number)

            change_calculation(change, order_number)

            print(f"Your balance is: £{round(user_balance, 2)}")
            print(f"Your discounted total is: £{round(discounted_cart_total,2)}")
            print(f"Your change is: £{round(change, 2)}")

            csv_flag = True

            while csv_flag:
                csv_flag = False

                csv_output = input(f"\nWould you like a CSV file for your receipt? Y or N\n").lower()

                if csv_output == "y":
                    make_csv_file(order_number, cart, cart_total, discount, discounted_cart_total, change)
                
                elif csv_output == "n":
                    continue
                
                else:
                    input("Invalid input. Press any key to try again.")
                    csv_flag = True



        elif ans == "4":
            #if the user exits, the while loop ends and the function ends.
            continue
        
        else:
            #if the input is invalid, repeats the while loop
            print("Invalid input.")
            main_menu_flag_repeat = True
            continue
  
main_menu()