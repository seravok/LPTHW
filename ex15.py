# import argument variable
from sys import argv

# arguments script and filename are created
script, filename = argv

# open the file specified
txt = open(filename)

# print content of the text file
print "Here's your file %r" % filename
print txt.read()

# type in the filename again
print "Type the filename again:"
file_again = raw_input("> ")

txt_again = open(file_again)
#print the content of the file again
print txt_again.read()
txt.close()
txt_again.close()
