from sys import argv

script, filename = argv

txt = open(filename)

print "Okay, lets check what's in %r" % filename
print txt.read()
txt.close()
