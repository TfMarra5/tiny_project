import time

line_length = 35

print(f"\n{' WELCOME! ':=^{line_length}}\n")


choose2 = input("Choose time format - seconds or minutes (s/m): \n").lower()
if choose2 not in ["s", "m"]:
    print("\nInvalid choice. Please choose 's' for seconds or 'm' for minutes.\n")

if choose2 == "s":
    t = input("\nEnter time in seconds: \n") #  Get user input for time in seconds
    user_choice = int(t)
    if t.isdigit() == False:
        print("\nInvalid input. Please enter a number.\n")
        exit()
else:
    t2 = input("\nEnter time in minutes: \n")  #  Get user input for time in minutes
    user_choice = int(t2)
    if t2.isdigit() == False:
        print("\nInvalid input. Please enter a number.\n")
        exit()

total_seconds = int(user_choice)
if choose2 == "m":
    total_seconds *= 60

print(f"{' TIME COUNTING ':=^{line_length}}\n")

while total_seconds != 0:
  minutes, seconds = divmod(total_seconds, 60)
  timer = "{:02d}:{:02d}".format(minutes, seconds)
  print("Timer set to:", timer, end="\r")
  print("=" * line_length)
  time.sleep(1)
  total_seconds = total_seconds - 1


print(f"\n{' Time\'s up! ':=^{line_length}}\n")