import random
import string

def password_generator(length=8):
    ascii_options = string.ascii_letters
    number_options = string.digits
    punt_options = string.punctuation
    options = ascii_options + number_options + punt_options

    password_user = ""

    for i in range(0, length):
        digit = random.choice(options)
        password_user = password_user + digit
    return password_user

user_choice = input("Enter desired password length: ")

if user_choice.isdigit():
    user_choice = int(user_choice)
else:
    print("Invalid input.")
    quit()

response = password_generator(length=user_choice)
print(f"Generated password:\n{response}")
