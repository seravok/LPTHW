# print text but don't end line because of the comma
print "How old are you?",
# raw_input is used in order to display input as it was writen
age = raw_input()
print "How tall are you?",
height = raw_input ()
print "How much do you weight?",
weight = raw_input()

print "So, you're %r old, %r tall and %r heavy." % (
    age, height, weight)
