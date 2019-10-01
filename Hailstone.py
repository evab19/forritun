#Generate a hailstone sequence

number = int(input("Enter a positive integer:"))
count = 0

print("Starting with number:", number)
print("Sequence is: ", end=' ')

while number > 1: #stops the sequence when we hit 1
    if number%2: #don't be fooled by the 2, this means the number is odd!
        number = number * 3 + 1
    else:
        number = number / 2 
    print(number,",", end=' ') #adds the number to the sequence

    count += 1
else:
    print() #just a blank line for a nicer output
    print("Sequence is ", count, " numbers long")
