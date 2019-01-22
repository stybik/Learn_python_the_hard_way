

# ex20: Functions and Files

from sys import argv

script, input_file = argv

# Define a function called print_call to print the whole contents of a
# file, with one file object as formal parameter
def print_all(f):
    print f.read()


# Define a function called rewind to make the file reader go back to
# the first byte of the file, with one file object as formal parameter
def rewind(f):
    # make the file reader go back to the first byte of the file
    f.seek(0)


# Define a function called print_a_line to print a line of the file,
# with a integer counter and a file object as formal parameters
def print_a_line(line_count, f):
    print "line_count equal to current_line?:", (line_count == current_line)
    print line_count, f.readline()


# Open a file
current_file = open(input_file)
print "First let's print the whole file:\n"
print_all(current_file)
print "Now let's rewind, kind of like a tape."
rewind(current_file)

print "Let's print three lines:"
current_line = 1
print "current_line = %d" % current_line
print_a_line(current_line, current_file)
current_line += 1
print "current_line is equal to:%d" % current_line
print_a_line(current_line, current_file)
current_line += 1
print "current_line is equal to:%d" % current_line
print_a_line(current_line, current_file)