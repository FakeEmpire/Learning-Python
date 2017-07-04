# starts at 0 and opens a new list

i = 0
numbers = []

# it adds 0 to the list, then adds 0+1 to the list
# this repeats until i = 5

while i < 6:
    print(f"At the top i is {i}")
    numbers.append(i)

    i = i + 1
    print("Numbers now: ", numbers)
    print(f"At the bottom i is {i}")


print("The numbers: ")

for num in numbers:
    print(num)
