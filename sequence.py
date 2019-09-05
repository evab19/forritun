#Design an algorithm that generates the first
# n numbers in the following sequence:; 1, 2, 3, 6, 11, 20, 37, ___, ___, ___, …
# each number is the sum of the previous three numbers
n = int(input("Enter the length of the sequence: "))

first = 0
second = 0
third = 0

for i in range(1, n+1):
    summed = first + second + third
    if (third == 0):
        print(i)
        summed = i
    else:
        print(summed)
        summed = first + second + third
    third = second
    second = first
    first = summed
