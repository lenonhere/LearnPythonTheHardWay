# There are 100 cars
cars = 100
# There are 4.0 spaces in each car
space_in_a_car = 4.0
# There are 30 drivers
drivers = 30
# There are 90 passenagers
passengers = 90
# Some of the cars would not be driven, the number is equal to the number of the cars minus the number of the drivers
cars_not_driven = cars - drivers
# The number of the cars which would be driven is equal to the number of the drivers
cars_driven = drivers
# Total capacity of the carpool is equal to number of the driven cars multiply by spaces in a car
carpool_capacity = cars_driven * space_in_a_car
# The average number of the passengers per car is equal to number of passengers divided by number of cars that be driven
average_passengers_per_car = passengers / cars_driven


print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."