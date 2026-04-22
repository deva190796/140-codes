# Write a Python Program to Print the Fibonacci sequence.
n = int(input("Enter the number of terms"))
a,b = 0,1
if n <= 0:
    print("no series for negative numbers")
elif n == 1:
    print(n)
else:
    print("Fibanocc Series :")
    for i in range(n):
        print(a, end = " ")
        a,b = b, a+ b