count = [1, 2, 3, 4, 5]
fruts = ['apple', 'orange', 'pineapple', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters'] # there is no need for "" for numbers but you have to use "" for strings

#  for-loop  through a list
for number in count:
    print(f"This is count list: {number} ")  

for frut_type in fruts:
    print(f"These are types of frut in fruts list: {frut_type} ")

for i in change:
    print(f"I got {i}")


# build a list
elements = []



# for-loop using range function
for i in range(0,20):
    print(f"Now we are using range function. You can now count without list. {i}  ")
    elements.append(i) # By append you can add to list
    print(elements)    


for i in elements:
    print(f"Element was: {i}")