import random
import string

letters = list(string.ascii_letters)
numbers = list("0123456789")
symbols = list(r"~!@#$%^&*()_-+=|\{}[];:\"'<,>.?/")

input_options = ["letters", "numbers", "symbols"]


def generate_password(user_selection: list[str], length):
    password = ""

    for _ in range(0, length):
        random_term_options = []

        if "letters" in user_selection:
            random_term_options.extend(letters)

        if "numbers" in user_selection:
            random_term_options.extend(numbers)

        if "symbols" in user_selection:
            random_term_options.extend(symbols)

        password += random.choice(user_selection)

    return password


def main():
    print("Kennan's Password Generator")
    print("Select what you want, separating each selector with a space")
    print("Options:")
    for option in input_options:
        print(option.title())
    print("\nEx input: \"letters symbols\" creates a password with letters, symbols, but no numbers")

    user_selection = input("Your Selection: ").lower().strip().split()

    for selection in user_selection:
        if selection not in input_options:
            print("Unrecognized option: ", selection)

    user_length_raw = input("How long do you want your password to be: ")

    try:
        user_length = int(user_length_raw)
    except ValueError:
        print("Length must be an integer, exiting program")
        exit()

    print(generate_password(user_selection, user_length))


main()
