# values are given to people, cars and trucks
people = 30
cars = 40
trucks = 15

# compare the values of cars and people, print line depending on boolean output
if cars > people:
    print "We should take the cars"
elif cars < people:
    print "We should not take the cars."
else:
    print "we can't decide."
# compare values of trucks and cars, print line depending on boolean output
if trucks > cars:
    print "Thats too many trucks"
elif truck < cars:
    print "Maybe we could take the trucks."
else:
    print "we still can't decide."
# compare people and trucks and print line depending on boolean output
if people > trucks:
    print "Alright, let's just take the trucks."
else:
    print "Fine, let's stay home then."
