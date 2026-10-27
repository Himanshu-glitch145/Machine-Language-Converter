num1 = input('''Hello,I am M.L.C.
<- Choose anyone convertor -> 
1.Binary to Decimal      (press 1)
2.Binary to Octal        (press 2)
3.Binary to Hexadecimal  (press 3)
4.Decimal to Binary      (press 4)
5.Decimal to Octal       (press 5)
6.Decimal to Hexadecimal (press 6)
7.Octal to Binary        (press 7)
8.Octal to Decimal       (press 8)
9.Octal to Hexadecimal   (press 9)
10.Hexadecimal to Binary (press 10)
11.Hexadecimal to Decimal(press 11)
12.Hexadecimal to Octal  (press 12)
13.!About this program!    (press 13)
    Enter your choose number :''')
if num1 == "1":
    def binary_to_decimal(binary_str):
        try:
            if not all(char in '01' for char in binary_str):
                raise ValueError(binary_input,"is not a binary number.")
            decimal_value = int(binary_str, 2)
            return decimal_value
        except ValueError as e:
            return f"Error: {e}"
    if __name__ == "__main__":
        binary_input = input("Enter a Binary number:")
        result = binary_to_decimal(binary_input)
    print(f"Decimal value: {result}")
elif num1 == "2":
    def binary_to_octal(binary_str):
        try:
            if not all(char in '01' for char in binary_str):
                raise ValueError(binary_input,"is not a valid binary number.")
            decimal_value = int(binary_str, 2)
            octal_value = oct(decimal_value)[2:]
            return octal_value
        except ValueError as e:
            return f"Error: {e}"
    if __name__ == "__main__":
        binary_input = input("Enter a binary number: ")
        result = binary_to_octal(binary_input)
    print(f"Octal value: {result}")
elif num1 == "3":
    def binary_to_hexadecimal(binary_str):
        try:
            if not all(char in '01' for char in binary_str):
                raise ValueError("Input is not a valid binary number.")
            decimal_value = int(binary_str, 2)
            hexadecimal_value = hex(decimal_value)[2:].upper()  
            return hexadecimal_value
        except ValueError as e:
            return f"Error: {e}"
    if __name__ == "__main__":
        binary_input = input("Enter a binary number: ")
        result = binary_to_hexadecimal(binary_input)
    print(f"Hexadecimal value: {result}")
elif num1 == "4":
    def decimal_to_binary(decimal_value):
        binary_value = bin(decimal_value)
        return binary_value[2:]
    decimal_value = int(input("Enter a decimal value: "))
    binary_value = decimal_to_binary(decimal_value)
    print(f"Binary value: {binary_value}")
elif num1 == "5":
    def decimal_to_octal(decimal_value):
        octal_value = oct(decimal_value)
        return octal_value[2:]
    decimal_value = int(input("Enter a decimal value: "))
    octal_value = decimal_to_octal(decimal_value)
    print(f"Octal value: {octal_value}")
elif num1 == "6":
    def decimal_to_hexadecimal(decimal_value):
        try:
            if not isinstance(decimal_value, int) or decimal_value < 0:
                raise ValueError("Input must be a non-negative integer.")
            hexadecimal_value = hex(decimal_value)[2:].upper()
            return hexadecimal_value
        except ValueError as e:
            return f"Error: {e}"
    if __name__ == "__main__":
        try:
            decimal_input = int(input("Enter a decimal number: "))
            result = decimal_to_hexadecimal(decimal_input)
            print(f"Hexadecimal value: {result}")
        except ValueError:
            print("Error: Input must be a valid integer.")
elif num1 == "7":
    def octal_to_binary(octal_str):
        try:
            if not all(char in '01234567' for char in octal_str):
                raise ValueError("Input is not a valid octal number.")
            decimal_value = int(octal_str, 8)
            binary_value = bin(decimal_value)[2:]
            return binary_value
        except ValueError as e:
            return f"Error: {e}"
    if __name__ == "__main__":
        octal_input = input("Enter an octal number: ")
        result = octal_to_binary(octal_input)
    print(f"Binary value: {result}")
elif num1 == "8":
    def octal_to_decimal(octal_str):
        try:
            if not all(char in '01234567' for char in octal_str):
                raise ValueError("Input is not a valid octal number.")
            decimal_value = int(octal_str, 8)
            return decimal_value
        except ValueError as e:
            return f"Error: {e}"
    if __name__ == "__main__":
        octal_input = input("Enter an octal number: ")
        result = octal_to_decimal(octal_input)
    print(f"Decimal value: {result}")
