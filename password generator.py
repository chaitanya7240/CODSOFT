import random

def generate_password(length, symbols, numbers):
    # Define character sets
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers_set = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols_set = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    # Initialize password list
    password_list = []

    # Add random letters
    password_list += [random.choice(letters) for _ in range(length)]

    # Add random symbols
    password_list += [random.choice(symbols_set) for _ in range(symbols)]

    # Add random numbers
    password_list += [random.choice(numbers_set) for _ in range(numbers)]

    # Shuffle the password list
    random.shuffle(password_list)

    # Convert password list to string
    password = ''.join(password_list)

    return password

def get_user_input():
    # Get user input for password criteria
    length = int(input("How many letters would you like to have in your password?\n"))
    symbols = int(input("How many symbols would you like to have?\n"))
    numbers = int(input("How many numbers would you like to have?\n"))

    return length, symbols, numbers

def main():
    print("Welcome to the Password Generator!")

    # Get user input for password criteria
    length, symbols, numbers = get_user_input()

    # Generate and print the password
    password = generate_password(length, symbols, numbers)
    print(f"Your password is: {password}")

# Run the program
if __name__ == "__main__":
    main()
