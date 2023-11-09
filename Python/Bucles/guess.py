guess = 0
tries = 0

while guess != 6 and tries != 7:
  guess = int(input("Guess the number:  "))
  tries += 1
if tries == 7:
  print("You failed!")
else:
  print("You got it!")