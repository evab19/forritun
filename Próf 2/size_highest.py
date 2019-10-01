# Create a program that lets the user input an integer, lets call it size. This integer should
# denote the size of a list. Next you should let the user input size many values to a list. Next the
# program should print the highest value in the list.
# You can solve this with built in functions but I recommend trying to solve this without using
# builtin functions as well (excluding .append()).

def input_list(size):
    our_list = []
    for i in range(size):
        list_elem = input("Please add value no. {} to list: ".format(i+1))
        our_list.append(list_elem)
    return our_list

def is_highest(our_list):
    highest = "0"
    for word in our_list:
        if word > highest:
            highest = word
    return highest

# Main program starts here, DO NOT change
size = int(input("Input vector size: "))

our_list = input_list(size)
highest_value = is_highest(our_list)

print(our_list, highest_value)