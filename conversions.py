# conversions
n = int(input("Enter a decimal number: "))

if n == 0:
    print("Binary: 0\nOctal: 0\nHexadecimal: 0")
else:
    num = n
    binary = ""
    while num > 0:
        binary = str(num % 2) + binary
        num //= 2

    num = n
    octal = ""
    while num > 0:
        octal = str(num % 8) + octal
        num //= 8

    num = n
    hexa = ""
    hex_chars = "0123456789abcdef"
    while num > 0:
        hexa = hex_chars[num % 16] + hexa
        num //= 16

    print("Binary:", binary)
    print("Octal:", octal)
    print("Hexadecimal:", hexa)