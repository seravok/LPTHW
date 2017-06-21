# define  x as text with number 10
x = "There are %d types of people." % 10

# binary is binary
binary = "binary"

# do_not is don't
do_not = "don't"

# defines y as a string with some other strings in it. 2 strings within  1 sting
y = "Those who know %s and those who %s." % (binary, do_not)

# print x and get the start of the joke
print x

# print y and the rest of the joke
print y

# repeat what was said in x with extra text at the start. 1 sting witin 1 string
print "I said: %r." %x

# repeat y with some extra text at the start. 1 string within 1 string
print "I also said: '%s'." % y

# hilarious checks as false
hilarious = False

# check if joke is funny
joke_evaluation = "Isn't that joke so funny?! %r"

# print the evaluation and false because hilarious
print joke_evaluation % hilarious

# simple string with some text
w = "This is the left side of..."

# another simple sring with some text
e = "a sting with a right side."

# adds the previous two stings together and prints them afte each other.
print w + e
