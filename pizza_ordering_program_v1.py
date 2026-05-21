import random

# Check that users have entered a valid
# option based on a list
def string_checker(question, valid_ans):
    error = f"Please enter a valid option from the following list: {valid_ans}"

    while True:

        # Get user response and make sure it's lowercase
        user_response = input(question).lower()

        for var_item in valid_ans:
            # check if the user response is a word in the list


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




# Main Routine Starts here

# Intialise game variables


yes_no = ["yes","no"]



# Game Heading - game play starts here
print("Mario Mario's Pizza")
print()


# ask user if they want to see the instructions and display
# them if requested
want_instructions = string_checker("Do you want to read the instructions? ",yes_no)

# checks users enter yes (y) or no (n)
if want_instructions == "yes":
    instruction()

