#Define the menu of resturant
menu = {
    'pizza':1500,
    'Pasta':1000,
    'Burger':500,
    'Salad':200,
    'Coffee':400,
}

#Greet

print("Welcome to Adi resturant")
print("pizza: Rs1500\nPasta: Rs1000\nBurger: Rs500\nSalad: Rs200\nCoffee: Rs400")


order_total = 0

item_1 = input("Enter the name of item you want to order = ")
if item_1 in menu:
    order_total += menu [item_1]
    print(f"your item {item_1} has been added to your order")

else:
    print(f"please order something else we can serve you")

another_order = input("do you want to add another item? (Yes/No) ")
if another_order == "Yes":
    item_2 = input("Enter the name of second item = ")
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"item {item_2} has been added to order")
    else:
        print(f"ordered item {item_2} is not available!")

print(f"The total amount of items to pay is {order_total}")