from units import *


# units = ("m", "cm", "km", "kg", "g", "ml", "l")
def add(num1: float, num2: float) -> float:
    return num1 + num2


def subtract(num1: float, num2: float) -> float:
    return num1 - num2


def multiply(num1: float, num2: float) -> float:
    return num1 * num2


def divide(num1: float, num2: float) -> float:
    return num1 / num2


if __name__ == "__main__":
    req = int(input("Unit Calculator -> 1\nStandard Calculator -> 2\n>> "))
    if req == 1:
        num = float(input("Number: "))
        unit = input(f"Unit of {num}: ")
        con = input("Convert to: ").lower()

        if unit == "m" and con == "cm":
            print(convert_meters(num))

        elif unit == "m" and con == "km":
            print(convert_meters(num, "km"))

        elif unit == "cm" and con == "m":
            print(convert_centimetre(num))

        elif unit == "cm" and con == "km":
            print(convert_centimetre(num, "km"))

        elif unit == "km" and con == "m":
            print(convert_kilometre(num))

        elif unit == "l" and con == "ml":
            print(convert_liter(num))

        elif unit == "ml" and con == "l":
            print(convert_milliliter(num))

        elif unit == "kg" and con == "g":
            print(convert_kilogram(num))

        elif unit == "g" and con == "kg":
            print(convert_gram(num))

    elif req == 2:
        a = float(input("Enter the first number\n"))
        b = float(input("Enter the second number\n"))
        c = float(input("Operator: "))

        match c:
            case "+":
                add(a, b)
            case "-":
                subtract(a, b)
            case "x" | "*":
                multiply(a, b)
            case "/":
                divide(a, b)
