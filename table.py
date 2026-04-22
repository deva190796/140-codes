# Write a Python Program to Display the multiplication Table.
n = int(input("Enter the number to create the table :"))
for i in range(1,11):
    result = n * i
    print(f"{n} X {i} = {result}")