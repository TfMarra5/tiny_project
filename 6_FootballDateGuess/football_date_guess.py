import json
import random
import os

RESET = "\033[0m"
GREEN = "\033[32m"
RED = "\033[31m"
YELLOW = "\033[33m"
CYAN = "\033[36m"

os.system("cls" if os.name == "nt" else "clear")

f = open("words.json", encoding="utf-8")
words = json.load(f)
f.close()

choice_c = random.choice(list(words.keys()))

print(CYAN + "====================================" + RESET)
print(CYAN + "          FOOTBALL TERMO            " + RESET)
print(CYAN + "====================================" + RESET)
print("Guess the date in format " + YELLOW + "DDMMAAAA" + RESET + ".")
print("Tip is always related to football.\n")

n_choices = 5

while n_choices > 0:
    print(f"You have {n_choices} attempts left.")
    print("Tip: " + YELLOW + words[choice_c] + RESET)

    answer_user = input("Date (DDMMAAAA): ")

    print()

    if not answer_user.isdigit():
        print(RED + "The date must contain only numbers." + RESET)
        print("------------------------------------")
        continue

    if len(answer_user) != len(choice_c):
        print(RED + "The length of the date is incorrect. Use 8 digits (DDMMAAAA)." + RESET)
        n_choices -= 1
        print("------------------------------------")
        continue

    if answer_user == choice_c:
        print(GREEN + "Congratulations! You guessed it!" + RESET)
        print("Event:", YELLOW + words[choice_c] + RESET)
        break
    else:
        print(RED + "Wrong answer. Try again." + RESET)
        n_choices -= 1
        print("------------------------------------")

else:
    print()
    print(RED + "No attempts left." + RESET)
    print("The correct date was:", YELLOW + choice_c + RESET)
    print("Event:", YELLOW + words[choice_c] + RESET)
