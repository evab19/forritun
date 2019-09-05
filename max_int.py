num_int = int(input("Input a number: "))    # Do not change this line

#Design an algorithm that finds the maximum positive integer input by a user.  
# The user repeatedly inputs numbers until a negative value is entered.
max_int = 0

while num_int >= 0:
    if num_int >= max_int:
        max_int = num_int
    num_int = int(input("Input a number: "))

print("The maximum is", max_int)    # Do not change this line