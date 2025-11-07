print ("You have started the quiz")

answer_user = input ("Would you like to continue? (Y/N)")

while answer_user != "Y" and answer_user != "N":
  print ("Invalid option")
  answer_user = input("Would you like to continue? (Y/N)\n")

print ("You chose: " + answer_user)

if answer_user == "N":
  quit()

score = 0

print ("Starting the quiz... \n")

print ("What is the capital of France? \n (A) Berlin \n (B) Madrid \n (C) Paris \n (D) Rome \n")
answer_1 = input ("Answer: ")
if answer_1 == "C":
  print ("Correct!\n")
  score = score + 1
else:
  print ("Incorrect!\n")
  score = score + 0

print ("What is 2 + 2? \n (A) 3 \n (B) 5 \n (C) 4 \n (D) 6 \n")
answer_2 = input ("Answer: ")
if answer_2 == "C":
  print ("Correct!\n")
  score = score + 1
else:
  print ("Incorrect!\n")
  score = score + 0

print ("What is the largest planet in our solar system? \n (A) Jupiter \n (B) Mars \n (C) Earth \n (D) Saturn \n")
answer_2 = input ("Answer: ")
if answer_2 == "A":
    print ("Correct!\n")
    score = score + 1
else:
    print ("Incorrect!\n")
    score = score + 0

print (f"Quiz over... Score: {score}/3")