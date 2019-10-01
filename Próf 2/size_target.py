def input_list(size):
    our_list = []
    for i in range(size):
        list_elem = input("Please add value no. {} to list: ".format(i+1))
        our_list.append(list_elem)
    return our_list

def is_target(our_list, target):
    for word in our_list:
        target_bool = False
        if word == target:
            target_bool = True
            break
        else:
            target_bool = False
    return target_bool

def print_target(target_bool, target):
    if target_bool == True:
        print(" {} is in the list!".format(target))
    else:
        print(" {} is not in the list!".format(target))

# Main program starts here, DO NOT change
size = int(input("Input vector size: "))
target = input("Input a target: ")

def main():
    our_list = input_list(size)

    target_bool = is_target(our_list, target)
    print(target_bool)
    print_target(target_bool, target)

main()