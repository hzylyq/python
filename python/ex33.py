def do_while(index, step):
	number = []
	i = 0
	while i < index:
		print("At the top i is %d" % i)
		number.append(i)

		i += step
		print("numbers now:", number)
		print("At the bottom i is %d" % i)

	print("The numbers: ")

	for num in number:
		print(num)

def do_for(index, step):
	number = []

	for i in range(0, 6, step):
		print("At the top i is %d" % i)
		number.append(i)
		print("numbers now:", number)
		print("At the bottom i is %d" % i)

	print("The numbers: ")

	for num in number:
		print(num)

do_while(6, 2)

do_for(6, 2)