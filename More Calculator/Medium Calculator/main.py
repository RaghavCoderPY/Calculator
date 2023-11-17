def calculate(num1, num2, operator) -> int:
    match operator:
        case "+":
            return num1 + num2
        case "-":
            return num1 - num2
        case "x" | "*":
            return num1 * num2
        case "/":
            return num1 / num2
        case _:
            raise NameError(f"No operator name {operator}")


if __name__ == "__main__":
    a = int(input("Enter the first value\n"))
    b = int(input("Enter the second value\n"))
    c = input("Operator: ")
    print(f"{a} {"x" if c == "*" else c} b = {calculate(a, b, c)}")
