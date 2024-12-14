import random
import string

def generate_password(length=12):
    """
    Generates a secure random password.
    
    :param length: Length of the password (default is 12)
    :return: A randomly generated password as a string
    """
    if length < 6:
        raise ValueError("Password length must be at least 6 characters.")

    # Character sets
    letters = string.ascii_letters  # a-z, A-Z
    digits = string.digits          # 0-9
    special_chars = string.punctuation  # Special characters like !@#$%^&*

    # Combine all character sets
    all_chars = letters + digits + special_chars

    # Ensure the password includes at least one character from each set
    password = [
        random.choice(letters),
        random.choice(digits),
        random.choice(special_chars)
    ]

    # Fill the rest of the password with random characters
    password += random.choices(all_chars, k=length - len(password))

    # Shuffle the password to avoid predictable patterns
    random.shuffle(password)

    # Return the password as a string
    return ''.join(password)

if __name__ == "__main__":
    try:
        length = int(input("Enter the desired password length (minimum 6): "))
        new_password = generate_password(length)
        print(f"Generated password: {new_password}")
    except ValueError as e:
        print(f"Error: {e}")