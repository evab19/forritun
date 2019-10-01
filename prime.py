
num = int(input("Input an integer greater than 1: "))

def is_prime(n):
    prime = True
    for i in range(2, n):
        if (n % i == 0):
            prime = False
    return prime

if is_prime(num):
    print(num, "is a prime")
else:
    print(num, "is not a prime")