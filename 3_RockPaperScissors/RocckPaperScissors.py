import random

user_score = 0
computer_points = 0

options = ['r', 'p', 's']
names = {'r': '🪨  Rock', 'p': '📄 Paper', 's': '✂️ Scissors'}
valid = {'r', 'p', 's', 'q'}
line_length = 35

while True:
    user_choice = input("Choose your weapon: R(Rock)/P(Paper)/S(Scissors)! or Q to quit\n").strip().lower()

    if user_choice not in valid:
        print("Invalid choice! Please choose R, P, S or Q to quit.\n")
        continue

    if user_choice == 'q':
        print("You chose to quit the game.\n")
        break

    computer_choice = random.choice(options)

    print(f"{' Choices ':=^{line_length}}")
    print(f"\nYou: {names[user_choice]} | Computer: {names[computer_choice]}\n")

    if user_choice == computer_choice:
        print("It's a tie!\n")
    elif (user_choice == 'r' and computer_choice == 's') or \
         (user_choice == 'p' and computer_choice == 'r') or \
         (user_choice == 's' and computer_choice == 'p'):
        print("You win this round!\n")
        user_score += 1
    else:
        print("Computer wins this round!\n")
        computer_points += 1
    print("=" * line_length)

print("Thanks for playing!\n")

print(f"Final Scores\nYou: {user_score}\nComputer: {computer_points}\n")

print(f"{' SCOREBOARD ':=^{line_length}}\n")
if user_score > computer_points:
    print("Congratulations! You are the overall winner!\n")
elif computer_points > user_score:
    print("Computer is the overall winner! Better luck next time.\n")
else:
    print("It's an overall tie!\n")

print("=" * line_length)