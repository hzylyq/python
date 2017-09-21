from sys import argv
from os.path import exists

script, from_file, to_file = argv

print("Copying from %s to %s" % (from_file, to_file))

#We could do these two on one line too, how?
in_file = open(from_file)
indata = in_file.read()

print("The file has %d bytes" % len(indata))

print("Does the to_file exists %r" % exists(to_file))
print("Ready, hit RETURN to continue, CTRL-C to abort.")
input()

out_file = open(to_file, 'w')
out_file.truncate()
out_file.write(indata)

print("Alright, all done")

out_file.close()
in_file.close()