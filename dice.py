import random

roll_dice = input("Write _start_ to dice roll: ")

if roll_dice == "start":
  die1 = random.randint(1,6)

  die2 = random.randint(1,6)


print(die1, die2)
print(die1 + die2)

if (die1 + die2) == 7 or (die1 + die2)== 11:

  print("You win!")

else:

  print("you lost")