# declare sum, subtract, multiply, divide functions and get input two numbers from user and print the sum, subtract, multiply, divide of two numbers


def sum(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


def main():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    if b == 0:
        print("Divide by zero error")
    print("Sum: ", sum(a, b))
    print("Subtract: ", subtract(a, b))
    print("Multiply: ", multiply(a, b))
    print("Divide: ", divide(a, b))


if __name__ == "__main__":
    main()