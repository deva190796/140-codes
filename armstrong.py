# armstrong
n = int(input("Enter the number :"))

digits = list(str(n))   
c = len(digits)         

total = 0
for i in digits:
    total += int(i) ** c

print("\nSum:", total)

if n == total:
    print("Armstrong")
else:
    print("Not an Armstrong number")