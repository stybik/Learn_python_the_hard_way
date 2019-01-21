name = 'Bikram'
age = 35
height = 82
weight = 75
eyes = "Brown"
teeth = "White"
hair = "Black"

print "Let's talk about %s" % name
print "He's %d years old." % age
print "He's %d inches tall." % height
print "He's %d pounds heavy." % weight
print "Actually that's not too heavy"
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % (teeth)

print 'If I add %d, %d and %d I get %d' % (age, height, weight, age + height + weight)

my_greeting = "Hello, \t"
my_first_name = 'Bikram'
my_last_name = 'Biswas'
my_age = 22

print "%r my name is %s %s, and I am %d years old" % (my_greeting, my_first_name, my_last_name, my_age)

# Extra credits, convert inches and pounds to centimeters and kilos

inches_per_centimeters = 2.54
pounds_per_kilo = 0.45359237

print "He's %f centimeters tall." % (height * inches_per_centimeters)
print "He's %f kilos heavy." % (weight * pounds_per_kilo)