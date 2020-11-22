from sys import argv
script, name, age = argv
prompt = ">>>>>>>>"
print("the script is: ", script)
print("your name is: ", name)
print("your age is: ", age)

#like = input("do you like me?")
print(f"Hi, this is {script} script")
print(f"Do you like me {name}?")
like = input(prompt)
print(f"so, you said {like}!!")