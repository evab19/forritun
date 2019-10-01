low = int(input("Integer 1: "))
high = int(input("Integer 2: "))
the_sum = 0

for i in range(low, high+1):
    the_sum += i

print(the_sum)
