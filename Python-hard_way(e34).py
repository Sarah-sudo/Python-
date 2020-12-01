i = 0
number = []

while i < 6:
    print(f"At the top of i is {i} ")
    number.append(i)
    print("number list is now : ", number)     
    i = i + 1   # if you don't write this line you will stuck in an endless loop!

for num in number:
    print(num)