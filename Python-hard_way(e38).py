ten_things = "Apples Oranges Crows Telephone Light Sugar"
print(ten_things)
print("wait there are not 10 things in the list. Let's fix that.")
stuff = ten_things.split(" ")
print(stuff)
more_stuff = ["day", "night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]


#attach more_stuff to ten_things
while len(stuff) != 10:
    next_one = more_stuff.pop()       #using pop()
    print("adding: ", next_one)
    stuff.append(next_one)
    print(f"there are {len(stuff)} items now")
    print("there you go: ", stuff)

print("\nLet's do some things with stuff.")
print(stuff[0])
print(stuff[-1])

print(' .....'.join(stuff))
print('#'.join(stuff[3:5]))
