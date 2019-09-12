def lower_case():
    count_lower = 0
    

    for char in user_input:

        if (char.islower()) == True:
            count_lower += 1

    return count_lower   

def upper_case():
    count_upper = 0 
    for char in user_input:

        if (char.isupper()) == True:
            count_upper += 1
    return count_upper   
# Your function definition goes here

user_input = input("Enter a string: ")

# Call the function here
upper = upper_case()
lower = lower_case()

print("Upper case count: ", upper)
print("Lower case count: ", lower)