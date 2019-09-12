# Given a string named a_str, move the first 3 letters to the back of the string.

# Print it.

a_str = input("Input a string: ")

first_three = a_str[:3] #var fyrst með [0:3] en það skiptir engu því að default er 0
a_str = a_str[3:] + first_three

print(a_str)