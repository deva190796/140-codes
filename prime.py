# Write a Python Program to Check Prime Number.
import math
n = int(input("Enter the number to check it is prime or not :"))
if n <= 1:
    print("Not a prime")
elif n == 2:
    print("Prime")
elif n % 2 == 0:
    print("Not a prime")
else:
    for i in range(3,int(math.sqrt(n)) + 1,2):
        if n % i == 0:
            print("Not a prime")
            break
    else:
        print("Prime")