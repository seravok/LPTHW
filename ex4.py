# Shows how many cars ar available today
cars = 100

# Every car has 4 seats
space_in_a_car = 4

# The amount of drivers available
drivers = 30

# How many passangers need a ride
passengers = 90

# What amount of cars will not be used
cars_not_driven = cars - drivers

# How many cars will be driven
cars_driven = drivers

# What is the capacity of the driven cars
carpool_capacity = cars_driven * space_in_a_car

# How many seats is needed in every car
average_passengers_per_car = passengers / cars_driven

# Prints the text with the amount of cars
print "There are", cars, "cars available."

# Prints how many drivers there are
print "There are only", drivers, "drivers available."

# Prints how many cars will not by used today
print "There will be", cars_not_driven, "empty cars today."

# Prints how how many passengers that can ride
print "We can transport", carpool_capacity, "people today."

# Prints how many passengers that need a ride
print "We have", passengers, "to carpool today."

# Prints how many passengers each car that is driven needs to hold.
print "We need to put about", average_passengers_per_car, "in each car."
