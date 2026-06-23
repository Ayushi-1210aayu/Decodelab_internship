"""Random Password Generator for Project 3.

Features:
- ask for password length
- generate random complex passwords
- support letters, numbers, and special characters
- use the random module for security
"""

import random
import string


def generate_password(length, use_special=True):
    """Generate a random password of the specified length.
    
    Args:
        length: The desired password length
        use_special: Include special characters (True/False)
    
    Returns:
        A random password string
    """
    characters = string.ascii_letters + string.digits
    if use_special:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    return password


def main():
    print("Welcome to the Random Password Generator!")
    print("This tool creates secure, random passwords.\n")

    while True:
        length_input = input("Enter desired password length (or 'quit' to exit): ").strip()
        
        if length_input.lower() == 'quit':
            print("Exiting password generator. Goodbye!")
            break

        try:
            length = int(length_input)
            if length < 4:
                print("Password length must be at least 4 characters.")
                continue
            if length > 128:
                print("Password length cannot exceed 128 characters.")
                continue
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        use_special_input = input("Include special characters? (yes/no, default: yes): ").strip().lower()
        use_special = use_special_input != 'no'

        password = generate_password(length, use_special)
        print(f"\nGenerated password: {password}")
        print(f"Password length: {len(password)}\n")


if __name__ == '__main__':
    main()