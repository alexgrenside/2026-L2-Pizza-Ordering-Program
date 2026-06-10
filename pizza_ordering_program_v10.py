# Check that users have entered a valid option based on a list
def string_checker(question, valid_ans):

    error = f"Please enter a valid option from the following list: {valid_ans}"

    while True:

        user_response = input(question).lower()

        for var_item in valid_ans:

            # Full word check
            if user_response == var_item:
                return var_item

            # Shortcut check
            words = var_item.replace("&", "").split()
            shortcut = ""

            for word in words:
                shortcut += word[0]

            if user_response == shortcut:
                return var_item

        print(error)
        print()


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

Type x in the ordering section to finish your order and continue to the cart.
Type back in the cart to continue ordering. 
Each pizza will add two minutes to the total delivery time + 10 minutes
Each pizza will add two minutes to the pickup time
''')


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


# Menu display
def menu():
    print('''
📜📜📜MENU📜📜📜

🍕🍕PIZZA🍕🍕
1. Pepperoni (p) $5
2. Cheese (c) $4
3. Ham & Cheese (hc) $5
4. Vegetarian (v) $5
5. Cheesy Garlic (cg) $5
6. Buffalo Chicken (bc) $7
7. Onion (o) $10000
8. Meatlovers (m) $7
9. Hawaiian (h) $5
10. Garlic Prawn (gp) $10
11. Mario Special (ms) $10

🍟🍟SIDES🍟🍟
1. Fries (f) $2
2. Coca Cola (cc) $1
3. Garlic Bread (gb) $3

Type x to finish order and continue to cart.
''')


# Variables
yes_no = ["yes", "no"]
delivery_options = ["delivery", "pickup"]


menu_items = [
    "pepperoni",
    "cheese",
    "ham & cheese",
    "vegetarian",
    "cheesy garlic",
    "buffalo chicken",
    "onion",
    "meatlovers",
    "hawaiian",
    "garlic prawn",
    "mario special",

    # sides
    "fries",
    "coca cola",
    "garlic bread",

    "x"
]

price = [
    5, 4, 5, 5, 5, 7, 10000, 7, 5, 10, 10,
    2, 1, 3]
cart = []

# Heading
print("🍕🍕Mario's Pizza🍕🍕")
print("Welcome to Mario's Pizza")
print()

# Phone number
while True:
    phone_number = input("What is your phone number? ")

    if phone_number.strip() != "":
        break

    print("Invalid address Please try again.")

print(f"Your phone number is: {phone_number}")
# Instructions
want_instructions = string_checker(
    "Do you want to read the instructions? ",
    yes_no
)

if want_instructions == "yes":
    instruction()

# Delivery or pickup
order_type = string_checker(
    "Do you want delivery or pickup? ",
    delivery_options
)

if order_type == "delivery":
    while True:
        address = input("What is your address? ")

        if address.strip() != "":
            break

        print("Invalid address Please try again.")

    print(f"Your address is: {address}")
else:
    print("Ok, your pickup time will be decided at the end")
    print()

# Show menu
ask_menu = string_checker(
    "Would you like to see the menu? ",
    yes_no
)

if ask_menu == "yes":
    menu()

# Ordering loop
while True:

    ask_order = string_checker(
        "What would you like to order? ",
        menu_items
    )

    if ask_order == "x":
        print("\nOrder finished.")
        break

    ask_amount = int_check(
        "How many would you like? ",
        1,
        99
    )

    cart.append([ask_order, ask_amount])

    print(f"{ask_amount} {ask_order} added to your cart")
    print()

# Cart / confirmation loop
# Cart / confirmation loop
while True:

    print("\n🛒🛒🛒 YOUR CART 🛒🛒🛒")

    if len(cart) == 0:
        print("Your cart is empty.")

    total_pizzas = 0
    total_cost = 0

    for item in cart:
        pizza = item[0]
        quantity = item[1]
        total_pizzas += quantity

        # Find pizza price
        pizza_index = menu_items.index(pizza)
        pizza_price = price[pizza_index]

        item_cost = pizza_price * quantity
        total_cost += item_cost

        print(f"{quantity} x {pizza} = ${item_cost}")

    print(f"\n💰 Total Cost: ${total_cost}")

    # Time calculations
    pickup_time = total_pizzas * 2

    if order_type == "delivery":
        delivery_time = pickup_time + 10
        print(f"\n🚚 Estimated delivery time: {delivery_time} minutes")
    else:
        print(f"\n🍕 Estimated pickup time: {pickup_time} minutes")

    cart_choice = input(
        "\nType 'back' to continue ordering or press Enter to confirm order: "
    ).lower()

    if cart_choice == "back":

        while True:

            ask_order = string_checker(
                "What pizzas would you like? ",
                menu_items
            )

            if ask_order == "x":
                break

            ask_amount = int_check(
                "How many would you like? ",
                1,
                99
            )

            cart.append([ask_order, ask_amount])

            print(f"{ask_amount} {ask_order} added to your cart")
            print()

    else:
        print("\n💳💳✅ Order confirmed!✅💳💳")
        print(f"💰 Total Paid: ${total_cost}")

        if order_type == "delivery":
            print(
                f"Your order will be delivered in approximately "
                f"{delivery_time} minutes to {address}. "
                f"We will text {phone_number} when the order is close"
            )
        else:
            print(
                f"Your order will be ready for pickup in approximately "
                f"{pickup_time} minutes. Please go to 91774 Mario Rd, "
                f"We will text {phone_number} when the pizza is almost ready"
            )

        break