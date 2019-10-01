import string

def lower_case():
    lower_str = in_str.lower()
    bad_chars = string.whitespace + string.punctuation

    for char in lower_str:
        if char in bad_chars:
            lower_str = lower_str.replace(char,'')
    
    return lower_str

in_str = input("Enter a string: ")

lower_in_str = lower_case()
if lower_in_str == lower_in_str[::-1]:
    print('"' + str(in_str) + '"', " is a palindrome")
else: 
    print('"' + str(in_str) + '"', "is not a palindrome")
