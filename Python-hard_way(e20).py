from sys import argv
script, input_file = argv  #input: current file

#read all of current file
def print_all(f):
    print(f.read())

#start from the top again
def rewind(f):
    f.seek(0)

#read just a line
def print_line(line_count, f):          #linecouent: num of the line
    print(line_count, f.readline())


#open current file
current_file = open(input_file)


#print all of current file
print("First let's print the whole file:\n")
print_all(current_file)

#start from top again (like a tape)
print("Now let's rewind, kind of like a tape.")
rewind(current_file)

#print some lines
print("Let's print the first  line:")

print_line(0, current_file)

