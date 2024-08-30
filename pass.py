import random
import string

def generate_password(length, use_special_chars=True):
    """Generate a random password of specified length."""
    if length < 1:
        raise ValueError("Password length must be at least 1")

    # Define character sets for password generation
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    specials = string.punctuation if use_special_chars else ''

    # Combine all character sets
    all_characters = lower + upper + digits + specials

    if not all_characters:
        raise ValueError("No characters available for password generation")

    # Generate password
    password = ''.join(random.choice(all_characters) for _ in range(length))

    return password

def main():
    try:
        # Get user input for password length and complexity
        length = int(input("Enter the desired length of the password: "))
        use_special_chars = input("Include special characters (y/n)? ").strip().lower() == 'y'

        # Generate and display the password
        password = generate_password(length, use_special_chars)
        print(f"Generated Password: {password}")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
