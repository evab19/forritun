#Finds and prints all positive two digit numbers whose square of the sum of its digits is equal to the number.

for double_digit in range(10,100):
    
    first_digit = double_digit // 10
    second_digit = double_digit % 10
    
    if (first_digit + second_digit)**2 == double_digit:
        print(double_digit)


#Finds and prints all positive numbers < 100 with exactly 10 divisors. 

for number in range(1,100):

    total_divisors = 0

    for divisor in range(1, number+1):
        if number % divisor == 0:
            total_divisors += 1
    if total_divisors == 10:
        print(number)
                