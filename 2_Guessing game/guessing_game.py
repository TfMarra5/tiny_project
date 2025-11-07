import random

print ("Welcome to the Guessing Game!")
choice_number = input ("Type the max number you want to guess up to: ")
number_to_guess = random.randint(1, 100)

while not choice_number.isdigit():
    print("Please type a number!\n")
    choice_number = input("Type a number: ")
    continue

choice_number = int(choice_number)
print("Okay, the max number is", choice_number)

random_numer = random.randint(0, choice_number)

n_choices = 0

while True:
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else :
        print("Please type a number!\n")
        continue
    
    n_choices = n_choices + 1
    if user_guess == random_numer:
        print("You're right! The number was ", random_numer)
        break
    
    elif user_guess > random_numer:
        print("Too high! Try again.\n")
    else:
        print("Too low! Try again.\n")

print ("You got it in", n_choices, "tries!")