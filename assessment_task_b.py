inventory = {
    1 :{'Name': 'Water','Price': 1.20, 'Stock' : 5}, 
    2 :{'Name': 'Soda','Price': 1.50, 'Stock' : 5}, 
    3 :{'Name': 'Chocolate','Price': 2.50, 'Stock' : 5}, 
    4 :{'Name': 'Crisps','Price': 1.40, 'Stock' : 5}, 
    5 :{'Name': 'Sandwich','Price': 3.80, 'Stock' : 5}, 
    }

def vending_machine():

    flag = True

    while flag:
    
        print("---------Welcome to the vending machine---------")

        ans = input("What would you like to do?\n1: Input coins\n2: Purchase an item\n")

        if ans == "1":
            input_money()

        elif ans == "2":
            purchase_items()
        
        else:
            input("Invalid input. Press any key to try again.")
            continue


def input_money():
    print()

def purchase_items():
    print("------------------------------------------------")
    for key, value in inventory.items():
        print(f'{key}: {value['Name']} \tPrice: {value['Price']} \tStock: {value['Stock']}')
    print()

def print_csv():
    print()

vending_machine()