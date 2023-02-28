import random
import string

def generate_password(length):
    # Define the character sets to be used in the password
    uppercase_letters = string.ascii_uppercase
    lowercase_letters = string.ascii_lowercase
    digits = string.digits
    special_chars = string.punctuation

    # Combine the character sets into a single pool of characters
    all_chars = uppercase_letters + lowercase_letters + digits + special_chars

    # Shuffle the characters to make the password more random
    shuffled_chars = random.sample(all_chars, len(all_chars))

    # Select a subset of the shuffled characters to form the password
    password = ''.join(random.sample(shuffled_chars, length))

    return password

# Prompt the user for the desired length of the password
length = int(input("Enter the length of the password: "))

# Generate a password with the specified length
password = generate_password(length)

# Print the generated password
print("Your generated password is:", password)
