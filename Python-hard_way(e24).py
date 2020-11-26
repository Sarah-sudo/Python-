print("Let' review everything.")

#\
print('you should know about \\ and how it works: ')
print("you should know that \\n is newline and \\t is a tab ")



print("--------------")
print(""" 
\t Hi I'm Annie, hi I'm Annie.
\n\t Hi i'm Ted, hi I'm Ted.
\n\t How are you today Ted?
\n\t Fine thank you Annie.
\n\t How are you?
\n\t Fine thank you.
""")
print("--------------")

five = 10 - 2 + 3 - 6
print(f"This should be five: {five}")

#function and return a value
def ingredient(start):
 jelly_beans = start * 500
 jars = jelly_beans / 1000
 crates = jars / 100
 return jelly_beans, jars, crates

start = 1000
beans, jars, crates = ingredient(start)
 
print(f"With a starting point of: {start}")  #print("With a starting point of: {}" .format(start))
print(f"We'd have {beans} beans, {jars} jars, and {crates} crates.")

start = start / 10
print("we can also do it this way: \n")
formula = ingredient(start)
print("We'd have {} beans, {} jars, and {} crates.".format(*formula))
#print(f"We'd have {beans} beans, {jars} jars, and {crates} crates.")
