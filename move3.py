MIN_INT = 1
MAX_INT = 10

first_position = int(input("Input a position between 1 and 10: "))

def sequence():
    "'Sequence takes in the value of the current position and prints out the axis with the virtual character in place'"
    for i in range(MIN_INT, MAX_INT+1):
        if i == first_position:
            print("o", end = '')
        else:
            print("x", end = '')
    print()

sequence()

print("""l - for moving left 
r - for moving right 
Any other letter for quitting""")

direction = input("Input your choice: ")

def position():
    if direction == "l":
        if first_position > MIN_INT:
                first_position -= 1
    elif direction == "r":
        if first_position < MAX_INT:
            first_position += 1
    return first_position

while direction == "l" or direction == "r":
    position = position(position)
    sequence(position)

    direction = input("Input your choice: ")
else:
    sequence()