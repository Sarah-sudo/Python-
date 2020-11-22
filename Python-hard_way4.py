from sys import argv
script, file_name = argv
target = open(file_name)
print(f""" hi. this is {script} script and 
I want to show some text from another file named {file_name} """)
print(target.read())
