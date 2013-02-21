# set value to x
x = "There are %d types of people." % 10
# set value to binary
binary = "binary"
# set value to do_not
do_not = "don't"
# set value to y
y = "Those who know %s and those who %s." % (binary, do_not)

# just output the value of x, y
print x
print y

# output with format
print "I said: %r." % x
print "I also said: '%s'." % y

# set value to hilarlous & joke_evaluation
hilarlous = False
joke_evaluation = "Isn't that joke so funny?! %r"

# output with format
print joke_evaluation % hilarlous

# set value to w & e
w = "This is the left side of..."
e = "a string with a right side."

# output string using +
print w + e