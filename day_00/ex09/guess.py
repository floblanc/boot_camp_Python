import random

def is_digit(n):
   try:
       int(n)
       return True
   except ValueError:
       return  False

find = random.randint(1, 99)
x = 0
t = 0
print("This is an interactive guessing game!")
print("You have to enter a number between 1 and 99", end = "")
print("to find out the secret number.")
print("Type 'exit' to end the game.\nGood luck!")
while int(x) != find:
	x = input("What's your guess between 1 and 99?\n")
	if (x == "exit"):
		print("Goodbye!")
		exit()
	elif not (is_digit(x)):
		print("That's not a number.")
	elif (int(x) > find):
		print("Too high!")
	elif (int(x) < find):
		print ("Too low!")
	t +=1
if (int(x) == 42):
	print("The answer to the ultimate question of life", end = "")
	print(", the universe and everything is")
if (t == 1):
	print("Congratulations! You got it on your first try!")
else:
	print("Congratulations, you've got it!\nYou won in", t, "attempts!")