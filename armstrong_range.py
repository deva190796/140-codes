# Write a Python Program to Find Armstrong Number in an Interval.

start = int(input("Enter start of interval: "))
end = int(input("Enter end of interval: "))

print("Armstrong numbers in the interval:")

for num in range(start, end + 1):
    c = len(str(num))   
    total = 0

    for digit in str(num):
        total += int(digit) ** c

    if total == num:
        print(num)