# Check that users have entered a valid
# option based on a list
def string_checker(question, valid_ans):

    error = f"Please enter a valid option from the following list: {valid_ans}"

    while True:

        # Get user response and make sure it's lowercase
        user_response = input(question).lower()

        for var_item in valid_ans:

            # Check if user typed full word
            if user_response == var_item:
                return var_item

            # Create shortcut using first letter of each word
            words = var_item.replace("&", "").split()
            shortcut = ""

            for word in words:
                shortcut += word[0]

            # Check shortcut
            if user_response == shortcut:
                return var_item

        # print error if user does not enter something that is valid
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
p = pickup
p = pepperoni
hc = ham & cheese
bc = buffalo chicken
gp = garlic prawn
ms = mario special

Type x in the ordering section to finish your order and continue to the cart.
''')


# Integer checker
def int_check(question, low, high):

    """Checks users enter an integer between two values"""

    error = f"Oops - please enter an integer between {low} and {high}."

    while True:

        try:
            # Change the response to an integer
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

1. Pepperoni (p)
2. Cheese (c)
3. Ham & Cheese (hc)
4. Vegetarian (v)
5. Cheesy Garlic (cg)
6. Buffalo Chicken (bc)
7. Onion (o)
8. Meatlovers (m)
9. Hawaiian (h)
10. Garlic Prawn (gp)
11. Mario Special (ms)

Type x to finish order and continue to cart.
''')


# Main Routine goes here

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
    "x"
]

# Cart
cart = []

# Heading
print("🍕🍕Mario's Pizza🍕🍕")
print("Welcome to Mario's Pizza")
print()

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
    print("House address and stuff")
    print()

elif order_type == "pickup":
    print("Ok, come in __ time")
    print()

# Ask to see menu
ask_menu = string_checker(
    "Would you like to see the menu? ",
    yes_no
)

if ask_menu == "yes":
    menu()

# Ordering loop
while True:

    ask_order = string_checker(
        "What pizzas would you like? ",
        menu_items
    )

    # Exit code
    if ask_order == "x":
        print()
        print("Order finished.")
        break

    # Ask quantity
    ask_amount = int_check(
        "How many would you like? ",
        1,
        99
    )

    # Add to cart
    cart.append([ask_order, ask_amount])

    # Confirm order
    print(f"{ask_amount} {ask_order} added to your cart")
    print()

# Display cart
print("\n🛒🛒🛒 YOUR CART 🛒🛒🛒")

if len(cart) == 0:
    print("Your cart is empty.")

else:
    for item in cart:
        pizza = item[0]
        quantity = item[1]
        print(f"{quantity} x {pizza}")