from sys import argv

script, filename = argv

print("we're going to erase %r." % filename)
print("If you don't want that, hint CTRL-C(^C).")
print("If you want that, hint RETURN")

input("?")

print("Opening the file ...")
target = open(filename, 'w')

print("Truncating the file.	Goodbye!")
target.truncate()

print("Now I'm going to ask you for three lines.")

line1 = input("line1:")
line2 = input("line2:")
line3 = input("line3:")

print("I'll going write these to the file.")

all_string = line1 + "\n" + line2 + "\n" + line3 + "\n"

"""
target.write(line1)
target.write("\n")

target.write(line2)
target.write("\n")

target.write(line3)
target.write("\n")
"""
target.write(all_string)

print("And finally, we close it")

target.close()