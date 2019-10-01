integer = int(input("Enter an integer: "))

total_sum = 0
total_odd = 0 
total_even = 0
largest_number = 0

while integer > 0:
    total_sum += integer
    if integer % 2: #if integer is an odd number
        total_odd += 1
    else: #if the number is even
        total_even += 1
    if integer > largest_number:
        largest_number = integer
    print("Cumulative total: ", total_sum)
    integer = int(input("Enter an integer: "))

if largest_number > 0: #to make sure the prints don't run if we start off with an int <= 0
    print("Largest number: ", largest_number)
    print("Count of even numbers: ", total_even)
    print("Count of odd numbers: ", total_odd)
