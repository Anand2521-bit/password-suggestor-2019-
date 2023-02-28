import random
import string

def generate_password(length):
    uppercase_letters = string.ascii_uppercase
    lowercase_letters = string.ascii_lowercase
    digits = string.digits
    special_chars = string.punctuation

    all_chars = uppercase_letters + lowercase_letters + digits + special_chars

    shuffled_chars = random.sample(all_chars, len(all_chars))

    password = ''.join(random.sample(shuffled_chars, length))

    return password

length = int(input("Enter the length of the password: "))

password = generate_password(length)
# Print the password
print("Your generated password is:", password)
