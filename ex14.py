# first import argument variable
from sys import argv

# Then define some arguments
script, user_name, pc_put_head = argv
prom = '>> '

# Ask some questions and save the data for later
print "Hi %s, I'm the %s script." % (user_name, script)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_name
likes = raw_input(prom)

print "Where do you live %s?" % user_name
lives = raw_input(prom)

print "What kind of computer do you have?"
computer = raw_input(prom)

# Print with the raw data specified
print """
Alright, you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer. Nice.
Please, put lapop on head for %r seconds.
""" % (likes, lives, computer, pc_put_head)
