def func1(str1, str2):
    if str1 > str2:
        result_str = str[1 :]
    else:
        result_str = str2[:-1]
    return result_str

#main program
response1_str = input("Enter a string: ")
response2_str = input("Enter a second string: ")

print(func1(response1_str, response2_str))
print(func1(response2_str, response1_str))

#given the input values, abc123 and then bcd456, what output is produced from line1?
#give the two input values, abc123 and then bcd456, what output is provided in line 2?
#given the input values, aaabbc and then aaabbcd, what output is produced in line 1?
#given the input values, aaabbc and then aaabbcd, what output is produced in line 2?
