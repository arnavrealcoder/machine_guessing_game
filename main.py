import random

n = 5

unique_random_list = random.sample(range(1,11), n)
winning_num = random.choice(unique_random_list)
print(unique_random_list)

while True:                          
  machine_1 = int(input("Please choose a random number: "))

  if machine_1 == winning_num:
    print("Congrats, you won!")
    break
  elif machine_1 > winning_num:
    print("Number is to high, guess lower")

  elif machine_1 < winning_num:
    print("Number is to low, guess higher")

  else:
      print("Invalid number")

