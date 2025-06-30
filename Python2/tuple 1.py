'''''
tuple=(('a','b','c'),('A','B','C'),(1,2,3),(-1,-2,-3))
print(tuple)
for i in tuple:
    print(i,type(tuple)
#write a python program to create a tuple of programming languages to find max element and min element and print the sorted tuple and  reversed tuple
#write a python program to create a tuple of names and print the original tuple and print the names which have the length 5 from the tuple'''''
Food_items = []
starters = ('Fish fry', 'Chicken 65', 'Mutton Kebabs', 'Loose prawns', 'Crab Roast')
prices = (150, 220, 100, 225, 350)

while True:
    print("\n*************** MENU ***************")
    print("1. Display the food items")
    print("2. Prices of the food items")
    print("3. Ordering food items")
    print("4. Billing food items")
    print("5. Exit")
    print("------------------------------------")

    Choice = int(input("Enter your Choice: "))

    if Choice == 1:
        print(f"Starters available: {starters}")

    elif Choice == 2:
        for item, price in zip(starters, prices):
            print(f"{item} - ₹{price}")

    elif Choice == 3:
        print("Enter the food item to order:")
        order = input()
        if order in starters:
            Food_items.append(order)
            print(f"{order} added to your order.")
        else:
            print("Sorry, item not available.")

    elif Choice == 4:
        if not Food_items:
            print("No items ordered yet.")
            continue
        total = 0
        print("\n----- Bill Summary -----")
        for item in Food_items:
            index = starters.index(item)
            item_price = prices[index]
            total += item_price
            print(f"{item} - ₹{item_price}")
        gst = total * 0.18
        final_amount = total + gst
        print(f"Subtotal: ₹{total}")
        print(f"GST (18%): ₹{gst:.2f}")
        print(f"Total Bill: ₹{final_amount:.2f}")
        Food_items.clear()

    elif Choice == 5:
        print("Exiting the menu. Thank you!")
        break

    else:
        print("Invalid Choice! Please select a valid option.")
