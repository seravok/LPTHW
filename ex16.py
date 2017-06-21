# import argument variable from sys
from sys import argv
# arguments are created
script, filename = argv
# print this and the name given when stating the script
print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."
# shows a questionmark while waiting for input
raw_input ("?")
# we need to tell the script to open in write mode with 'w'
print "Opening the file..."
target = open (filename,'w')
# remove everything in the existing file by truncateing
# truncateing is is not really needed when opening in write mode
#print "Truncating the file. Goodbye!"
#target.truncate()

print "Now I'm going to ask you for three lines."
# prompt to type in data is dispayed
line1 = raw_input("Line 1: ")
line2 = raw_input("Line 2: ")
line3 = raw_input("Line 3: ")
# simple print sent
print "I'm going to write these to the file."
# write to specified filename
#target.write(line1)
#target.write("\n")
#target.write(line2)
#target.write("\n")
#target.write(line3)
# a shorter one line version of the same code as above
target.write(line1 +"\n"+ line2 +"\n"+ line3)

#print about closing then close file
print "And finally, we close it."
target.close()
