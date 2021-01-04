numbers = [2, 1, 5]
n = 0
while True:
	
	try:
		answer = input("Guess a number: ")
	
		if (answer == "q"):
			break
		
		number = int(answer)
		
		if (number in numbers):
			print("You're correct!")
			break
		else:
			print("Wrong number!")
	except NameError:
		print("Please input a number or type \"q\" to exit.")

