import random
num_of_guesses = 5
actual_number = random.randint(1, 101)
#print(actual_number)
for count in range(num_of_guesses):
  guess_number = int(input())
  if actual_number == guess_number:
    print("EXCELLENT")
  elif abs(actual_number - guess_number <= 10):
    print("GOOD")
  elif actual_number - guess_number > 10:
    print("TOO_LOW")
  else:
    print("TOO_HIGH")