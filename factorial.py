# Write a Python Program to Find the Factorial of a Number.
n = int(input("Enter the number :"))
fact = 1
if n < 0:
    print("Factorial does not exist for the negative numbers")
elif n == 0:
    print("factorial of 0 is 1")
else:
    for i in range(1, n + 1):
        fact = fact * i
    print(fact)