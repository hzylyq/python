print("You enter a dark room with two doors. Do you go through door #1 or #2")

door = int(input('>'))

if door == 1:
	print("You enter door #1")
	print("There's a giant bear here eating a cheese cake and he ask you \"do you want to eat a cake\"")
	print("Yes: please choose 1. No: please choose 2.")

	bear = int(input('>'))

	if bear == 1:
		print("You becomes a boyfriend with the bear")
	elif bear == 2:
		print("You are eated by the bear. Good job")
	else:
		print("You run but you stumble around and fall on a knife and die. Good job")

elif door == 2:
	print("You enter door #2")
	print("You stare into the endless abyss at Cthulhu's retina.")
	print("1. Blueberries")
	print("2. Yellow jacket clothespins.")
	print("3. Understanding revolvers yelling melodies.")

	insanity = int(input('>'))

	if insanity == 1 or insanity == 2:
		print("Your body survives powered by a mind of jello. Good job")
	elif insanity == 3:
		print("The insanity rots your eyes into a pool of muck. Good job")
	else:
		print("You couldn't run and you died. Good job")

else:
	print("You stumble around and fall on a knife and die. Good job!")