
import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation

    password = random.choice(string.ascii_uppercase)
    password = password + random.choice(string.ascii_lowercase)
    password = password + random.choice(string.digits)
    password = password + random.choice(string.punctuation)

    for i in range(length - 4):
        password = password + random.choice(characters)

    password = list(password)
    random.shuffle(password)

    return "".join(password)


length = int(input("Enter password length (minimum 4): "))

if length >= 4:
    print("Generated Password:", generate_password(length))
else:
    print("Please enter a length of at least 4.")
