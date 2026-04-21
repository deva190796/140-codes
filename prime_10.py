# Write a Python Program to Print all Prime Numbers in an Interval of 1-10.
import math
n = int(input("Enter the number :"))
if n < 2:
    print("No prime numbers found")
else:
    for num in range(2,n+1):
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                break
        else:
            print(num)