
num = int(input("Input an integer greater than 1: "))

def is_prime():
    prime = True
    for i in range(2,num):
        if (num % i == 0):
            prime = False
    return prime

if is_prime():
    print(num, "is a prime")
else:
    print(num, "is not a prime")