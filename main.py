from random import randint
from gameComponents import winLose

choices = ["rabbit", "gun", "wall"]

Dad= False

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

while Dad is False:


	Dad =input("Make your selection! :")
	Son = choices[randint(0,2)]

	print("Dad chose: " + Dad)
	print("Son chose: " + Son)

	#=====================================

	if (Son == Dad):
		print(" ")
		print("You select the same! Choose again")

	elif (Dad == "rabbit"):
		if (Son == "gun"):
			print(" ")
			print("Dad lose!")
			DadLives = DadLives - 1
		else:
			print(" ")
			print("DAD WIN!")
			SonLives = SonLives - 1

	elif (Dad == "gun"):
		if (Son == "wall"):
			print(" ")
			print("Dad lose!")
			DadLives = DadLives - 1
		else:
			print(" ")
			print("DAD WIN!")
			SonLives = SonLives - 1

	elif (Dad == "wall"):
		if (Son == "rabbit"):
			print(" ")
			print("Dad lose!")
			DadLives = SonLives - 1
		else:
			print(" ")
			print("DAD WIN!")
			SonLives = SonLives - 1

	print("==============")
	print("Dad Lives " + str(DadLives))
	print("Son Lives: " + str(SonLives))
	print("==============")
	print(" ")

	#=====================================

	if DadLives == 0:
		# call the winorlose function here
		winLose.winorlose(" lost :( ")

	elif SonLives == 0:
		# call the winorlose function here
		winLose.winorlose(" WON!! :) :) :) :) ")

	Dad = False
