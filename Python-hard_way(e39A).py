# Lists and dictionaries
# Lists
# you can ONLY use numbers to “index” into a list
things = ['a', 'b', 'c', 'd', 'e', 'f']
print(things[1])
print(things)
# change something 
things[2] = 'z'
print("I changed third item from 'c' to 'z'.")
print(things)

# Dictionaries(Dict)
Dict_name = {'name': 'Sarah', 'age':  22, 'height':  (30*2)+(16/2)}
print(Dict_name['name'])
print(Dict_name['age'])
print(Dict_name['height'])
# add city to the dict
Dict_name['city'] = 'Hamburg'
print(Dict_name['city'])
print(Dict_name)
# using number in dict
Dict_name[0] = 'Hello!'
print(Dict_name[0])
print(Dict_name)
# Erase an item in dict
del Dict_name['age']
print("\nI just remove my age from the dict!")
print(Dict_name)