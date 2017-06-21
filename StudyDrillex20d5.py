# import argument variable from sys
from sys import argv
# define the arguments for argv
script, input_file = argv
# create the function print_all
def print_all(f):
    print f.read()
# create the function rewind
def rewind(f):
    f.seek(0)
# create the function print_a_line
def print_a_line(line_count, f):
    print line_count, f.readline()
# use the function current_file on the defined input_file
current_file = open(input_file)
# print message
print "First let's print the whole file:\n"
# use the function print_all on the current_file
print_all(current_file)
# print message
print "Now let's rewind, kind of like a tape."
# use the rewind function to seek the current_file
rewind(current_file)
# print message
print "Let's print three lines:"
# first line of the file
current_line = 1
print_a_line(current_line, current_file)
# current_line + current_line = print second line
current_line = current_line + 1
print_a_line(current_line, current_file)
# second line + 1 = third line and print it
current_line = current_line + 1
print_a_line(current_line, current_file)
# same as above but with less code
current_line += 1
print_a_line(current_line, current_file)
