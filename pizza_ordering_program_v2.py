
# Check that users have entered a valid
# option based on a list
def string_checker(question, valid_ans):
    error = f"Please enter a valid option from the following list: {valid_ans}"

    while True:

        # Get user response and make sure it's lowercase
        user_response = input(question).lower()

        for var_item in valid_ans:
            # check if the user response is a word in the list
            if user_response == var_item:
                return var_item

            # check if the user response is the same as
            # the first letter of an item in the list
            if user_response == var_item[0]:
                return var_item

        # print error if user does not enter something that is valid
        print(error)
        print()


# Displays instructions
def instruction():
    print('''

**** Instructions ****

Pizza Pizza Pizza Pizza
Pizza Pizza Pizza Pizza
Pizza Pizza Pizza Pizza
Pizza Pizza Pizza Pizza
Pizza Pizza Pizza Pizza
Pizza Pizza Pizza Pizza
 ''')

# variables
yes_no = ["yes","no"]
delivery_options = ["delivery","pickup"]

# Heading - starts here
print("🍕🍕Mario's Pizza🍕🍕")
print("Welcome to Mario's Pizza")


# ask user if they want to see the instructions and display them if requested
want_instructions = string_checker("Do you want to read the instructions? ",yes_no)

# checks users enter yes (y) or no (n)
if want_instructions == "yes":
    instruction()

# ask user if they want delivery or pickup
order_type = string_checker("Do you want your pizza to be delivered or do you want to pickup your pizza? ",delivery_options)

if order_type == "delivery":
    print("ok bro")

elif order_type == "pickup":
    print("yeah")
