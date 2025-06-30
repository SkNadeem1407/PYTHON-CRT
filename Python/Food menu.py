# write a python program
# 1. to display the menu of the food items (list)
# 2. create a tuple of prices with respect to food items list
# 3. read the input from the user for ordering the food including quantity
#    if it exists in the menu -- confirm order
#    if not, print a message --- not available
# 4. while billing read phone no., feedback, read tip amount
# 5. add 18% gst to the bill and print the bill if bill>0
Food_items = []
starters = ("Chicken Majestic,Apollo Fish,Mutton Kebabs,Chilli Prawns,Steamed Crab")
price = (240, 250, 260, 270, 280)
while (True):
    print("*************** MENU ***************")
    print("1. Display the food items")
    print("2. Prices of the food items")
    print("3. Ordering food items.")
    print("4. Billing food items.")
    print("5. Exit")
    print("------------------------------------")
    Choice = int(input("Enter your Choice: "))
    if (Choice >= 1 and Choice <= 5):
        if (Choice == 1):

            print(starters)
            break
        elif (Choice == 2):
            print(starters)
            print("Prices of the food items:")
            print(price)
            break
        elif (Choice == 3):
            print("Enter the food items you want to order:")
            order = input()
            if order in starters:
                index = starters.index(order)
                quantity = int(input("Enter the quantity: "))
                Food_items.append((order, quantity, price[index] * quantity))
                print(f"Order confirmed for {quantity} {order}(s).")
            else:
                print("Sorry, the item is not availble.")
        elif (Choice == 4):
            if not Food_items:
                print("No items ordered yet.")
            else:
                total_bill = sum(item[2] for item in Food_items)
                gst = total_bill * 0.18
                final_bill = total_bill + gst
                print("Bill:")
                for item in Food_items:
                    print(f"{item[1]}x{item[0]}@{item[2] / item[1]}={item[2]}")
                    print(f"Total: {total_bill}")
                    print(f"GST (18%): {gst}")
                    print(f"Final Bill: {final_bill}")
                    phone_no = input("Enter your phone number: ")
                    feedback = input("Please provide your feedback: ")
                    tip = float(input("Enter tip amount:"))
                    final_bill += tip
                    print(f"Total amount to be paid (including tip): {final_bill}")
                    Food_items.clear()
        elif (Choice == 5):
            print("Thank you for visiting our restraunt")
            break
        else:
            print("Invalid choice. Please try again.")