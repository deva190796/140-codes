# Write a Python program to solve quadratic equation.
import math
a = int(input("Enter the co-efficient of a :"))
b = int(input("Enter the co-efficient of b :"))
c = int(input("Enter the co-efficient of c :"))

discriminant = (b ** 2 ) - 4 * a * c

if discriminant > 0:
    print("The roots are positive")
    positive_root = (-b + math.sqrt(discriminant)) / (2 * a)
    negative_root = (-b - math.sqrt(discriminant)) / (2 * a)
    print(positive_root)
    print(negative_root)
elif discriminant == 0:
    root = -b/(2 * a)
    print(root)
else:
    real_root = -b / (2 *a)
    imaginary_root = math.sqrt(abs(discriminant)) / (2 * a)
    print(f"{real_root} + {imaginary_root}i")
    print(f"{real_root} - {imaginary_root}i")
