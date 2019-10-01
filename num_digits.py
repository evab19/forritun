#Prenta út fjölda tölustafa í innslegnum streng

# Fá streng frá notanda

def get_string():
    a_str = input("Enter a string: ")
    return a_str

# Reikna út fjölda tölustafa í strengnum

def count_digits(a_str):
    ''' Returns the count of digits in a_str ''' 
    count = 0
    for ch in a_str:
        if ch.isdigit():
            count += 1

    return count

# Prenta út niðurstöðuna

a_str = get_string()
count = count_digits(a_str)

print(count)