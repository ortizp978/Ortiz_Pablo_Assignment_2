def winorlose(status):
	print(" ")
	print("DAD " + status)
	print("Would you like to play RABBIT, GUN & WALL again?... Please Daddy?")
	choice = input(" Y / N? ")

	global DadLives
	global SonLives
	global Dad

	if choice == "n":
		print(" ")
		print("Ok Dad, you must have a lot better things to do ... continue with your busy adult life  :(")
		print(" ")
		exit()
	else:
		print(" ")
		print("Remember... Wall defeats Gun, Gun defeats Rabbit, and Rabbit defeats Wall.")
		print(" ")
		DadLives = 5
		SonLives = 5
		Dad = False