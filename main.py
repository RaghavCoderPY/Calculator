def calculate(a, b, operator = "+"):
    if operator == "+":
        return a + b
    elif operator == "-":
        return a - b
    elif operator == "*":
        return a * b
    elif operator == "/":
        return a / b
    

def geometric_mean(a, b):
    return (a * b) / (a + b)


ch = 10
while ch > 0:
    print("You have {} chances".format(ch))
    a = int(input("Enter number 1\n"))
    b = int(input("Enter number 2\n"))
    c = input("Operator: ")
    print(f"Ans: calculate(a, b, c)")
    print(f"Geometric Mean: {geometric_mean(a, b)}")
    ch = ch - 1
