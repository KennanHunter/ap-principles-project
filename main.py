import random
import string

# Create lists of possible characters
# for the different possible selections
# Consult lines 21-35 for usage
letters = list(string.ascii_letters)
numbers = list("0123456789")
symbols = list(r"~!@#$%^&*()_-+=|\{}[];:\"'<,>.?/")

# The different possible options that will be used
# to randomly generate the password
input_options = ["letters", "numbers", "symbols"]

# Return a string with the given random
# choice possibilities and length
def generate_password(user_selection: list[str], length: int):
    # Create an empty password string that will be added to later
    password = ""

    # Loop through a range with however many characters we want to produce
    for _ in range(0, length):
        # Create an empty list that has every possible character
        random_term_options = []

        # if the user selected letters, add all letters to that list
        if "letters" in user_selection:
            random_term_options.extend(letters)

        # if the user selected numbers, add all numbers (0-9) to that list
        if "numbers" in user_selection:
            random_term_options.extend(numbers)

        # if the user selected symbols, add all common symbols to that list
        if "symbols" in user_selection:
            random_term_options.extend(symbols)

        password += random.choice(user_selection)

    return password

# Function that handles accepting user input and printing out the output
def main():
    print("Kennan's Password Generator")
    print("Select what you want, separating each selector with a space")
    print("Options:")

    # Show the different options
    for option in input_options:
        print(option.title())

    # Provide an example as the directions aren't very clear
    print("\nEx input: \"letters symbols\" creates a password with letters, symbols, but no numbers")

    # Take in the user input
    # make every character lowercase (in case it isn't),
    # strip all whitespace from the left and right
    # and separate it into words
    # user_selection is a list of strings here
    user_selection = input("Your Selection: ").lower().strip().split()

    # If the user doesn't input anything, we check the length and kill the program
    if len(user_selection) == 0:
        print("Must enter a selection, exiting")
        exit()

    # if any of user_selection doesn't exist in the known
    # input options ("letters", "numbers", "symbols"), then
    # tell the user
    for selection in user_selection:
        if selection not in input_options:
            print("Unrecognized option: ", selection)

    # If the user inputs a length that can't be converted to an integer
    # such as a decimal or text, we exit early
    try:
        user_length = int(input("How long do you want your password to be: "))
    except ValueError:
        print("Length must be an integer, exiting program")
        exit()

    # Pass the values we collected into the generate_password function
    password = generate_password(user_selection, user_length)

    # Tell the user what password was generated
    print("Your password is: \n" + password)


# Run the main function that handles interacting with the user
main()
