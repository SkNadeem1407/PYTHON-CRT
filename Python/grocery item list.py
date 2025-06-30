
Grocery_items=['Rice','Dal','Wheat flour','Maida','Sugar','Salt']
prices=(1100,85,120,89,100,75)
cart_items=[]
cart_quantities=[]
while True:
    print("************* MENU *******************")
    print("1.Display the list of grocery items")
    print("2.Add items to the cart")
    print("3.To view the cart items")
    print("4.Update the quantity or item in the list")
    print("5.Generate the bill and exit")
    print("-----------------------------")
    Choice=int(input("Enter your choice: "))
    if (Choice>=1 and Choice<=5):
        if Choice==1:
            print(f"list of grocery items: {Grocery_items}")
        elif Choice==2:
            required_items=input("Enter the required items(comma-separated): ").split(",")
            for items in required_items:
                items=items.strip()
                if items in Grocery_items:
                    quantity=int(input(f"Enter in kg {items} in kg: "))
                    cart_items.append(items)
                    cart_quantities.append(quantity)
                    print(f"{quantity} kg of{required_items} added to cart")
                else:
                 print(f"{required_items} not found in grocery list")
        elif Choice==3:
            if cart_items and len(cart_items) == len(cart_quantities):
                print("cart items")
                for i in range(len(cart_items)):
                    print(f"{cart_items[i]} - {cart_quantities[i]} kg")
            else:
                print("cart is empty")
        elif Choice==4:
            update_item = input("Enter the item to update: ").strip()
            if update_item in cart_items:
                index = cart_items.index(update_item)
                new_quantity = int(input(f"Enter the new quantity in kg for {update_item}: "))
                cart_quantities[index] = new_quantity
                print(f"{update_item} quantity updated to {new_quantity} kg")
            else:
                 print("item not found in cart")
        elif Choice==5:
            print("************Bill***********")
            total=0
            for i in range(len(cart_items)):
                item= cart_items[i]
                quantity=cart_quantities[i]
                prices_per_kg=prices[Grocery_items.index(item)]
                if quantity>10:
                    print("1kg discount")
                    billed_quantity =quantity-1
                else:
                    billed_quantity=quantity
                    print(f"{item}: {quantity} kg (1 kg free) x {prices_per_kg} = {billed_quantity * prices_per_kg}")
                total += billed_quantity * prices_per_kg
            if total>1000:
                discount=total*0.10
                total-=discount
                print("10% discount applied: ",discount)
            gst = total * 0.25
            final_total = total + gst
            print("GST (25%):", gst)
            print("Total amount payable:", final_total)
            print("Thank you for shopping!")
            break









