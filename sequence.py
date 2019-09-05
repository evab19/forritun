#Design an algorithm that generates the first
# n numbers in the following sequence:; 1, 2, 3, 6, 11, 20, 37, ___, ___, ___, …
# each number is the sum of the previous three numbers
n = int(input("Enter the length of the sequence: "))

first = 0
second = 1
third = 0

for i in range(0, n):
    summed = first + second + third
    print(summed)
        
    third = second
    second = first
    first = summed
