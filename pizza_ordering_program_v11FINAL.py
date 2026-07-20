import pandas as pd


# Check that users have entered a valid option based on a list
def string_checker(question, valid_ans):
    error = f"Please enter a valid option from the following list: {valid_ans}"
    while True:
        user_response = input(question).lower()
        for var_item in valid_ans:
            if user_response == var_item:
                return var_item
            shortcut = "".join(word[0] for word in var_item.replace("&", "").split())
            if user_response == shortcut:
                return var_item
        print(error)
        print()


# Integer checker
def int_check(question, low, high):
    error = f"Oops - please enter an integer between {low} and {high}."
    while True:
        try:
            response = int(input(question))
            if low <= response <= high:
                return response
            else:
                print(error)
        except ValueError:
            print(error)


# Displays instructions
def instruction():
    print('''
📃📃📃Instructions📃📃📃

Enter your delivery address if you pick delivery.
You can type shortcuts for everything or type the whole word.

Examples:
d = delivery
p = pepperoni
hc = ham & cheese
bc = buffalo chicken
gp = garlic prawn
ms = mario special

Shortcuts for sides:
gb = garlic bread
cs = coleslaw
fs = french fries
cc = choc chip cookies

Type x in the ordering section to finish your order and continue to the cart.
Type back in the cart to continue ordering.
A maximum of 5 pizzas can be ordered.
Each pizza will add two minutes to the total delivery time + 10 minutes.
Each pizza will add two minutes to the pickup time.
A delivery fee of $3 applies for delivery orders.
''')


# Menu data
pizza_df = pd.DataFrame({
    "Pizza": ["pepperoni", "cheese", "ham & cheese", "vegetarian", "cheesy garlic",
              "buffalo chicken", "onion", "meatlovers", "hawaiian", "garlic prawn", "mario special"],
    "Price": [5, 4, 5, 5, 5, 7, 10000, 7, 5, 10, 10]
})

sides_df = pd.DataFrame({
    "Side": ["garlic bread", "coleslaw", "french fries", "choc chip cookies"],
    "Price": [4, 3, 4, 5]
})

DELIVERY_FEE = 3
MAX_PIZZAS = 5
yes_no = ["yes", "no"]
delivery_options = ["delivery", "pickup"]
menu_items = list(pizza_df["Pizza"]) + ["x"]
side_items = list(sides_df["Side"]) + ["x"]


# Show menus
def show_menu(df, title, footer):
    print(f"\n{title}\n")
    num = 1
    for index, row in df.iterrows():
        name = row["Pizza"] if "Pizza" in df.columns else row["Side"]
        price = row["Price"]
        print(f"{num}. {name.title()} - ${price}")
        num += 1
    print(f"\n{footer}\n")


# Display cart and return (total_pizzas, total_cost)
def display_cart(cart_pizzas, cart_sides, order_type):
    print("\n🛒🛒🛒 YOUR CART 🛒🛒🛒")
    total_pizzas = 0
    total_cost = 0
    rows = []

    for pizza, qty in cart_pizzas:
        price = int(pizza_df.loc[pizza_df["Pizza"] == pizza, "Price"].values[0])
        item_cost = price * qty
        total_pizzas += qty
        total_cost += item_cost
        rows.append({"Item": pizza.title(), "Qty": qty, "Unit Price": f"${price}", "Subtotal": f"${item_cost}"})

    for side, qty in cart_sides:
        price = int(sides_df.loc[sides_df["Side"] == side, "Price"].values[0])
        item_cost = price * qty
        total_cost += item_cost
        rows.append({"Item": side.title(), "Qty": qty, "Unit Price": f"${price}", "Subtotal": f"${item_cost}"})

    if rows:
        order_df = pd.DataFrame(rows)
        order_df.index = range(1, len(order_df) + 1)
        print()
        print(order_df.to_string())
    else:
        print("Your cart is empty.")

    if order_type == "delivery":
        print(f"\n🚚 Delivery fee: ${DELIVERY_FEE}")
        total_cost += DELIVERY_FEE

    print(f"\n💰 Total Cost: ${total_cost}")
    return total_pizzas, total_cost