elif num1 == "9":
    def octal_to_hexadecimal(octal_str):
        try:
            if not all(char in '01234567' for char in octal_str):
                raise ValueError("Input is not a valid octal number.")
            decimal_value = int(octal_str, 8)
            hexadecimal_value = hex(decimal_value)[2:].upper()  
            return hexadecimal_value
        except ValueError as e:
            return f"Error: {e}"
    if __name__ == "__main__":
        octal_input = input("Enter an octal number: ")
        result = octal_to_hexadecimal(octal_input)
    print(f"Hexadecimal value: {result}")
elif num1 == "10":
    def hexadecimal_to_binary(hexadecimal_str):
        try:
            if not all(char in '0123456789ABCDEFabcdef' for char in hexadecimal_str):
                raise ValueError("Input is not a valid hexadecimal number.")
            decimal_value = int(hexadecimal_str, 16)
            binary_value = bin(decimal_value)[2:]
            return binary_value
        except ValueError as e:
            return f"Error: {e}"
    if __name__ == "__main__":
        hexadecimal_input = input("Enter a hexadecimal number: ")
        result = hexadecimal_to_binary(hexadecimal_input)
    print(f"Binary value: {result}")
elif num1 == "11":
    def hexadecimal_to_decimal(hexadecimal_str):
        try:
            if not all(char in '0123456789ABCDEFabcdef' for char in hexadecimal_str):
                raise ValueError("Input is not a valid hexadecimal number.")
            decimal_value = int(hexadecimal_str, 16)
            return decimal_value
        except ValueError as e:
            return f"Error: {e}"
    if __name__ == "__main__":
        hexadecimal_input = input("Enter a hexadecimal number: ")
        result = hexadecimal_to_decimal(hexadecimal_input)
    print(f"Decimal value: {result}")
elif num1 == "12":
    def hexadecimal_to_octal(hexadecimal_str):
        try:
            if not all(char in '0123456789ABCDEFabcdef' for char in hexadecimal_str):
                raise ValueError("Input is not a valid hexadecimal number.")
            decimal_value = int(hexadecimal_str, 16)
            octal_value = oct(decimal_value)[2:]
            return octal_value
        except ValueError as e:
            return f"Error: {e}"
    if __name__ == "__main__":
        hexadecimal_input = input("Enter a hexadecimal number: ")
        result = hexadecimal_to_octal(hexadecimal_input)
    print(f"Octal value: {result}")
elif num1 == "13":
     print('''***This program is designed to translate machine language***
    ***MLC stand for Machine Language Translator***
       ***Create by Himanshu Jangir***
                                               For more information visit 
                                                  www.thepyexperthub.in''')
else:
    print("***Incorrect number!!!!***")
num2=str(input("Continue/Exit :"))
if num2=="Continue":
    a = input('''
<- Choose any convertor -> 
1.Binary to Decimal      (press 1)
2.Binary to Octal        (press 2)
3.Binary to Hexadecimal  (press 3)
4.Decimal to Binary      (press 4)
5.Decimal to Octal       (press 5)
6.Decimal to Hexadecimal (press 6)
7.Octal to Binary        (press 7)
8.Octal to Decimal       (press 8)
9.Octal to Hexadecimal   (press 9)
10.Hexadecimal to Binary  (press 10)
11.Hexadecimal to Decimal (press 11)
12.Hexadecimal to Octal   (press 12)
    Enter your choose number :''')
if a == "1":
    def binary_to_decimal(binary_str):
        try:
            if not all(char in '01' for char in binary_str):
                raise ValueError(binary_input,"is not a binary number.")
            decimal_value = int(binary_str, 2)
            return decimal_value
        except ValueError as e:
            return f"Error: {e}"
    if __name__ == "__main__":
        binary_input = input("Enter a Binary number:")
        result = binary_to_decimal(binary_input)
    print(f"Decimal value: {result}")
elif a == "2":
    def binary_to_octal(binary_str):
        try:
            if not all(char in '01' for char in binary_str):
                raise ValueError(binary_input,"is not a valid binary number.")
            decimal_value = int(binary_str, 2)
            octal_value = oct(decimal_value)[2:]
            return octal_value
        except ValueError as e:
            return f"Error: {e}"
    if __name__ == "__main__":
        binary_input = input("Enter a binary number: ")
        result = binary_to_octal(binary_input)
    print(f"Octal value: {result}")
elif a == "3":
    def binary_to_hexadecimal(binary_str):
        try:
            if not all(char in '01' for char in binary_str):
                raise ValueError("Input is not a valid binary number.")
            decimal_value = int(binary_str, 2)
            hexadecimal_value = hex(decimal_value)[2:].upper()  
            return hexadecimal_value
        except ValueError as e:
            return f"Error: {e}"
    if __name__ == "__main__":
        binary_input = input("Enter a binary number: ")
        result = binary_to_hexadecimal(binary_input)
    print(f"Hexadecimal value: {result}")
