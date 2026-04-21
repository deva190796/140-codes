# Write a Python program to display calendar.
import calendar
month = int(input("Enter the Month :"))
year = int(input("Enter the Year :"))
cal = calendar.month(year,month)
print(cal)
