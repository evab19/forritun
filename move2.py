MIN_INT = 1
MAX_INT = 10
 
def sequence(position):
    "'Sequence takes in the value of the current position and prints out the axis with the virtual character in place'"
    for i in range(MIN_INT, MAX_INT+1):
        if i == position:
            print("o", end = '')
        else:
            print("x", end = '')
    print()
 
def update_position(position):
    "' update_position takes in the current position and depending on the command from the user changes the position either to the left or right'"
    if direction == "l":
        if position > MIN_INT:
                position -= 1
    elif direction == "r":
        if position < MAX_INT:
            position += 1
    return position
 
current_position = int(input("Input a position between 1 and 10: "))
 
sequence(current_position)

print("""l - for moving left
r - for moving right
Any other letter for quitting""")
 
direction = input("Input your choice: ")
 
while direction == "l" or direction == "r":
    current_position = update_position(current_position)
    sequence(current_position)

    direction = input("Input your choice: ")
else:
    sequence(current_position)