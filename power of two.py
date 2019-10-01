number = int(input("Number: "))

power = 1

new_number = number / 2 

while new_number % 2 == 0:
    power += 1
    new_number = new_number/2

print(power)
