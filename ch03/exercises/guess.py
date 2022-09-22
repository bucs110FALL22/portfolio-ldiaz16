import random

num = random.randrange(1,11)
num_guesses = 0

for i in range(3):
  guess_num = int(input("Please enter a guess:"))
  num_guesses += 1
  if guess_num > num:
    print("Your value is too high")
  elif guess_num < num:
    print("Your value is too low")
  else:
    print("Correct")
    i = 3
print("It took you",num_guesses,"to get it right")    
