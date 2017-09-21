name = "huzhiyang"
age = 24	#terrible
height = 165
weight = 60
eyes = "Black"
teeth = "White"
hair = "Black"

print("let's talk about %s" % name)
print("He's %d cm" % height)
print("He's %d kg" % weight)
print("Actually that's not too heavy")
print("He's got %s eyes and %s hair" % (eyes, hair))
print("His teeth are usually %s depending on the coffee." % teeth)

#this line is tricky, try to get it exactly right
print("If I add %d %d, and %d I get %r" % (age, height, weight, age + height + weight))
print(round(1.5000000001))

print("%s", "ahaha\n")
print("%r", "ahaha\n")

print('%r' % '\x27')	# 带括号的单引号 "'" 
print('%s' % '\x27') 	# 纯单引号