elif a == "4":
    def decimal_to_binary(decimal_value):
        binary_value = bin(decimal_value)
        return binary_value[2:]
    decimal_value = int(input("Enter a decimal value: "))
    binary_value = decimal_to_binary(decimal_value)
    print(f"Binary value: {binary_value}")
elif a == "5":
    def decimal_to_octal(decimal_value):
        octal_value = oct(decimal_value)
        return octal_value[2:]
    decimal_value = int(input("Enter a decimal value: "))
    octal_value = decimal_to_octal(decimal_value)
    print(f"Octal value: {octal_value}")
elif a == "6":
    def decimal_to_hexadecimal(decimal_value):
        try:
            if not isinstance(decimal_value, int) or decimal_value < 0:
                raise ValueError("Input must be a non-negative integer.")
            hexadecimal_value = hex(decimal_value)[2:].upper()
            return hexadecimal_value
        except ValueError as e:
            return f"Error: {e}"
    if __name__ == "__main__":
        try:
            decimal_input = int(input("Enter a decimal number: "))
            result = decimal_to_hexadecimal(decimal_input)
            print(f"Hexadecimal value: {result}")
        except ValueError:
            print("Error: Input must be a valid integer.")
elif a == "7":
    def octal_to_binary(octal_str):
        try:
            if not all(char in '01234567' for char in octal_str):
                raise ValueError("Input is not a valid octal number.")
            decimal_value = int(octal_str, 8)
            binary_value = bin(decimal_value)[2:]
            return binary_value
        except ValueError as e:
            return f"Error: {e}"
    if __name__ == "__main__":
        octal_input = input("Enter an octal number: ")
        result = octal_to_binary(octal_input)
    print(f"Binary value: {result}")
elif a == "8":
    def octal_to_decimal(octal_str):
        try:
            if not all(char in '01234567' for char in octal_str):
                raise ValueError("Input is not a valid octal number.")
            decimal_value = int(octal_str, 8)
            return decimal_value
        except ValueError as e:
            return f"Error: {e}"
    if __name__ == "__main__":
        octal_input = input("Enter an octal number: ")
        result = octal_to_decimal(octal_input)
    print(f"Decimal value: {result}")
elif a == "9":
    def octal_to_hexadecimal(octal_str):
        try:
            if not all(char in '01234567' for char in octal_str):
                raise ValueError("Input is not a valid octal number.")
            decimal_value = int(octal_str, 8)
            hexadecimal_value = hex(decimal_value)[2:].upper()  
            return hexadecimal_value
        except ValueError as e:
            return f"Error: {e}"
    if __name__ == "__main__":
        octal_input = input("Enter an octal number: ")
        result = octal_to_hexadecimal(octal_input)
    print(f"Hexadecimal value: {result}")
elif a == "10":
    def hexadecimal_to_binary(hexadecimal_str):
        try:
            if not all(char in '0123456789ABCDEFabcdef' for char in hexadecimal_str):
                raise ValueError("Input is not a valid hexadecimal number.")
            decimal_value = int(hexadecimal_str, 16)
            binary_value = bin(decimal_value)[2:]
            return binary_value
        except ValueError as e:
            return f"Error: {e}"
    if __name__ == "__main__":
        hexadecimal_input = input("Enter a hexadecimal number: ")
        result = hexadecimal_to_binary(hexadecimal_input)
    print(f"Binary value: {result}")
elif a == "11":
    def hexadecimal_to_decimal(hexadecimal_str):
        try:
            if not all(char in '0123456789ABCDEFabcdef' for char in hexadecimal_str):
                raise ValueError("Input is not a valid hexadecimal number.")
            decimal_value = int(hexadecimal_str, 16)
            return decimal_value
        except ValueError as e:
            return f"Error: {e}"
    if __name__ == "__main__":
        hexadecimal_input = input("Enter a hexadecimal number: ")
        result = hexadecimal_to_decimal(hexadecimal_input)
    print(f"Decimal value: {result}")
elif a == "12":
    def hexadecimal_to_octal(hexadecimal_str):
        try:
            if not all(char in '0123456789ABCDEFabcdef' for char in hexadecimal_str):
                raise ValueError("Input is not a valid hexadecimal number.")
            decimal_value = int(hexadecimal_str, 16)
            octal_value = oct(decimal_value)[2:]
            return octal_value
        except ValueError as e:
            return f"Error: {e}"
    if __name__ == "__main__":
        hexadecimal_input = input("Enter a hexadecimal number: ")
        result = hexadecimal_to_octal(hexadecimal_input)
    print(f"Octal value: {result}")
elif a == "13":
     print('''***This program is designed to translate machine language***
    ***MLC stand for Machine Language Translator***
       ***Create by Himanshu Jangir***
                                               For more information visit 
                                                  www.thepyexperthub.in''')
     print("***End of program***")