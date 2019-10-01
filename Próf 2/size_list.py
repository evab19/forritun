def input_list(size):
    our_list = []
    for i in range(size):
        list_elem = input("Please add value no. {} to list: ".format(i+1))
        our_list.append(list_elem)
    return our_list

# Main program starts here, DO NOT change
size = int(input("Input vector size: "))

our_list = input_list(size)

print(our_list)