# Pizza ordering loop
def order_pizzas(cart_pizzas):
    while True:
        remaining = MAX_PIZZAS - sum(qty for _, qty in cart_pizzas)
        if remaining == 0:
            print(f"\nYou've reached the maximum of {MAX_PIZZAS} pizzas.")
            break
        ask_order = string_checker(f"What pizza would you like? (up to {remaining} more): ", menu_items)
        if ask_order == "x":
            print("\nPizza selection finished.")
            break
        ask_amount = int_check("How many would you like? ", 1, remaining)
        cart_pizzas.append([ask_order, ask_amount])
        print(f"{ask_amount} x {ask_order} added to your cart.\n")


# Sides ordering loop
def order_sides(cart_sides):
    show_menu(sides_df, "🍟🍟🍟 SIDES MENU 🍟🍟🍟", "Type x to finish adding sides and continue to cart.")
    while True:
        ask_side = string_checker("What side would you like? ", side_items)
        if ask_side == "x":
            print("\nSides selection finished.")
            break
        ask_amount = int_check("How many would you like? ", 1, 10)
        cart_sides.append([ask_side, ask_amount])
        print(f"{ask_amount} x {ask_side} added to your cart.\n")


# Main program
print("🍕🍕 Mario's Pizza 🍕🍕")

while True:
    print("\n" + "=" * 40)
    print("Welcome to Mario's Pizza")
    print("=" * 40 + "\n")

    # Customer details
    while True:
        customer_name = input("What is your name? ").strip()
        if customer_name:
            break
        print("Invalid name. Please try again.")

    phone_number = int_check("What is your phone number? ", 0, 9999999999)
    print(f"Thanks, {customer_name}! Your phone number is: {phone_number}")

    # Instructions
    if string_checker("Do you want to read the instructions? ", yes_no) == "yes":
        instruction()

    # Delivery or pickup
    order_type = string_checker("Do you want delivery or pickup? ", delivery_options)

    if order_type == "delivery":
        while True:
            address = input("What is your delivery address? ").strip()
            if address:
                break
            print("Invalid address. Please try again.")
        print(f"Your address is: {address}")
    else:
        address = None
        print("Ok, your pickup time will be decided at the end.\n")

    # Show menu
    if string_checker("Would you like to see the menu? ", yes_no) == "yes":
        show_menu(pizza_df, "📜📜📜 PIZZA MENU 📜📜📜", "Type x to finish ordering pizzas and move to sides.")

    # Order pizzas and sides
    cart_pizzas = []
    cart_sides = []
    order_pizzas(cart_pizzas)

    if string_checker("Would you like to add any sides? ", yes_no) == "yes":
        order_sides(cart_sides)

    # Cart / confirmation loop
    while True:
        total_pizzas, total_cost = display_cart(cart_pizzas, cart_sides, order_type)

        pickup_time = total_pizzas * 2
        if order_type == "delivery":
            delivery_time = pickup_time + 10
            print(f"\n🚚 Estimated delivery time: {delivery_time} minutes")
        else:
            print(f"\n🍕 Estimated pickup time: {pickup_time} minutes")

        cart_choice = input("\nType 'back' to continue ordering, 'cancel' to cancel order, or press Enter to confirm: ").lower().strip()

        if cart_choice == "back":
            order_pizzas(cart_pizzas)
            if string_checker("Would you like to add sides? ", yes_no) == "yes":
                order_sides(cart_sides)

        elif cart_choice == "cancel":
            print("\n❌ Order cancelled.")
            break

        elif cart_choice != "":
            print("\n⚠️  Please type 'back', 'cancel', or just press Enter to confirm.")

        else:
            print("\n💳💳✅ Order confirmed! ✅💳💳")
            display_cart(cart_pizzas, cart_sides, order_type)

            if order_type == "delivery":
                print(f"\n🚚 Your order will be delivered in approximately {delivery_time} minutes to {address}.")
                print(f"📋 Name: {customer_name}")
                print(f"🏠 Address: {address}")
                print(f"📱 Phone: {phone_number}")
                print(f"We will text {phone_number} when the order is close.")
            else:
                print(f"\n🍕 Your order will be ready for pickup in approximately {pickup_time} minutes.")
                print("Please go to 91774 Mario Rd.")
                print(f"📋 Name: {customer_name}")
                print(f"📱 Phone: {phone_number}")
                print(f"We will text {phone_number} when the pizza is almost ready.")
            break

    # New order or exit
    print()
    if string_checker("Would you like to place another order? ", yes_no) == "no":
        print("\nThanks for choosing Mario's Pizza! 🍕 Goodbye!")
        break
