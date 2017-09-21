ten_things = "Apples Oranges Crows Telephone Light Sugar"

print("Wait there's not 10 things in that list, let's fix that")

stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee", "Cron", "Banana", "Gril", "Boy"]

while len(stuff) != 10:
	next_one = more_stuff.pop()		#将more_stuff的元素依次给next_one
	print("Adding: ", next_one)
	stuff.append(next_one)			#实际上执行了append(stuff, next_one)
	print("There's %d items now" % len(stuff))

print("There we go: ", stuff)

print("Let's do some thing with stuff.")

print(stuff[1])
print(stuff[-1])
print(stuff.pop())
print(' '.join(stuff))		#What?Cool!
print('#'.join(stuff[3:5]))












