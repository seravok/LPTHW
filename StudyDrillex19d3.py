def forks_and_knifes(fork_count, knife_count):
    print "I have %d forks" % fork_count
    print "And also %d knifes" % knife_count

forks_and_knifes(15,20)

print "How many forks?: ",
forks_how_many = int(raw_input())
print "How many knifes?: ",
knifes_how_many = int(raw_input())

forks_and_knifes(forks_how_many, knifes_how_many)

forks_and_knifes(forks_how_many + 999, knifes_how_many + 99)

forks_and_knifes(forks_how_many * 5, knifes_how_many **2 )
