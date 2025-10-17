#exercise 2
'''
numbers = [0,1,2,3]

x = 5

print(numbers[0])
print(numbers[-1])

numbers[0] = x

print(numbers)

numbers.append(15)

print(numbers)
'''
#exercise 3
'''
prices = [4, 1, 10, 9, 6]

print(max(prices))
print(min(prices))

first_last_total = prices[0] + prices[-1]

prices.append(first_last_total)

prices.reverse()
print(prices)

average_price = sum(prices) / len(prices)

print(average_price)
'''
#exercise 4

'''
days = ("Monday", "Tuesday", "Sunday", "Friday")

print(f"{days[0]} {days[-1]}")
print(days[:-1])

print(days)
'''

#exercise 5
'''
product1 = ("Water", 1.5)
product2 = ("Soda", 2.0)
product3 = ("Chocolate", 2.5)

print(f"{product1[0]}, {product1[1]}\n{product2[0]}, {product2[1]}\n{product3[0]}, {product3[1]}\n ")

products = (product1, product2, product3)

r = ', '.join(map(str, products))

print(r)

print(products[0])

'''

#exercise 6
'''
fruits_set = {"apple", "banana", "orange", "apple", "banana"}

print(fruits_set)

fruits_set.add("kiwi")

print(fruits_set)

fruits_set.remove("orange")

print(fruits_set)

print(len(fruits_set))
'''

#exercise 7
'''
workshop1 = {"Alice", "Bob", "Charlie"}
workshop2 = {"Bob", "Diana", "Eve"}

in_both = workshop1 & workshop2

print(f"Students found in both: {in_both}")

at_least_1 = workshop1 | workshop2

print(f"Students found in at least one workshop: {at_least_1}")

only_one = workshop1 - workshop2

print(f"Students who only attended workshop 1: {only_one}")
'''

#exercise 8
'''
locked_palette = ("Red", "Green", "Blue", "Purple", "Yellow")

extra_colours = ("White","Black","Cyan","Lime","Pink")

full_palette = locked_palette + extra_colours

editable_palette = list(full_palette)

editable_palette.append("Light Grey")

print(editable_palette)

unique_colours = set(editable_palette)

theme_colours = {"Pink", "Green", "Red", "Purple", "Dark Grey"}

common_colours = unique_colours & theme_colours

print(common_colours)
'''

#Exercise 9/10
'''
students = {
    "Name": ["Alice", "Bob", "Charlie", "Diana"],
    "Score": ["85","92","78","90"]
}
print(students)
'''

#Exercise 12 part 1
'''
person1 = {
    'name':'Alice',
    'age':'25',
    'message':'Loves programming'
}

person2 = {
    'name':'Bob',
    'age':'30',
    'message':'Enjoys AI'
}

person3 = {
    'name':'Charlie',
    'age':'22',
    'message':'Learning python'
}

people = [person1, person2, person3]

for i in people:
    print(i["message"])

people[2]["message"] = "completed Python"

print(people)
'''


#Exercise 12 part 2
'''
customer = {
    'Name':'Alex',
    'Age':'18',
    'Cars':["Ford", "Land Rover"],
}

print(f"{customer["Name"]}, {customer["Cars"]}")

customer["Cars"].append("Ferrari")
print(customer["Cars"])
'''

#Exercise 13
#1. float
#2. string
#3. string

#Exercise 14
'''
num_list = [0,1,2,3,4,5,6,7,8,9]

let_list = ["A","B","C","D","E","F","G","H","I","J"]

number_to_letters = zip(num_list, let_list)

numlet_dict = dict(number_to_letters)

print(numlet_dict)

print(numlet_dict[2], numlet_dict[0], numlet_dict[5], numlet_dict[4])
'''

#Exercise 15
'''
numbers = [1,2,2,3,4,3]

unique_list = set(numbers)

print(unique_list)
'''

#Exercise 16
'''
numbers = [1,2,3,4]
print(numbers)
numbers.reverse()
print(numbers)
'''

#Exercise 17
'''
marks = []
marks.append(98)
marks.append(95)
marks.append(81)
print(marks)
total = sum(marks)

print(total)
'''

#Exercise 18
'''
message = ""

message += "Hello"

message += " Alex"

print(message)
'''

#Exercise 19
'''
import random
roll1 = random.randint(1,6)
print(roll1)

roll2 = random.randint(1,6)
print(roll2)

total = roll1 + roll2

if total > 8:
    print("bigger than 8")
'''

#Exercise 20
'''
for i in range (1,200):
    i += i

print(i)
'''
