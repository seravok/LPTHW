# string text will be tabbed in by \t
tabby_cat = "\tI'm tabbed in."
# string text will be splitt to a new line by \n
persian_cat = "I'm split\non a line."
# string text will have backslash in it
backslash_cat = "I'm \\ a \\ cat."

# horizontal tab with \t. \n can also be used to create new line
fat_cat ="""
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""
# print all the cat related strings
print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

test_string = """
How about some more testing
I hope it %r
""" % '\n\t* works'

print test_string

#while True:
#    for i in ["/","-","|","\\","|"]:
#        print "%s\r" % i,
