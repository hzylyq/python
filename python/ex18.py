#this one is like script with argv
def print_two(*args):
	arg1, arg2 = args
	print("arg1:%r arg2:%r" % (arg1, arg2))

#ok that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
	print("arg1:%r arg2:%r" % (arg1, arg2))

def print_one(arg):
	print("arg:%r" % arg)

def print_none():
	print("I get nothing")

print_two("Zed", "Shaw")
print_two_again("Zed", "Shaw")
print_one("First!")
print_none()