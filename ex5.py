name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
weight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "He's %d pounds heavy." % weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is trycky,try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (
    age, height, weight, age + height + weight)

# convert inches to centimeters
height_cm = height * 2.54
print (height_cm)

# convert pounds to kilograms
weight_kg = weight * 0.45359237
print (weight_kg)

# print age plus the converted centimeters and kilograms with some decimals
print "If we use real measurements we would add  %f, %.2f, and %.2f\nand would get %.2f." %(
age, height_cm, weight_kg, age + height_cm + weight_kg)

# now the above result but with all decimal numbers
print "Now the same with decimals\nlets add %r, %r and %r\nand we will get %r." %(
age, height_cm , weight_kg, age + height_cm + weight_kg)
