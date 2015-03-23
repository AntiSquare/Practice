from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copying from %s to %s" % (from_file, to_file)

# we could do these two on one line, how?
# in_file = open(from_file)
# indata = in_file.read()
indata = open(from_file).read()

print "The input file is %d bytes long" % len(indata)

# make this one line long?
# out_file = open(to_file, 'w')
# out_file.write(indata)
out_file = open(to_file, 'w').write(indata)

print "Alright, all done."

# if you open and read/write in one line then python will
# automatically close the file for you after that line of
# code runs
# out_file.close()
# in_file.close()