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

