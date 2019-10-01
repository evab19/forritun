# Create a program that lets the user input an integer, lets call it size. This integer should
# denote the size of a list. Next you should let the user input size many values to a list. Next
# you should let the user input a value, lets call it target. Next you should count how often the
# value target occurs in the list. Next the program should print how many times the value
# target occurs in the list.
# You can solve this with built in functions but I recommend trying to solve this without using
# builtin functions as well (excluding .append()).

def input_list(size):
    our_list = []
    for i in range(size):
        list_elem = input("Please add value no. {} to list: ".format(i+1))
        our_list.append(list_elem)
    return our_list

def is_target(our_list, target):
    count = 0
    target_bool = False
    for word in our_list:
        
        if word == target:
            target_bool = True
            count += 1

    return target_bool, count

def print_target(target_bool, target, count):
    if target_bool == True:
        print(" {} is in the list!".format(target))
        print(" {} appears {} times in the list".format(target, count))
    else:
        print(" {} is not in the list!".format(target))

# Main program starts here, DO NOT change
size = int(input("Input vector size: "))
target = input("Input a target: ")

def main():
    our_list = input_list(size)

    target_bool, count = is_target(our_list, target)
    print(target_bool)
    print_target(target_bool, target, count)

main()