# Simple-Game
#It's a simple game written in python.
import time
name = raw_input("Enter your name : ")
print"  Hello  "+name," name to play AKthe_HULK "
print("")
time.sleep(1)
print "start gusing"
time.sleep(0.5)
word="Github rep"
guesses=''
turns = 10
while turns > 0:
	failed =0
	for char in word:
		if char in guesses:
			print(char)
		else:
			print("---")
			failed +=1
	if failed ==0:
		print("you Won")
		break
	print
	gusess = raw_input("gusess a charector :")
	guesses += gusess
	if gusess not in word:
		turns -=1
		print("WRONG")
	print("you have ",+turns,"more guesses")
if turns ==0:
	print("YOU LOSSE")
