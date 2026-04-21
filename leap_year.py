# Write a Python Program to Check Leap Year.
year = int(input("Enter the Year :"))
if year % 400 == 0 and year % 100 == 0:
    print("The year is leap")
elif year % 4 == 0 and year % 100 != 0:
    print("Leap Year")
else:
    print("Not a leap year")
    