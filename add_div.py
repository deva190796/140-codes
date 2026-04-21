# Write a Python program to do arithmetical operations addition and division.
a = int(input("Enter the first number :"))
b = int(input("Enter the second nummber :"))
print(f"Addition of {a} and {b} is = ",a + b)
if b == 0:
    print("Zero division error")
else:    
    print(f"Division of {a} and {b} is = ",a / b)
