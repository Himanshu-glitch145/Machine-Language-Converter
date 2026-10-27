def main():
    while True:
        num1 = input('''
Hello, I am M.L.C.

<- Choose any one converter ->

1. Binary to Decimal       (press 1)
2. Binary to Octal         (press 2)
3. Binary to Hexadecimal   (press 3)
4. Decimal to Binary       (press 4)
5. Decimal to Octal        (press 5)
6. Decimal to Hexadecimal  (press 6)
7. Octal to Binary         (press 7)
8. Octal to Decimal        (press 8)
9. Octal to Hexadecimal    (press 9)
10. Hexadecimal to Binary  (press 10)
11. Hexadecimal to Decimal (press 11)
12. Hexadecimal to Octal   (press 12)
13. About this program     (press 13)

Enter your choice number: ''')

        try:
            if num1 == "1":
                value = input("Enter a binary number: ")
                result = int(value, 2)
                print("Decimal value:", result)

            elif num1 == "2":
                value = input("Enter a binary number: ")
                result = oct(int(value, 2))[2:]
                print("Octal value:", result)

            elif num1 == "3":
                value = input("Enter a binary number: ")
                result = hex(int(value, 2))[2:].upper()
                print("Hexadecimal value:", result)

            elif num1 == "4":
                value = int(input("Enter a decimal number: "))
                print("Binary value:", bin(value)[2:])

            elif num1 == "5":
                value = int(input("Enter a decimal number: "))
                print("Octal value:", oct(value)[2:])

            elif num1 == "6":
                value = int(input("Enter a decimal number: "))
                print("Hexadecimal value:", hex(value)[2:].upper())

            elif num1 == "7":
                value = input("Enter an octal number: ")
                print("Binary value:", bin(int(value, 8))[2:])

            elif num1 == "8":
                value = input("Enter an octal number: ")
                print("Decimal value:", int(value, 8))

            elif num1 == "9":
                value = input("Enter an octal number: ")
                print("Hexadecimal value:", hex(int(value, 8))[2:].upper())

            elif num1 == "10":
                value = input("Enter a hexadecimal number: ")
                print("Binary value:", bin(int(value, 16))[2:])

            elif num1 == "11":
                value = input("Enter a hexadecimal number: ")
                print("Decimal value:", int(value, 16))

            elif num1 == "12":
                value = input("Enter a hexadecimal number: ")
                print("Octal value:", oct(int(value, 16))[2:])

            elif num1 == "13":
                print('''
*** This program is designed to convert numbers
    between different number systems. ***

MLC stands for Machine Language Converter.

Created by Himanshu Jangir.

''')

            else:
                print("Incorrect choice! Please select 1 to 13.")

        except ValueError:
            print("Invalid input! Please enter a valid number.")

        # Ask the user whether to continue
        while True:
            choice = input(
                "\nDo you want to continue? (Yes/No): "
            ).strip().lower()

            if choice in ("yes", "y"):
                print("\nRestarting M.L.C....\n")
                break

            elif choice in ("no", "n"):
                print("\nThank you for using M.L.C. Goodbye!")
                return

            else:
                print("Invalid choice! Please enter Yes or No.")


if __name__ == "__main__":
    main()
