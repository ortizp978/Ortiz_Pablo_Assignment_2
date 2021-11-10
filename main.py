from random import randint
from gameComponents import winLose,gameVars

choices = ["rabbit", "gun", "wall"]

Dad = False

# add player 
DadLives = 1
SonLives = 1

print(" ")
print("LETS PLAY WITH YOUR SON RABBIT - GUN - WALL!")
print(" ")
print("********* INSTRUCTIONS *********")
print("Select between RABBIT, GUN & WALL.")
print("WALL defeats GUN, GUN defeats RABBIT, and RABBIT defeats WALL.")
print("Good Luck Daddy!")
print(" ")

while gameVars.Dad is False:


	gameVars.Dad =input("Make your selection! :")
	gameVars.Son = choices[randint(0,2)]

	print("Dad chose: " + gameVars.Dad)
	print("Son chose: " + gameVars.Son)

	#=====================================

	if (gameVars.Son == gameVars.Dad):
		print(" ")
		print("You select the same! Choose again")

	elif (gameVars.Dad == "rabbit"):
		if (gameVars.Son == "gun"):
			print(" ")
			print("Dad lose!")
			gameVars.DadLives = gameVars.DadLives - 1
		else:
			print(" ")
			print("DAD WIN!")
			gameVars.SonLives = gameVars.SonLives - 1

	elif (gameVars.Dad == "gun"):
		if (gameVars.Son == "wall"):
			print(" ")
			print("Dad lose!")
			gameVars.DadLives = gameVars.DadLives - 1
		else:
			print(" ")
			print("DAD WIN!")
			gameVars.SonLives = gameVars.SonLives - 1

	elif (gameVars.Dad == "wall"):
		if (gameVars.Son == "rabbit"):
			print(" ")
			print("Dad lose!")
			gameVars.DadLives = gameVars.SonLives - 1
		else:
			print(" ")
			print("DAD WIN!")
			gameVars.SonLives = gameVars.SonLives - 1

	print("==============")
	print("Dad Lives " + str(gameVars.DadLives))
	print("Son Lives: " + str(gameVars.SonLives))
	print("==============")
	print(" ")

	#=====================================

	if gameVars.DadLives == 0:
		# call the winorlose function here
		winLose.winorlose(" lost :( ")

	elif gameVars.SonLives == 0:
		# call the winorlose function here
		winLose.winorlose(" WON!! :) :) :) :) ")

	gameVars.Dad = False
