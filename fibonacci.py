# Your function definition goes here
def fibo():
    first = 1
    second = 0
    sequence = []

    for i in range(0,n+1):
        summed = first + second
        sequence.append(first)
       
        second = first
        first = summed
    return sequence

n = int(input("Input the length of Fibonacci sequence (n>=1): "))

fibo = fibo()

print(fibo)