menu = [
    {"Popcorn": 5.00},
    {"Soda": 3.00},
    {"Candy": 2.50},
    {"Nachos": 4.50},
    {"Hot Dog": 4.00}
]
for item in menu:
        print(f"{list(item.keys())[0]}: ${list(item.values())[0]:5.2f}")
cart=[]
total = 0
def add_to_cart(Item):
    cart.append(Item)
    global total
    total += list(Item.values())[0]
def view_cart():
    print("Items in your cart:")
    for item in cart:
        print(f"{list(item.keys())[0]}: ${list(item.values())[0]:5.2f}")
    print(f"Total: ${total:5.2f}")
def checkout():
    print("Checking out...")
    view_cart()
    print("Thank you for your purchase!")
def clear_cart():
    global cart, total
    cart = []
    total = 0
    print("Cart cleared.")
def menu_options():
    print("\nMenu Options:")
    print("1. View Menu")
    print("2. Add Item to Cart")
    print("3. View Cart")
    print("4. Checkout")
    print("5. Clear Cart")
    print("6. Exit")
while True:
    menu_options()
    choice = input("Select an option (1-6): ")
    if choice == '1':
        for item in menu:
            print(f"{list(item.keys())[0]}: ${list(item.values())[0]:5.2f}")
    elif choice == '2':
        item_name = input("Enter the name of the item to add to cart: ")
        found = False
        for item in menu:
            if list(item.keys())[0].lower() == item_name.lower():
                add_to_cart(item)
                print(f"{item_name} added to cart.")
                found = True
                break
        if not found:
            print("Item not found in menu.")
    elif choice == '3':
        view_cart()
    elif choice == '4':
        checkout()
        break
    elif choice == '5':
        clear_cart()
    elif choice == '6':
        print("Exiting the program.")
        break
    else:
        print("Invalid option. Please try again.")

