def main():

    inventory = {
        1 :{'Name': 'Water','Price': 1.20, 'Stock' : 5}, 
        2 :{'Name': 'Soda','Price': 1.50, 'Stock' : 5}, 
        3 :{'Name': 'Chocolate','Price': 2.50, 'Stock' : 5}, 
        4 :{'Name': 'Crisps','Price': 1.40, 'Stock' : 5}, 
        5 :{'Name': 'Sandwich','Price': 3.80, 'Stock' : 5}, 
        }

    def vending_machine():

        flag = True
        sum = 0

        while flag:
        
            print("---------Welcome to the vending machine---------")

            ans = input(f"What would you like to do? Your sum is: £{sum}\n1: Input coins\n2: Purchase an item\n3. Exit\n")

            if ans == "1":
                sum = input_money()

            elif ans == "2":
                purchase_items()
            
            elif ans == "3":
                flag = False
                continue
            
            else:
                input("Invalid input. Press any key to try again.")
                continue


    def input_money():
        print("------------------------------------------------")
        flag = True
        sum = 0

        while flag:
            ans = input(f"Your sum is: £{round(sum, 2)}\nHow much do you want to enter? The machine accepts: £1, £2, 50p and 20p.\n1. £1\n2. £2\n3. 50p\n4. 20p\n5. Return\n")

            if ans == "1":
                sum += 1
            
            elif ans == "2":
                sum += 2
            
            elif ans == "3":
                sum += 0.5
            
            elif ans == "4":
                sum += 0.2
            
            elif ans == "5":
                flag = False
                return sum


    def purchase_items():
        print("------------------------------------------------\nPlease choose an item:")
        for key, value in inventory.items():
            print(f'{key}: {value['Name']} \tPrice: {value['Price']} \tStock: {value['Stock']}')
        print("5: Return")

    def print_csv():
        print()

    vending_machine()

main()