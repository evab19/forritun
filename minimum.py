# find_min function definition goes here

first = int(input("Enter first number: "))
second = int(input("Enter second number: "))
    
# Call the function here
def minimum_func():
    minimum = 0
    if first <= second:
        minimum = first
    else:
        mininum = second
    return(minimum)

minimum = minimum_func()    
print("Minimum: ", minimum)